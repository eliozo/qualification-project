"""SPARQL 1.1 Protocol request handling: parameters, query checks, formats.

https://www.w3.org/TR/sparql11-protocol/#query-operation -- a query arrives
in one of three ways:

* ``GET  ?query=...``
* ``POST`` with ``Content-Type: application/x-www-form-urlencoded``
* ``POST`` with ``Content-Type: application/sparql-query`` (the query is the body)

plus optional ``default-graph-uri`` and ``named-graph-uri`` parameters.
Updates are refused: this endpoint is read-only.
"""

from dataclasses import dataclass, field
from urllib.parse import parse_qs

from pyoxigraph import NamedNode, RdfFormat

from eliozo_dao.advanced_search_repository import keywords


class ProtocolError(Exception):
    def __init__(self, status, message):
        super().__init__(message)
        self.status = status
        self.message = message


@dataclass
class SparqlRequest:
    query: str = None
    default_graphs: list = field(default_factory=list)
    named_graphs: list = field(default_factory=list)
    format: str = None            # the optional non-standard ``format`` parameter


_UPDATE_KEYWORDS = {'INSERT', 'DELETE', 'LOAD', 'CLEAR', 'DROP', 'CREATE',
                    'ADD', 'MOVE', 'COPY', 'WITH'}
_QUERY_FORMS = {'SELECT', 'ASK', 'CONSTRUCT', 'DESCRIBE'}

READ_ONLY_MESSAGE = 'SPARQL Update is not supported: this endpoint is read-only.'


def check_query(query, max_length):
    """Refuse queries that must not reach the store (raises ProtocolError).

    SERVICE is refused because the store would send HTTP requests to whatever
    address the query names. Keywords are looked for outside comments,
    strings and IRIs (see ``eliozo_dao.advanced_search_repository.keywords``).
    Syntax errors are left to the SPARQL parser.
    """
    if not query or not query.strip():
        raise ProtocolError(400, 'The query is empty.')
    if len(query) > max_length:
        raise ProtocolError(413, f'The query is longer than {max_length} characters.')
    words = keywords(query)
    if 'SERVICE' in words:
        raise ProtocolError(400, 'SERVICE (federated query) is not allowed on this endpoint.')
    first = next((w for w in words if w in _QUERY_FORMS or w in _UPDATE_KEYWORDS), None)
    if first in _UPDATE_KEYWORDS:
        raise ProtocolError(400, READ_ONLY_MESSAGE)


def _single(params, name):
    values = params.get(name, [])
    if len(values) > 1:
        raise ProtocolError(400, f'The {name} parameter may be given only once.')
    return values[0] if values else None


def _iris(params, name):
    out = []
    for value in params.get(name, []):
        try:
            out.append(NamedNode(value.strip()))
        except ValueError:
            raise ProtocolError(400, f'Invalid IRI in {name}: {value!r}')
    return out


def _read_body(environ, max_bytes):
    try:
        length = int(environ.get('CONTENT_LENGTH') or 0)
    except ValueError:
        raise ProtocolError(400, 'Invalid Content-Length.')
    if length > max_bytes:
        raise ProtocolError(413, f'The request body is larger than {max_bytes} bytes.')
    body = environ['wsgi.input'].read(length) if length else b''
    return body


def _decode(data, charset='utf-8'):
    try:
        return data.decode(charset or 'utf-8')
    except (UnicodeDecodeError, LookupError):
        raise ProtocolError(400, 'The request is not valid UTF-8.')


def parse_request(environ, max_request_bytes):
    """The SparqlRequest of a GET or POST; ``query`` is None when there is none."""
    method = environ['REQUEST_METHOD']
    url_params = parse_qs(environ.get('QUERY_STRING', ''), keep_blank_values=True)
    if method in ('GET', 'HEAD'):
        params = url_params
        if 'update' in params:
            raise ProtocolError(400, READ_ONLY_MESSAGE)
        query = _single(params, 'query')
    elif method == 'POST':
        ctype, _, rest = (environ.get('CONTENT_TYPE') or '').partition(';')
        ctype = ctype.strip().lower()
        charset = None
        for part in rest.split(';'):
            key, _, value = part.strip().partition('=')
            if key.lower() == 'charset':
                charset = value.strip('"\' ')
        body = _read_body(environ, max_request_bytes)
        if ctype == 'application/x-www-form-urlencoded':
            form = parse_qs(_decode(body), keep_blank_values=True)
            if 'update' in form or 'update' in url_params:
                raise ProtocolError(400, READ_ONLY_MESSAGE)
            params = {**url_params, **form}
            query = _single(params, 'query')
        elif ctype == 'application/sparql-query':
            params = url_params
            if 'query' in params:
                raise ProtocolError(400, 'With application/sparql-query the query must be '
                                         'the request body, not a query parameter.')
            query = _decode(body, charset)
            if not query.strip():
                raise ProtocolError(400, 'The query is empty.')
        elif ctype == 'application/sparql-update':
            raise ProtocolError(400, READ_ONLY_MESSAGE)
        else:
            raise ProtocolError(415, 'Use Content-Type application/x-www-form-urlencoded '
                                     'or application/sparql-query.')
        if query is None:
            raise ProtocolError(400, 'Missing query parameter.')
    else:
        raise ProtocolError(405, f'Method {method} is not allowed.')
    return SparqlRequest(query=query,
                         default_graphs=_iris(params, 'default-graph-uri'),
                         named_graphs=_iris(params, 'named-graph-uri'),
                         format=_single(params, 'format'))


# --- Content negotiation ----------------------------------------------------

# (key, media type of the response, other media types that select it).
# The order is the server's preference when the client does not mind.
RESULT_FORMATS = [
    ('json', 'application/sparql-results+json', ('application/json',)),
    ('xml', 'application/sparql-results+xml', ('application/xml', 'text/xml')),
    ('csv', 'text/csv', ()),
    ('tsv', 'text/tab-separated-values', ()),
]
GRAPH_FORMATS = [
    ('turtle', 'text/turtle', ('application/x-turtle',)),
    ('ntriples', 'application/n-triples', ('text/plain',)),
    ('rdfxml', 'application/rdf+xml', ('application/xml', 'text/xml')),
    ('jsonld', 'application/ld+json', ('application/json',)),
]
RDF_FORMATS = {
    'turtle': RdfFormat.TURTLE,
    'ntriples': RdfFormat.N_TRIPLES,
    'rdfxml': RdfFormat.RDF_XML,
    'jsonld': RdfFormat.JSON_LD,
}
# Short names accepted by the ``format`` parameter.
FORMAT_ALIASES = {
    'json': 'json', 'srj': 'json', 'xml': 'xml', 'srx': 'xml', 'csv': 'csv', 'tsv': 'tsv',
    'turtle': 'turtle', 'ttl': 'turtle', 'ntriples': 'ntriples', 'nt': 'ntriples',
    'n-triples': 'ntriples', 'rdfxml': 'rdfxml', 'rdf': 'rdfxml', 'rdf/xml': 'rdfxml',
    'jsonld': 'jsonld', 'json-ld': 'jsonld',
}


def parse_accept(header):
    """[(media range, q)] from an Accept header; malformed entries are skipped."""
    out = []
    for item in (header or '').split(','):
        parts = [p.strip() for p in item.split(';')]
        media = parts[0].lower()
        if '/' not in media:
            continue
        q = 1.0
        for p in parts[1:]:
            key, _, value = p.partition('=')
            if key.strip().lower() == 'q':
                try:
                    q = float(value)
                except ValueError:
                    q = 0.0
        out.append((media, q))
    return out


def _quality(accepted, media_types):
    """Quality of the best (most specific) range matching any of ``media_types``.

    The first media type is the one actually sent; the others are aliases
    that select it only when named exactly (``text/*`` must not pick a
    format that is sent as ``application/...`` because of a ``text/xml`` alias).
    """
    best = None    # (specificity, q)
    for index, media in enumerate(media_types):
        mtype = media.split('/')[0]
        for rng, q in accepted:
            if rng == media:
                spec = 3
            elif index > 0:
                continue
            elif rng == mtype + '/*':
                spec = 2
            elif rng == '*/*':
                spec = 1
            else:
                continue
            if best is None or spec > best[0] or (spec == best[0] and q > best[1]):
                best = (spec, q)
    return best[1] if best else 0.0


def negotiate(formats, accept_header, format_param=None):
    """(key, media type) of the response format, or None if nothing is acceptable."""
    if format_param:
        wanted = format_param.strip().lower()
        key = FORMAT_ALIASES.get(wanted)
        for k, media, aliases in formats:
            if k == key or wanted == media or wanted in aliases:
                return k, media
        raise ProtocolError(400, f'Unsupported format {format_param!r} for this query.')
    accepted = parse_accept(accept_header)
    if not accepted:
        return formats[0][0], formats[0][1]
    best = None
    for k, media, aliases in formats:
        q = _quality(accepted, (media,) + aliases)
        if q > 0 and (best is None or q > best[0]):
            best = (q, k, media)
    return (best[1], best[2]) if best else None


def prefers_html(accept_header):
    """True when a browser asks for a page (text/html ranked above Turtle and JSON)."""
    accepted = parse_accept(accept_header)
    html = _quality(accepted, ('text/html', 'application/xhtml+xml'))
    rdf = max(_quality(accepted, (m,) + a) for _, m, a in GRAPH_FORMATS)
    exact_html = any(r in ('text/html', 'application/xhtml+xml') for r, _ in accepted)
    return exact_html and html >= rdf
