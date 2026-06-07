"""Tests for the references repository (sources index)."""

from eliozo_dao.references_repository import getSPARQLSources


def test_get_sources_returns_python_dicts(hermetic_store):
    """getSPARQLSources returns parsed Python list, not raw JSON."""
    sources = getSPARQLSources("lv")
    assert isinstance(sources, list)
    assert len(sources) == 1
    src = sources[0]
    assert set(src.keys()) == {"label", "name", "description", "url"}
    assert src["label"] == "AMO"
    assert src["url"] == "https://example.org/amo"


def test_get_sources_language_filter(hermetic_store):
    """English query should return nothing — fixture has only @lv sources."""
    sources_en = getSPARQLSources("en")
    assert sources_en == []
