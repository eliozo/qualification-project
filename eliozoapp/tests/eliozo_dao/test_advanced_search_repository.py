"""Tests for the advanced (SPARQL) search: query checks, grouping, the worker
process, the preset files in ``sparql_presets`` and the page itself.

Queries run against the small TTL fixture of ``tests/conftest.py``: in an
in-memory store for ``collect_rows`` and in an on-disk copy for
``run_query``, whose worker process opens the store by path.
"""

import pytest
from pyoxigraph import RdfFormat, Store

from conftest import FIXTURE_TTL
from eliozo_dao.advanced_search_repository import (
    DEFAULT_LIMIT,
    MAX_LIMIT,
    MAX_QUERY_LENGTH,
    QueryError,
    check_query,
    collect_rows,
    group_rows,
    parse_limit,
    run_query,
)

PREFIX = 'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\n'

EXTRA_TTL = """
@prefix eliozo: <http://www.dudajevagatve.lv/eliozo#> .
eliozo:LV.AMO.2011.5.2 a eliozo:Problem ; eliozo:problemID "LV.AMO.2011.5.2" ;
    eliozo:problemGrade 5 ; eliozo:domain "Alg" .
eliozo:LV.AMO.2011.6.1 a eliozo:Problem ; eliozo:problemID "LV.AMO.2011.6.1" ;
    eliozo:problemGrade 6 ; eliozo:domain "Comb" .
eliozo:LV.AMO.2011.6.2 a eliozo:Problem ; eliozo:problemID "LV.AMO.2011.6.2" ;
    eliozo:problemGrade 6 ; eliozo:domain "Alg" ; eliozo:domain "Comb" .
"""


def _load(store):
    store.load(input=FIXTURE_TTL, format=RdfFormat.TURTLE)
    store.load(input=EXTRA_TTL, format=RdfFormat.TURTLE)
    return store


@pytest.fixture
def store():
    return _load(Store())


@pytest.fixture(scope='module')
def db_path(tmp_path_factory):
    path = str(tmp_path_factory.mktemp('oxigraph') / 'db')
    s = _load(Store(path))
    s.flush()
    del s  # release the write lock so the worker can open it read-only
    return path


def _kind(query):
    with pytest.raises(QueryError) as info:
        check_query(query)
    return info.value.kind


# --- check_query -----------------------------------------------------------

def test_check_query_accepts_select():
    check_query(PREFIX + 'SELECT ?problemID WHERE { ?p eliozo:problemID ?problemID }')
    check_query('select * where { ?s ?p ?o }')


@pytest.mark.parametrize('query, kind', [
    ('', 'empty'),
    ('   \n ', 'empty'),
    ('# SELECT ?x WHERE {}', 'not_select'),
    ('ASK { ?s ?p ?o }', 'not_select'),
    ('CONSTRUCT { ?s ?p ?o } WHERE { ?s ?p ?o }', 'not_select'),
    ('DESCRIBE <http://example.org/a>', 'not_select'),
    ('INSERT DATA { <a:a> <a:a> <a:a> }', 'update'),
    (PREFIX + 'DELETE WHERE { ?s ?p ?o }', 'update'),
    ('SELECT ?x WHERE { SERVICE <http://example.org/sparql> { ?x ?p ?o } }', 'service'),
    ('SELECT ?x WHERE { service <http://example.org/sparql> { ?x ?p ?o } }', 'service'),
])
def test_check_query_refuses(query, kind):
    assert _kind(query) == kind


def test_check_query_refuses_long_query():
    assert _kind('SELECT * WHERE { ?s ?p ?o }' + ' ' * MAX_QUERY_LENGTH) == 'too_long'


def test_keywords_in_comments_strings_and_names_do_not_count():
    check_query(PREFIX + '''# INSERT, SERVICE and DELETE in a comment
SELECT ?problemID ?service WHERE {
  ?p eliozo:problemID ?problemID ; eliozo:service ?service .
  FILTER (?service != "SERVICE" && ?service != """DELETE""")
  FILTER (?p != <http://example.org/insert#SERVICE>)
}''')


# --- parse_limit -----------------------------------------------------------

@pytest.mark.parametrize('value, limit', [
    (None, DEFAULT_LIMIT), ('', DEFAULT_LIMIT), ('5', 5), (' 7 ', 7),
    ('100', 100), ('101', MAX_LIMIT), ('100000', MAX_LIMIT),
    ('0', None), ('-3', None), ('2.5', None), ('abc', None),
])
def test_parse_limit(value, limit):
    assert parse_limit(value) == limit


# --- collect_rows ----------------------------------------------------------

def test_collect_rows_plain(store):
    rows, truncated = collect_rows(store, PREFIX + '''
SELECT ?problemID WHERE { ?p eliozo:problemID ?problemID } ORDER BY ?problemID''', 10)
    assert [r['problemid'] for r in rows] == [
        'LV.AMO.2011.5.1', 'LV.AMO.2011.5.2', 'LV.AMO.2011.6.1', 'LV.AMO.2011.6.2']
    assert rows[0]['section'] is None and rows[0]['subsection'] is None
    assert truncated is False


def test_collect_rows_variable_names_are_case_insensitive(store):
    rows, _ = collect_rows(store, PREFIX + '''
SELECT ?PROBLEMID (?grade AS ?Section) WHERE {
  ?p eliozo:problemID ?PROBLEMID ; eliozo:problemGrade ?grade } ORDER BY ?PROBLEMID''', 10)
    assert rows[0] == {'problemid': 'LV.AMO.2011.5.1', 'section': '5', 'subsection': None}


def test_collect_rows_limit_and_truncation(store):
    query = PREFIX + 'SELECT ?problemID WHERE { ?p eliozo:problemID ?problemID } ORDER BY ?problemID'
    rows, truncated = collect_rows(store, query, 3)
    assert len(rows) == 3 and truncated is True
    rows, truncated = collect_rows(store, query, 4)
    assert len(rows) == 4 and truncated is False


def test_collect_rows_skips_repeats_and_unbound_ids(store):
    # Without DISTINCT every problem comes once per triple; one row has no ID.
    rows, _ = collect_rows(store, PREFIX + '''
SELECT ?problemID WHERE {
  { ?p eliozo:problemID ?problemID ; ?anyProperty ?anyValue }
  UNION { BIND ("x" AS ?other) }
}''', 100)
    assert sorted(r['problemid'] for r in rows) == [
        'LV.AMO.2011.5.1', 'LV.AMO.2011.5.2', 'LV.AMO.2011.6.1', 'LV.AMO.2011.6.2']


def test_collect_rows_shortens_iris(store):
    rows, _ = collect_rows(store, PREFIX + '''
SELECT ?problemID ?section WHERE { ?p eliozo:problemID ?problemID ; eliozo:topic ?section }''', 10)
    assert rows == [{'problemid': 'LV.AMO.2011.5.1', 'section': 'Algebra', 'subsection': None}]


def test_collect_rows_requires_problem_id(store):
    with pytest.raises(QueryError) as info:
        collect_rows(store, PREFIX + 'SELECT ?p WHERE { ?p a eliozo:Problem }', 10)
    assert info.value.kind == 'no_problem_id'


def test_collect_rows_syntax_error_has_position(store):
    query = PREFIX + 'SELECT ?problemID\nWHERE {\n  ?p eliozo:problemID ?problemID .\n  FILTRE (?x)\n}'
    with pytest.raises(QueryError) as info:
        collect_rows(store, query, 10)
    e = info.value
    assert e.kind == 'syntax'
    assert e.line == 5 and e.column >= 1
    assert e.line_text == '  FILTRE (?x)'
    assert e.message


# --- group_rows ------------------------------------------------------------

def test_group_rows_without_sections():
    rows = [{'problemid': 'A', 'section': None, 'subsection': None},
            {'problemid': 'B', 'section': None, 'subsection': None}]
    assert group_rows(rows) == [
        {'title': None, 'subsections': [{'title': None, 'problemids': ['A', 'B']}]}]


def test_group_rows_two_levels_keep_first_seen_order():
    rows = [{'problemid': 'A', 'section': 'S2', 'subsection': 'x'},
            {'problemid': 'B', 'section': 'S1', 'subsection': 'y'},
            {'problemid': 'C', 'section': 'S2', 'subsection': 'z'},
            {'problemid': 'D', 'section': 'S2', 'subsection': 'x'}]
    assert group_rows(rows) == [
        {'title': 'S2', 'subsections': [{'title': 'x', 'problemids': ['A', 'D']},
                                         {'title': 'z', 'problemids': ['C']}]},
        {'title': 'S1', 'subsections': [{'title': 'y', 'problemids': ['B']}]},
    ]


def test_group_rows_empty():
    assert group_rows([]) == []


# --- run_query (worker process) --------------------------------------------

def test_run_query_in_worker(db_path):
    rows, truncated = run_query(PREFIX + '''
SELECT ?problemID (?grade AS ?section) (?domain AS ?subsection) WHERE {
  ?p eliozo:problemID ?problemID ; eliozo:problemGrade ?grade ; eliozo:domain ?domain
} ORDER BY ?grade ?domain ?problemID''', 10, db_path=db_path)
    assert truncated is False
    assert group_rows(rows) == [
        {'title': '5', 'subsections': [{'title': 'Alg', 'problemids': ['LV.AMO.2011.5.2']}]},
        {'title': '6', 'subsections': [{'title': 'Alg', 'problemids': ['LV.AMO.2011.6.2']},
                                        {'title': 'Comb', 'problemids': ['LV.AMO.2011.6.1',
                                                                         'LV.AMO.2011.6.2']}]},
    ]


def test_run_query_caps_limit(db_path):
    rows, truncated = run_query(PREFIX + '''
SELECT ?problemID WHERE { VALUES ?n { 1 2 3 4 5 6 7 8 9 10 11 12 } ?p eliozo:problemID ?id .
  BIND (CONCAT(?id, "-", STR(?n)) AS ?problemID) }''', 1000, db_path=db_path)
    assert len(rows) == 48 and truncated is False
    rows, truncated = run_query('SELECT ?problemID WHERE { ?s ?p ?o . ?s2 ?p2 ?o2 . '
                                'BIND (CONCAT(STR(?s), STR(?o), STR(?s2), STR(?o2)) AS ?problemID) }',
                                1000, db_path=db_path)
    assert len(rows) == MAX_LIMIT and truncated is True


def test_run_query_reports_worker_errors(db_path):
    # A syntax error, and a store the worker cannot open.
    with pytest.raises(QueryError) as info:
        run_query('SELECT ?problemID WHERE {\n  ?p ?q }', 10, db_path=db_path)
    assert info.value.kind == 'syntax' and info.value.line is not None

    with pytest.raises(QueryError) as info:
        run_query('SELECT ?problemID WHERE {}', 10, db_path=db_path + '-missing')
    assert info.value.kind == 'failed' and info.value.message


def test_run_query_checks_before_running(db_path):
    with pytest.raises(QueryError) as info:
        run_query('SELECT ?x WHERE { SERVICE <http://127.0.0.1:9/> { ?x ?p ?o } }', 10,
                  db_path=db_path)
    assert info.value.kind == 'service'


def test_run_query_timeout(db_path):
    endless = '''SELECT ?problemID WHERE {
  ?a ?b ?c . ?d ?e ?f . ?g ?h ?i . ?j ?k ?l . ?m ?n ?o .
  BIND (STR(?c) AS ?problemID)
} ORDER BY ?a ?d ?g ?j ?m'''
    with pytest.raises(QueryError) as info:
        run_query(endless, 10, db_path=db_path, timeout=1)
    assert info.value.kind == 'timeout'


# --- presets and page ------------------------------------------------------

def _preset_queries():
    from blueprints.advanced_search import load_presets
    menu, queries = load_presets('lv')
    return menu, queries


def test_presets_are_valid_select_queries(store):
    menu, queries = _preset_queries()
    assert menu and queries
    for query in queries:
        check_query(query)
        collect_rows(store, query, MAX_LIMIT)  # parses; raises on syntax errors


def test_presets_menu_structure_and_titles(tmp_path):
    from blueprints.advanced_search import load_presets
    (tmp_path / '20_b.yaml').write_text('''
title: {lv: "Bē", en: "B"}
items:
  - title: {en: "Only English"}
    items:
      - title: "Plain"
        query: "SELECT ?problemID WHERE {}"
  - title: "No query"
''', encoding='utf-8')
    (tmp_path / '10_a.yaml').write_text('title: "A"\nitems:\n  - title: X\n    query: "SELECT 1"\n',
                                        encoding='utf-8')
    (tmp_path / '30_broken.yaml').write_text('title: [unclosed', encoding='utf-8')
    menu, queries = load_presets('en', presets_dir=str(tmp_path))
    assert menu == [
        {'title': 'A', 'children': [{'title': 'X', 'index': 0}]},
        {'title': 'B', 'children': [{'title': 'Only English',
                                  'children': [{'title': 'Plain', 'index': 1}]}]},
    ]
    assert queries == ['SELECT 1', 'SELECT ?problemID WHERE {}']
    assert load_presets('lt', presets_dir=str(tmp_path))[0][1]['title'] == 'Bē'


@pytest.fixture
def client(db_path, monkeypatch):
    import eliozo
    import eliozo_dao
    monkeypatch.setattr(eliozo_dao, 'OXIGRAPH_DB_PATH', db_path)
    app = eliozo.create_app({'TESTING': True})
    return app.test_client()


def test_page_shows_form_and_presets(client):
    html = client.get('/advanced_search').get_data(as_text=True)
    assert 'name="query"' in html and 'name="limit"' in html and 'value="20"' in html
    assert 'preset-query' in html and 'dropdown-submenu' in html


def test_page_runs_query_and_keeps_input(client):
    query = PREFIX + '''SELECT ?problemID (?grade AS ?section) WHERE {
  ?p eliozo:problemID ?problemID ; eliozo:problemGrade ?grade } ORDER BY ?grade ?problemID'''
    html = client.post('/advanced_search', data={'query': query, 'limit': '3'}).get_data(as_text=True)
    assert '<h3>5</h3>' in html and '<h3>6</h3>' in html
    assert 'problemid=LV.AMO.2011.5.1' in html and 'problemid=LV.AMO.2011.6.2' not in html
    assert 'value="3"' in html
    assert 'eliozo:problemGrade ?grade } ORDER BY' in html  # the query is still in the textarea


def test_page_reports_syntax_error_and_bad_limit(client):
    html = client.post('/advanced_search', data={'query': 'SELECT ?problemID WHERE {\n  ?p ?q }',
                                                 'limit': '20'}).get_data(as_text=True)
    assert 'alert-server-error' in html and 'sparql-error-line' in html
    html = client.post('/advanced_search', data={'query': 'SELECT ?problemID WHERE {}',
                                                 'limit': 'many'}).get_data(as_text=True)
    assert 'value="many"' in html and 'alert-danger' in html
