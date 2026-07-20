"""Data access for the Eliozo Flask app.

This package replaces the previous Apache Jena Fuseki HTTP integration with
an embedded pyoxigraph store. Repositories import :func:`sparql_query` and
get back the same SPARQL 1.1 JSON Results string that Fuseki used to return,
so call sites (e.g. ``json.loads(...)["results"]["bindings"]``) are unchanged.

The on-disk store location can be overridden with the ``OXIGRAPH_DB_PATH``
environment variable. See ``README.md`` in this directory for how to import
TTL data and run test queries.
"""

import os
import threading

from pyoxigraph import QueryResultsFormat, Store

_DEFAULT_DB_PATH = os.path.normpath(
    os.path.join(os.path.dirname(__file__), "..", "data", "oxigraph_db")
)
OXIGRAPH_DB_PATH = os.environ.get("OXIGRAPH_DB_PATH", _DEFAULT_DB_PATH)

_store = None
_store_lock = threading.Lock()


def get_store():
    """Return a process-wide, read-only handle to the oxigraph store."""
    global _store
    if _store is not None:
        return _store
    with _store_lock:
        if _store is None:
            if not os.path.isdir(OXIGRAPH_DB_PATH):
                raise RuntimeError(
                    f"Oxigraph store not found at {OXIGRAPH_DB_PATH!r}. "
                    "Run `python -m eliozo_dao.load_rdf` to import RDF data, "
                    "or set the OXIGRAPH_DB_PATH environment variable."
                )
            _store = Store.read_only(OXIGRAPH_DB_PATH)
    return _store


def sparql_query(query: str) -> str:
    """Execute a SPARQL SELECT/ASK query, return the SPARQL JSON result as a string.

    Matches the wire format the old Fuseki HTTP endpoint returned, so existing
    ``json.loads(...)`` call sites keep working unchanged.
    """
    results = get_store().query(query)
    return results.serialize(format=QueryResultsFormat.JSON).decode("utf-8")
