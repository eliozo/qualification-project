"""Tests for search by meaning, without PostgreSQL or the OpenAI API.

``mergeHits`` is the pure part of ``eliozo_dao.postgres.semantic_search``;
``semanticSearchProblems`` is run with ``semanticSearch`` replaced by canned
hits and the texts shown taken from a small in-memory oxigraph store.
"""

import pytest

import eliozo_dao.postgres.semantic_search as semantic_search
from eliozo_dao.problem_listing import PAGE_SIZE
from eliozo_dao.postgres.semantic_search import mergeHits
from eliozo_dao.search_repository import (
    SEARCH_TARGET_PROBLEMS,
    SEARCH_TARGET_SOLUTIONS,
    semanticSearchProblems,
)


SEMANTIC_FIXTURE_TTL = '''
@prefix eliozo: <http://www.dudajevagatve.lv/eliozo#> .

eliozo:P1 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.5.1" ;
    eliozo:problemTextHtml "<p>Latviski</p>"@lv, "<p>In English</p>"@en .
eliozo:P2 a eliozo:Problem ;
    eliozo:problemID "LV.TST.2020.5.2" ;
    eliozo:problemTextHtml "<p>Tikai latviski</p>"@lv .
'''


@pytest.fixture
def semantic_store(monkeypatch):
    from pyoxigraph import RdfFormat, Store

    import eliozo_dao

    store = Store()
    store.load(input=SEMANTIC_FIXTURE_TTL, format=RdfFormat.TURTLE)
    monkeypatch.setattr(eliozo_dao, "_store", store, raising=False)
    return store


def _hit(problemid, inSolution=False, solutionLang=None, distance=0.1):
    return {'problemid': problemid, 'distance': distance, 'content': 'A & <b>', 'contentLang': 'lv',
            'inSolution': inSolution, 'solutionLang': solutionLang}


@pytest.fixture
def fake_hits(monkeypatch):
    """Set the hits the next semantic search returns; records the call."""
    calls = []

    def install(hits):
        def fake(queryText, includeSolutions):
            calls.append(includeSolutions)
            return hits
        monkeypatch.setattr(semantic_search, 'semanticSearch', fake)
        return calls
    return install


# --- mergeHits ---------------------------------------------------------------

def test_merge_orders_by_closest_text_and_limits():
    problems = [('A', 'a', 'lv', 0.30), ('B', 'b', 'lv', 0.10)]
    chunks = [('C', 'c', 'lv', 'lv', 0.20)]
    assert [r['problemid'] for r in mergeHits(problems, chunks, 2)] == ['B', 'C']


def test_merge_flags_solution_only_when_it_is_closer():
    problems = [('A', 'a', 'lv', 0.30), ('B', 'b', 'lv', 0.10)]
    chunks = [('A', 'a', 'lv', 'en', 0.20), ('A', 'a', 'lv', 'lv', 0.25), ('B', 'b', 'lv', 'lv', 0.40)]
    byId = {r['problemid']: r for r in mergeHits(problems, chunks, 10)}
    assert byId['A']['inSolution'] and byId['A']['solutionLang'] == 'en'
    assert byId['A']['distance'] == 0.20
    assert not byId['B']['inSolution'] and byId['B']['solutionLang'] is None
    assert byId['B']['distance'] == 0.10


def test_merge_problem_found_only_through_solution():
    [hit] = mergeHits([], [('C', 'c', 'lv', 'lt', 0.5)], 10)
    assert hit['inSolution'] and hit['solutionLang'] == 'lt'


# --- semanticSearchProblems --------------------------------------------------

def test_pages_through_hits(semantic_store, fake_hits):
    fake_hits([_hit('LV.TST.2020.5.1', distance=i / 100) for i in range(PAGE_SIZE + 3)])
    first = semanticSearchProblems('q', uiLang='lv')
    second = semanticSearchProblems('q', uiLang='lv', offset=PAGE_SIZE)
    assert first['total'] == second['total'] == PAGE_SIZE + 3
    assert len(first['problems']) == PAGE_SIZE
    assert len(second['problems']) == 3


def test_searches_solutions_only_when_asked(semantic_store, fake_hits):
    calls = fake_hits([])
    semanticSearchProblems('q', SEARCH_TARGET_PROBLEMS)
    semanticSearchProblems('q', SEARCH_TARGET_SOLUTIONS)
    assert calls == [False, True]


def test_shows_ui_language_and_links_solution_language(semantic_store, fake_hits):
    fake_hits([_hit('LV.TST.2020.5.1', inSolution=True, solutionLang='lv'),
               _hit('LV.TST.2020.5.2')])
    p1, p2 = semanticSearchProblems('q', SEARCH_TARGET_SOLUTIONS, uiLang='en')['problems']
    assert (p1['lang'], p1['textHtml']) == ('en', '<p>In English</p>')
    assert p1['solutionMatchLang'] == 'lv'
    assert p1['matchLang'] is None
    assert p2['solutionMatchLang'] is None


def test_untagged_solution_links_shown_language(semantic_store, fake_hits):
    fake_hits([_hit('LV.TST.2020.5.2', inSolution=True, solutionLang=None)])
    [p] = semanticSearchProblems('q', SEARCH_TARGET_SOLUTIONS, uiLang='en')['problems']
    assert p['solutionMatchLang'] == 'lv'


def test_problem_missing_from_rdf_store_shows_stored_text(semantic_store, fake_hits):
    fake_hits([_hit('LV.GONE.2020.5.1')])
    [p] = semanticSearchProblems('q', uiLang='lv')['problems']
    assert p['textHtml'] == '<p>A &amp; &lt;b&gt;</p>'
