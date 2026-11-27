"""The WSGI application of the read-only SPARQL endpoint.

Routes, below ``SPARQL_PATH_PREFIX`` (default ``/sparql``):

    /sparql            SPARQL 1.1 Protocol queries (GET, POST); without a query:
                       the Service Description (or a help page for browsers)
    /sparql/void       VoID description of the data
    /sparql/graph      read-only Graph Store Protocol: ?default or ?graph=IRI
    /sparql/health     JSON status for monitoring

Gunicorn runs ``sparql_endpoint.app:application``; for local testing run
``python -m sparql_endpoint``.
"""

import hashlib
import html
import json
import logging
import os
import time
from datetime import datetime, timezone
from urllib.parse import parse_qs

from pyoxigraph import DefaultGraph, NamedNode, QueryBoolean, QuerySolutions, QueryTriples

from . import description, results
from .config import Settings
from .protocol import (GRAPH_FORMATS, RDF_FORMATS, RESULT_FORMATS, ProtocolError,
                       check_query, negotiate, parse_request, prefers_html)
from .store import StoreHolder, StoreUnavailable

log = logging.getLogger('sparql_endpoint')

_STATUS = {200: 'OK', 204: 'No Content', 400: 'Bad Request', 404: 'Not Found',
           405: 'Method Not Allowed', 406: 'Not Acceptable', 413: 'Content Too Large',
           415: 'Unsupported Media Type', 500: 'Internal Server Error',
           503: 'Service Unavailable'}

CORS_HEADERS = [
    ('Access-Control-Allow-Origin', '*'),
    ('Access-Control-Expose-Headers', 'X-SPARQL-Truncated, X-SPARQL-Limit'),
]

_TEXT_TYPES = ('text/', 'application/sparql-results+', 'application/n-triples',
               'application/rdf+xml', 'application/ld+json', 'application/json')


def _content_type(media):
    return media + '; charset=utf-8' if media.startswith(_TEXT_TYPES) else media


def _iso(timestamp):
    if timestamp is None:
        return None
    return datetime.fromtimestamp(timestamp, timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')


class SparqlApplication:
    def __init__(self, settings=None, holder=None, clock=time.monotonic):
        self.settings = settings or Settings.from_env()
        self.holder = holder or StoreHolder(self.settings.store_path,
                                            self.settings.reload_check,
                                            self.settings.reload_settle)
        self.clock = clock
        self.started_at = time.time()
        self.request_count = 0
        self._cache_generation = None
        self._cache = {}

    # --- WSGI entry --------------------------------------------------------

    def __call__(self, environ, start_response):
        start = self.clock()
        self.request_count += 1
        method = environ['REQUEST_METHOD']
        path = environ.get('PATH_INFO', '') or '/'
        prefix = self.settings.path_prefix
        info = {}
        try:
            if method == 'OPTIONS':
                status, headers, body = self._preflight(environ)
            elif path in (prefix, prefix + '/'):
                status, headers, body = self._endpoint(environ, info)
            elif path == prefix + '/void':
                status, headers, body = self._void(environ)
            elif path == prefix + '/graph':
                status, headers, body = self._graph_store(environ)
            elif path == prefix + '/health':
                status, headers, body = self._health(environ)
            else:
                raise ProtocolError(404, f'Not found: {path}')
        except ProtocolError as e:
            status, headers, body = self._error(e.status, e.message)
        except StoreUnavailable as e:
            log.error('store unavailable: %s', e)
            status, headers, body = self._error(503, 'The RDF store is not available. '
                                                     'Try again later.')
        except Exception:
            log.exception('unexpected error')
            status, headers, body = self._error(500, 'Internal server error.')

        if 'query' in info:
            self._log_query(environ, status, info, self.clock() - start)
        headers = headers + CORS_HEADERS + [('Content-Length', str(len(body)))]
        start_response(f'{status} {_STATUS.get(status, "")}', headers)
        return [b''] if method == 'HEAD' else [body]

    # --- responses ---------------------------------------------------------

    def _error(self, status, message):
        headers = [('Content-Type', 'text/plain; charset=utf-8')]
        if status == 405:
            headers.append(('Allow', 'GET, HEAD, POST, OPTIONS'))
        return status, headers, f'Error {status}: {message}\n'.encode('utf-8')

    def _preflight(self, environ):
        requested = environ.get('HTTP_ACCESS_CONTROL_REQUEST_HEADERS', '')
        return 204, [
            ('Access-Control-Allow-Methods', 'GET, HEAD, POST, OPTIONS'),
            ('Access-Control-Allow-Headers', requested or 'Accept, Content-Type'),
            ('Access-Control-Max-Age', '86400'),
            ('Allow', 'GET, HEAD, POST, OPTIONS'),
        ], b''

    def endpoint_url(self, environ):
        if self.settings.public_url:
            return self.settings.public_url
        scheme = environ.get('HTTP_X_FORWARDED_PROTO') or environ.get('wsgi.url_scheme', 'http')
        host = environ.get('HTTP_HOST') or environ.get('SERVER_NAME', 'localhost')
        return f'{scheme}://{host}{self.settings.path_prefix}'

    def _rdf_response(self, environ, triples, prefixes=None):
        fmt = negotiate(GRAPH_FORMATS, environ.get('HTTP_ACCEPT'), self._format_param(environ))
        if fmt is None:
            raise ProtocolError(406, 'None of the requested formats is available. Use '
                                + ', '.join(m for _, m, _ in GRAPH_FORMATS) + '.')
        key, media = fmt
        body = results.graph_bytes(triples, RDF_FORMATS[key], prefixes or results.PREFIXES)
        return 200, [('Content-Type', _content_type(media)), ('Vary', 'Accept')], body

    @staticmethod
    def _format_param(environ):
        values = parse_qs(environ.get('QUERY_STRING', '')).get('format')
        return values[0] if values else None

    # --- per-store-generation cache (VoID, triple count) -------------------

    def _cached(self, key, compute):
        generation = self.holder.generation
        if generation != self._cache_generation:
            self._cache_generation, self._cache = generation, {}
        if key not in self._cache:
            self._cache[key] = compute()
        return self._cache[key]

    def _triple_count(self, store):
        return self._cached('triples', lambda: len(store))

    # --- /sparql -----------------------------------------------------------

    def _endpoint(self, environ, info):
        if environ['REQUEST_METHOD'] not in ('GET', 'HEAD', 'POST'):
            raise ProtocolError(405, f'Method {environ["REQUEST_METHOD"]} is not allowed.')
        req = parse_request(environ, self.settings.max_request_bytes)
        if req.query is None:
            return self._service_description(environ)
        info['query'] = req.query
        info['sha'] = hashlib.sha1(req.query.encode('utf-8', 'replace')).hexdigest()[:10]
        # Logged before running, so a query that gets its worker killed by the
        # hard timeout still leaves its text in the log (no matching 'done' line).
        text = ''
        if self.settings.log_query_chars > 0:
            text = ' '.join(req.query.split())[:self.settings.log_query_chars]
        log.info('query sha=%s ip=%s len=%d q=%s', info['sha'], self._client_ip(environ),
                 len(req.query), json.dumps(text, ensure_ascii=False))
        return self._query(environ, req, info)

    def _service_description(self, environ):
        url = self.endpoint_url(environ)
        if prefers_html(environ.get('HTTP_ACCEPT')):
            return 200, [('Content-Type', 'text/html; charset=utf-8'), ('Vary', 'Accept')], \
                self._help_page(url)
        store = self.holder.get()
        triples = description.service_description(url, self.settings, self._triple_count(store))
        return self._rdf_response(environ, triples, description.DESCRIPTION_PREFIXES)

    def _query(self, environ, req, info):
        s = self.settings
        check_query(req.query, s.max_query_length)
        store = self.holder.get()
        kwargs = {}
        if req.default_graphs:
            kwargs['default_graph'] = req.default_graphs
        if req.named_graphs:
            kwargs['named_graphs'] = req.named_graphs
        deadline = self.clock() + s.query_timeout
        try:
            answer = store.query(req.query, **kwargs)
        except SyntaxError as e:
            raise ProtocolError(400, f'Query syntax error: {e}')
        except OSError as e:
            raise ProtocolError(500, f'Query evaluation failed: {e}')

        headers = [('Vary', 'Accept')]
        if isinstance(answer, QueryBoolean):
            info['kind'] = 'ASK'
            fmt = self._result_format(environ, req)
            body = results.ASK_WRITERS[fmt[0]](bool(answer))
            return 200, headers + [('Content-Type', _content_type(fmt[1]))], body

        if isinstance(answer, QuerySolutions):
            info['kind'] = 'SELECT'
            fmt = self._result_format(environ, req)
            variables = [v.value for v in answer.variables]
            n = len(variables)
            rows, truncated = self._collect(answer, s.max_rows, deadline,
                                            lambda sol: tuple(sol[i] for i in range(n)))
            body = results.SELECT_WRITERS[fmt[0]](variables, rows)
            limit = s.max_rows
        elif isinstance(answer, QueryTriples):
            info['kind'] = 'CONSTRUCT/DESCRIBE'
            fmt = negotiate(GRAPH_FORMATS, environ.get('HTTP_ACCEPT'), req.format)
            if fmt is None:
                raise ProtocolError(406, 'None of the requested formats is available. Use '
                                    + ', '.join(m for _, m, _ in GRAPH_FORMATS) + '.')
            rows, truncated = self._collect(answer, s.max_triples, deadline, lambda t: t)
            body = results.graph_bytes(rows, RDF_FORMATS[fmt[0]])
            limit = s.max_triples
        else:
            raise ProtocolError(500, 'Unexpected query result type.')

        info['rows'], info['truncated'] = len(rows), truncated
        headers.append(('Content-Type', _content_type(fmt[1])))
        if truncated:
            headers += [('X-SPARQL-Truncated', 'true'), ('X-SPARQL-Limit', str(limit))]
        return 200, headers, body

    def _result_format(self, environ, req):
        fmt = negotiate(RESULT_FORMATS, environ.get('HTTP_ACCEPT'), req.format)
        if fmt is None:
            raise ProtocolError(406, 'None of the requested formats is available. Use '
                                + ', '.join(m for _, m, _ in RESULT_FORMATS) + '.')
        return fmt

    def _collect(self, iterator, limit, deadline, convert):
        """Up to ``limit`` items; (items, truncated). Raises 503 past the deadline."""
        items = []
        try:
            for item in iterator:
                if len(items) >= limit:
                    return items, True
                items.append(convert(item))
                if len(items) % 256 == 0 and self.clock() > deadline:
                    raise ProtocolError(503, self._timeout_message())
        except ProtocolError:
            raise
        except Exception as e:  # evaluation errors raised while iterating
            raise ProtocolError(500, f'Query evaluation failed: {e}')
        if self.clock() > deadline:
            raise ProtocolError(503, self._timeout_message())
        return items, False

    def _timeout_message(self):
        return (f'The query took longer than {self.settings.query_timeout:g} s and was '
                'stopped. Make it more selective or add a LIMIT.')

    # --- /sparql/void, /sparql/graph, /sparql/health -----------------------

    def _void(self, environ):
        if environ['REQUEST_METHOD'] not in ('GET', 'HEAD'):
            raise ProtocolError(405, 'Only GET is allowed here.')
        store = self.holder.get()
        url = self.endpoint_url(environ)
        triples = self._cached(('void', url), lambda: description.void_description(
            store, url, self.settings, _iso(self.holder.opened_at)))
        return self._rdf_response(environ, triples, description.DESCRIPTION_PREFIXES)

    def _graph_store(self, environ):
        if environ['REQUEST_METHOD'] not in ('GET', 'HEAD'):
            raise ProtocolError(405, 'The Graph Store is read-only: only GET is allowed.')
        params = parse_qs(environ.get('QUERY_STRING', ''), keep_blank_values=True)
        if ('default' in params) == ('graph' in params):
            raise ProtocolError(400, 'Give either ?default or ?graph=<IRI>.')
        store = self.holder.get()
        if 'default' in params:
            graph = DefaultGraph()
        else:
            try:
                graph = NamedNode(params['graph'][0])
            except ValueError:
                raise ProtocolError(400, 'Invalid graph IRI.')
            if not store.contains_named_graph(graph):
                raise ProtocolError(404, f'No graph named <{graph.value}>.')
        triples = []
        for quad in store.quads_for_pattern(None, None, None, graph):
            if len(triples) >= self.settings.max_triples:
                raise ProtocolError(413, f'The graph has more than {self.settings.max_triples} '
                                         'triples; use a CONSTRUCT query with LIMIT instead.')
            triples.append(quad.triple)
        return self._rdf_response(environ, triples)

    def _health(self, environ):
        try:
            store = self.holder.get()
            ok = bool(store.query('ASK {}'))
            triples = self._triple_count(store)
            status = 200 if ok else 503
        except StoreUnavailable as e:
            status, triples = 503, None
            log.error('health: %s', e)
        body = json.dumps({
            'status': 'ok' if status == 200 else 'unavailable',
            'store_path': self.settings.store_path,
            'store_generation': self.holder.generation,
            'store_opened_at': _iso(self.holder.opened_at),
            'triples': triples,
            'worker_pid': os.getpid(),
            'worker_started_at': _iso(self.started_at),
            'worker_requests': self.request_count,
        }, indent=1).encode('utf-8')
        return status, [('Content-Type', 'application/json'),
                        ('Cache-Control', 'no-store')], body

    # --- logging and help page ---------------------------------------------

    @staticmethod
    def _client_ip(environ):
        return environ.get('HTTP_X_REAL_IP') or environ.get('REMOTE_ADDR') or '-'

    def _log_query(self, environ, status, info, seconds):
        log.info('done  sha=%s ip=%s status=%s kind=%s rows=%s truncated=%s ms=%d',
                 info.get('sha', '-'), self._client_ip(environ), status,
                 info.get('kind', '-'), info.get('rows', '-'),
                 'yes' if info.get('truncated') else 'no', seconds * 1000)

    def _help_page(self, url):
        s = self.settings
        u = html.escape(url)
        example = html.escape(f'curl -H "Accept: application/sparql-results+json" '
                              f'--data-urlencode "query=SELECT * WHERE {{ ?s ?p ?o }} LIMIT 5" {url}')
        return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Eliozo SPARQL endpoint</title>
<style>body{{font-family:system-ui,sans-serif;max-width:46rem;margin:2rem auto;padding:0 1rem;
line-height:1.5;color:#222;background:#fff}}code,pre{{background:#f3f3f3;padding:.1rem .3rem}}
pre{{padding:.6rem;overflow-x:auto}}</style></head><body>
<h1>Eliozo SPARQL endpoint</h1>
<p>A read-only <a href="https://www.w3.org/TR/sparql11-protocol/">SPARQL 1.1 Protocol</a>
endpoint at <code>{u}</code>. Send queries with <code>GET ?query=</code> or <code>POST</code>
(<code>application/x-www-form-urlencoded</code> or <code>application/sparql-query</code>).
The response format follows the <code>Accept</code> header.</p>
<pre>{example}</pre>
<h2>Limits</h2>
<ul><li>Queries up to {s.max_query_length} characters; use POST for long queries.</li>
<li>At most {s.max_rows} result rows and {s.max_triples} triples. A cut-off response has the
header <code>X-SPARQL-Truncated: true</code>.</li>
<li>{s.query_timeout:g} s per query.</li>
<li>Updates and <code>SERVICE</code> (federated queries) are refused.</li>
<li>Requests per IP address are rate-limited (HTTP 429).</li></ul>
<h2>Descriptions</h2>
<ul><li><a href="{u}?format=turtle">Service description</a> (Turtle; also by <code>Accept</code>)</li>
<li><a href="{u}/void?format=turtle">VoID dataset description</a></li>
<li><a href="{u}/graph?default&amp;format=turtle">Default graph</a> (Graph Store Protocol, read-only)</li>
<li><a href="{u}/health">Health</a></li></ul>
</body></html>
'''.encode('utf-8')


def create_app(settings=None):
    logging.basicConfig(level=logging.INFO, format='%(levelname)s %(name)s: %(message)s')
    return SparqlApplication(settings)


class _LazyApplication:
    """Builds the application on the first request (after Gunicorn forks)."""

    def __init__(self):
        self._app = None

    def __call__(self, environ, start_response):
        if self._app is None:
            self._app = create_app()
        return self._app(environ, start_response)


application = _LazyApplication()
