"""Tests for the Filter page queries in ``eliozo_dao.filter_repository``.

The Filter page lists problems through ``problem_listing.listProblemsPage``,
the same way as search, so the tests check that every problem is listed once,
in SEARCH_RESULT_ORDER, with one translation, and that the counts next to the
filters count problems rather than rows.
"""

import json

import pytest

from eliozo_dao.filter_repository import (
    getProblemCountsByFiltersSPARQL,
    getProblemsByFiltersSPARQL,
)
from eliozo_dao.problem_listing import listProblemsPage


FILTER_FIXTURE_TTL = r'''
@prefix eliozo: <http://www.dudajevagatve.lv/eliozo#> .

# Two translations and two solutions: one problem, however many rows it makes.
eliozo:LV.AMO.2020.9.1 a eliozo:Problem ;
    eliozo:problemID "LV.AMO.2020.9.1" ;
    eliozo:suggestedGrade 9 ; eliozo:problemGrade 9 ;
    eliozo:problemYear 2020 ; eliozo:country "LV" ;
    eliozo:olympiadType "RegionalOrOpen" ;
    eliozo:problemTextHtml "<p>2020.9.1 lv</p>"@lv , "<p>2020.9.1 en</p>"@en ;
    eliozo:problemSolution eliozo:SOLN.A , eliozo:SOLN.B .

eliozo:SOLN.A eliozo:solutionTextHtml "<p>A</p>"@lv .
eliozo:SOLN.B eliozo:solutionTextHtml "<p>B</p>"@lv .

eliozo:LV.AMO.2021.9.2 a eliozo:Problem ;
    eliozo:problemID "LV.AMO.2021.9.2" ;
    eliozo:suggestedGrade 9 ; eliozo:problemGrade 9 ;
    eliozo:problemYear 2021 ; eliozo:country "LV" ;
    eliozo:olympiadType "RegionalOrOpen" ;
    eliozo:problemTextHtml "<p>2021.9.2 lv</p>"@lv .

# The lv text is an empty placeholder, as on the IMO shortlist.
eliozo:EE.PK.2021.9.1 a eliozo:Problem ;
    eliozo:problemID "EE.PK.2021.9.1" ;
    eliozo:suggestedGrade 9 ; eliozo:problemGrade 9 ;
    eliozo:problemYear 2021 ; eliozo:country "EE" ;
    eliozo:olympiadType "National" ;
    eliozo:problemTextHtml ""@lv , "<p>PK en</p>"@en , "<p>PK ee</p>"@ee .

eliozo:LV.AMO.2021.10.1 a eliozo:Problem ;
    eliozo:problemID "LV.AMO.2021.10.1" ;
    eliozo:suggestedGrade 10 ; eliozo:problemGrade 10 ;
    eliozo:problemYear 2021 ; eliozo:country "LV" ;
    eliozo:olympiadType "RegionalOrOpen" ;
    eliozo:problemTextHtml "<p>2021.10.1 lv</p>"@lv .
'''

NO_FILTER = dict(grade="NA", olympiad="NA", domain="NA", questionType="NA",
                 method="NA", hasSolution="NA", hasVideo="NA")


@pytest.fixture
def filter_store(monkeypatch):
    from pyoxigraph import RdfFormat, Store

    import eliozo_dao

    store = Store()
    store.load(input=FILTER_FIXTURE_TTL, format=RdfFormat.TURTLE)
    monkeypatch.setattr(eliozo_dao, "_store", store, raising=False)
    yield store


def listing(uiLang="lv", offset=0, pageSize=10, **filters):
    params = dict(NO_FILTER, **filters)
    return listProblemsPage(getProblemsByFiltersSPARQL(params), uiLang, offset, pageSize)


def count(**filters):
    raw = getProblemCountsByFiltersSPARQL(dict(NO_FILTER, **filters))
    return int(json.loads(raw)["results"]["bindings"][0]["count"]["value"])


def test_each_problem_is_listed_once_in_result_order(filter_store):
    result = listing(grade="9")
    assert [p["problemid"] for p in result["problems"]] == [
        "EE.PK.2021.9.1", "LV.AMO.2021.9.2", "LV.AMO.2020.9.1"]
    assert result["total"] == 3


def test_translation_follows_the_precedence_rules(filter_store):
    shown = {p["problemid"]: p["textHtml"] for p in listing(grade="9")["problems"]}
    assert shown["LV.AMO.2020.9.1"] == "<p>2020.9.1 lv</p>"
    assert shown["EE.PK.2021.9.1"] == "<p>PK en</p>"      # empty lv placeholder skipped

    shown = {p["problemid"]: p["textHtml"] for p in listing(uiLang="lt", grade="9")["problems"]}
    assert shown["LV.AMO.2020.9.1"] == "<p>2020.9.1 en</p>"


def test_pages(filter_store):
    first = listing(grade="9", pageSize=2)
    second = listing(grade="9", offset=2, pageSize=2)
    assert [p["problemid"] for p in first["problems"] + second["problems"]] == [
        "EE.PK.2021.9.1", "LV.AMO.2021.9.2", "LV.AMO.2020.9.1"]
    assert first["total"] == second["total"] == 3


def test_counts_count_problems_not_solutions(filter_store):
    assert count(hasSolution="1") == 1          # one problem with two solutions
    assert len(listing(hasSolution="1")["problems"]) == 1


def test_counts_agree_with_the_listing(filter_store):
    for filters in ({}, {"grade": "9"}, {"grade": "10"}, {"olympiad": "National"},
                    {"hasSolution": "-"}):
        assert count(**filters) == listing(**filters)["total"], filters
