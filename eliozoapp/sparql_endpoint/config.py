"""Settings of the SPARQL endpoint, read from environment variables.

On the server the values come from ``/etc/eliozo/sparql.env`` (loaded by the
``eliozo-sparql`` systemd unit), so limits can be changed with a restart and
no code change. Every variable is optional.

    OXIGRAPH_DB_PATH           store directory (same variable as the Flask app)
    SPARQL_PUBLIC_URL          public URL of the endpoint, used in the service
                               description; default: built from the request
    SPARQL_PATH_PREFIX         URL path of the endpoint (default /sparql)
    SPARQL_MAX_QUERY_LENGTH    max characters in a query (default 20000)
    SPARQL_MAX_REQUEST_BYTES   max POST body size in bytes (default 65536)
    SPARQL_MAX_ROWS            max SELECT rows returned (default 10000)
    SPARQL_MAX_TRIPLES         max CONSTRUCT/DESCRIBE/graph triples (default 50000)
    SPARQL_QUERY_TIMEOUT       seconds before a running query is abandoned
                               (default 20); Gunicorn kills the worker 10 s later
    SPARQL_RELOAD_CHECK        seconds between checks for a reloaded store (default 2)
    SPARQL_RELOAD_SETTLE       seconds a changed store must stay unchanged, with
                               no writer, before it is reopened (default 5)
    SPARQL_LOG_QUERY_CHARS     how much of each query to log (default 300, 0 = none)
    SPARQL_VOID_URI_SPACE      void:uriSpace in the VoID description
                               (default http://www.dudajevagatve.lv/eliozo#)
"""

import os
from dataclasses import dataclass

_DEFAULT_DB_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), '..', 'data', 'oxigraph_db'))


def _int(environ, name, default):
    value = environ.get(name, '').strip()
    return int(value) if value else default


def _float(environ, name, default):
    value = environ.get(name, '').strip()
    return float(value) if value else default


@dataclass(frozen=True)
class Settings:
    store_path: str = _DEFAULT_DB_PATH
    public_url: str = ''
    path_prefix: str = '/sparql'
    max_query_length: int = 20000
    max_request_bytes: int = 65536
    max_rows: int = 10000
    max_triples: int = 50000
    query_timeout: float = 20.0
    reload_check: float = 2.0
    reload_settle: float = 5.0
    log_query_chars: int = 300
    void_uri_space: str = 'http://www.dudajevagatve.lv/eliozo#'

    @classmethod
    def from_env(cls, environ=None):
        e = os.environ if environ is None else environ
        d = cls()
        return cls(
            store_path=e.get('OXIGRAPH_DB_PATH') or d.store_path,
            public_url=e.get('SPARQL_PUBLIC_URL', '').strip().rstrip('/'),
            path_prefix='/' + (e.get('SPARQL_PATH_PREFIX', '').strip().strip('/')
                               or d.path_prefix.strip('/')),
            max_query_length=_int(e, 'SPARQL_MAX_QUERY_LENGTH', d.max_query_length),
            max_request_bytes=_int(e, 'SPARQL_MAX_REQUEST_BYTES', d.max_request_bytes),
            max_rows=_int(e, 'SPARQL_MAX_ROWS', d.max_rows),
            max_triples=_int(e, 'SPARQL_MAX_TRIPLES', d.max_triples),
            query_timeout=_float(e, 'SPARQL_QUERY_TIMEOUT', d.query_timeout),
            reload_check=_float(e, 'SPARQL_RELOAD_CHECK', d.reload_check),
            reload_settle=_float(e, 'SPARQL_RELOAD_SETTLE', d.reload_settle),
            log_query_chars=_int(e, 'SPARQL_LOG_QUERY_CHARS', d.log_query_chars),
            void_uri_space=e.get('SPARQL_VOID_URI_SPACE', '').strip() or d.void_uri_space,
        )
