"""Health checks for the embedded pyoxigraph backend.

These tests don't depend on the user's full RDF load — they spin up an
in-memory oxigraph store via the ``hermetic_store`` fixture (see
``tests/conftest.py``) and assert the adapter behaves correctly.
"""

import json

import pytest

import eliozo_dao
from eliozo_dao import sparql_query


def test_default_db_path_is_under_eliozoapp_data():
    """The default OXIGRAPH_DB_PATH should live next to the eliozoapp tree."""
    assert eliozo_dao.OXIGRAPH_DB_PATH.endswith("data/oxigraph_db")


def test_sparql_query_returns_valid_sparql_json(hermetic_store):
    raw = sparql_query("SELECT * WHERE { ?s ?p ?o } LIMIT 1")
    data = json.loads(raw)
    assert "head" in data
    assert "vars" in data["head"]
    # SPARQL doesn't guarantee var order for SELECT *, so compare as a set.
    assert set(data["head"]["vars"]) == {"s", "p", "o"}
    assert "results" in data
    assert "bindings" in data["results"]


def test_sparql_query_select_with_prefix(hermetic_store):
    raw = sparql_query("""
        PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
        SELECT (COUNT(*) AS ?n) WHERE {
          ?p a eliozo:Problem .
        }
    """)
    data = json.loads(raw)
    bindings = data["results"]["bindings"]
    assert len(bindings) == 1
    assert int(bindings[0]["n"]["value"]) >= 1


def test_sparql_query_literal_with_language_tag(hermetic_store):
    """SPARQL JSON encodes lang-tagged literals with xml:lang — verify
    the binding shape matches the SPARQL 1.1 Results spec."""
    raw = sparql_query("""
        PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
        SELECT ?name WHERE {
          ?o eliozo:olympiadName ?name .
          FILTER (lang(?name) = "lv")
        }
    """)
    data = json.loads(raw)
    bindings = data["results"]["bindings"]
    assert len(bindings) >= 1
    name = bindings[0]["name"]
    assert name["type"] == "literal"
    assert name["xml:lang"] == "lv"
    assert "value" in name


def test_get_store_singleton_is_reused(hermetic_store):
    """get_store() should return the same handle on repeated calls."""
    s1 = eliozo_dao.get_store()
    s2 = eliozo_dao.get_store()
    assert s1 is s2


def test_missing_store_raises_helpful_error(monkeypatch, tmp_path):
    """If OXIGRAPH_DB_PATH points to a nonexistent dir, the error must
    tell the operator how to fix it."""
    monkeypatch.setattr(eliozo_dao, "_store", None, raising=False)
    monkeypatch.setattr(eliozo_dao, "OXIGRAPH_DB_PATH",
                        str(tmp_path / "does-not-exist"))
    with pytest.raises(RuntimeError) as excinfo:
        eliozo_dao.get_store()
    msg = str(excinfo.value)
    assert "load_rdf" in msg
    assert "OXIGRAPH_DB_PATH" in msg
