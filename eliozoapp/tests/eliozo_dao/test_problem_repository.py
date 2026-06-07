"""Repository-level tests against an in-memory oxigraph store.

Uses the ``hermetic_store`` fixture from ``tests/conftest.py``.
"""

import json

from eliozo_dao.problem_repository import (
    getSPARQLOlympiads,
    getSPARQLProblem,
    getSPARQLVideoBookmarks,
)


def test_get_olympiads_returns_lv_language(hermetic_store):
    raw = getSPARQLOlympiads("lv")
    data = json.loads(raw)
    bindings = data["results"]["bindings"]
    assert len(bindings) == 1, "fixture has exactly one olympiad tagged @lv"
    row = bindings[0]
    assert row["olympiadCountry"]["value"] == "LV"
    assert row["olympiadCode"]["value"] == "AMO"
    assert row["olympiadName"]["xml:lang"] == "lv"


def test_get_olympiads_language_filter_works(hermetic_store):
    """The query's ``FILTER (lang(?name)=...)`` must exclude other languages."""
    lv_count = len(json.loads(getSPARQLOlympiads("lv"))["results"]["bindings"])
    en_count = len(json.loads(getSPARQLOlympiads("en"))["results"]["bindings"])
    assert lv_count == 1
    assert en_count == 1
    assert lv_count + en_count == 2  # fixture has one of each


def test_get_problem_returns_bound_text(hermetic_store):
    raw = getSPARQLProblem("LV.AMO.2011.5.1", "lv")
    data = json.loads(raw)
    bindings = data["results"]["bindings"]
    assert len(bindings) == 1
    assert "Test problem" in bindings[0]["problemTextHtml"]["value"]


def test_get_video_bookmarks_returns_ordered_rows(hermetic_store):
    raw = getSPARQLVideoBookmarks("LV.AMO.2011.5.1")
    data = json.loads(raw)
    bindings = data["results"]["bindings"]
    assert len(bindings) == 2, "fixture has exactly two bookmarks"
    # ORDER BY ?tstamp in the query — first row should be tstamp=5
    assert bindings[0]["tstamp"]["value"] == "5"
    assert bindings[1]["tstamp"]["value"] == "45"
    for row in bindings:
        assert row["youtubeID"]["value"] == "tWx-UGFeuSA"
        assert row["videoTitle"]["value"] == "AMO2011, 5.klases 1.uzdevums"


def test_get_problem_missing_returns_empty_bindings(hermetic_store):
    raw = getSPARQLProblem("DOES.NOT.EXIST", "lv")
    data = json.loads(raw)
    assert data["results"]["bindings"] == []
