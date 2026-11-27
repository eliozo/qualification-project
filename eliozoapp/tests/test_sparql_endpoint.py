"""Tests for the read-only SPARQL endpoint (``sparql_endpoint``).

The application runs against an on-disk copy of the TTL fixture of
``tests/conftest.py`` (plus one named graph), opened read-only exactly as on
the server, and is called through Werkzeug's WSGI test client.
"""

import json
import os
import shutil
import subprocess
import sys
import textwrap
import time
import xml.etree.ElementTree as ET

import pytest
from pyoxigraph import Literal, NamedNode, Quad, RdfFormat, Store
from werkzeug.test import Client

from conftest import FIXTURE_TTL
from sparql_endpoint import results
from sparql_endpoint.app import SparqlApplication
from sparql_endpoint.config import Settings
from sparql_endpoint.protocol import negotiate, parse_accept, prefers_html, RESULT_FORMATS
from sparql_endpoint.store import StoreHolder, fingerprint, writer_active

PREFIX = 'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\n'
GRAPH = 'http://example.org/graph/extra'
COUNT_OLYMPIADS = PREFIX + 'SELECT (COUNT(*) AS ?n) WHERE { ?o a eliozo:Olympiad }'
JSON_RESULTS = 'application/sparql-results+json'


def build_store(path, extra=0):
    store = Store(path)
    store.load(input=FIXTURE_TTL, format=RdfFormat.TURTLE)
    store.add(Quad(NamedNode('http://example.org/s'), NamedNode('http://example.org/p'),
                   Literal('in a named graph'), NamedNode(GRAPH)))
    for i in range(extra):
        store.add(Quad(NamedNode(f'http://example.org/x{i}'),
                       NamedNode('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'),
                       NamedNode('http://www.dudajevagatve.lv/eliozo#Olympiad')))
    store.flush()
    del store


@pytest.fixture
def store_path(tmp_path):
    path = str(tmp_path / 'store')
    build_store(path)
    return path


def make_client(store_path, clock=None, **overrides):
    settings = Settings(store_path=store_path, public_url='https://example.org/sparql',
                        **overrides)
    app = SparqlApplication(settings, clock=clock) if clock else SparqlApplication(settings)
    return Client(app), app


@pytest.fixture
def client(store_path):
    return make_client(store_path)[0]


def select_json(response):
    assert response.status_code == 200, response.get_data(as_text=True)
    return json.loads(response.get_data(as_text=True))


# --- the three ways to send a query -------------------------------------------

def test_get_query_returns_json_by_default(client):
    r = client.get('/sparql', query_string={'query': COUNT_OLYMPIADS})
    assert r.headers['Content-Type'].startswith(JSON_RESULTS)
    assert select_json(r)['results']['bindings'][0]['n']['value'] == '2'


def test_post_form(client):
    r = client.post('/sparql', data={'query': COUNT_OLYMPIADS})
    assert select_json(r)['results']['bindings'][0]['n']['value'] == '2'


def test_post_sparql_query_body(client):
    r = client.post('/sparql', data=COUNT_OLYMPIADS.encode('utf-8'),
                    content_type='application/sparql-query; charset=utf-8')
    assert select_json(r)['head']['vars'] == ['n']


def test_post_other_content_type_is_415(client):
    r = client.post('/sparql', data=COUNT_OLYMPIADS, content_type='text/plain')
    assert r.status_code == 415


def test_post_without_query_is_400(client):
    assert client.post('/sparql', data={'foo': 'bar'}).status_code == 400


def test_query_given_twice_is_400(client):
    r = client.get('/sparql?query=ASK%7B%7D&query=ASK%7B%7D')
    assert r.status_code == 400


# --- response formats ---------------------------------------------------------

@pytest.mark.parametrize('accept,media', [
    ('application/sparql-results+xml', 'application/sparql-results+xml'),
    ('text/csv', 'text/csv'),
    ('text/tab-separated-values', 'text/tab-separated-values'),
    ('application/json', JSON_RESULTS),
    ('text/csv;q=0.5, application/sparql-results+xml', 'application/sparql-results+xml'),
    ('*/*', JSON_RESULTS),
])
def test_select_formats_by_accept(client, accept, media):
    r = client.get('/sparql', query_string={'query': COUNT_OLYMPIADS},
                   headers={'Accept': accept})
    assert r.status_code == 200
    assert r.headers['Content-Type'].split(';')[0] == media


def test_select_xml_csv_tsv_content(client):
    q = PREFIX + 'SELECT ?code ?name WHERE { ?o eliozo:olympiadCode ?code ; ' \
                 'eliozo:olympiadName ?name } ORDER BY ?code'
    xml = client.get('/sparql', query_string={'query': q},
                     headers={'Accept': 'application/sparql-results+xml'}).get_data()
    ns = {'s': 'http://www.w3.org/2005/sparql-results#'}
    root = ET.fromstring(xml)
    literals = root.findall('.//s:binding[@name="name"]/s:literal', ns)
    assert literals[0].text == 'Atklātā matemātikas olimpiāde'
    assert literals[0].get('{http://www.w3.org/XML/1998/namespace}lang') == 'lv'

    csv_text = client.get('/sparql', query_string={'query': q},
                          headers={'Accept': 'text/csv'}).get_data(as_text=True)
    assert csv_text.split('\r\n')[:2] == ['code,name', 'AMO,Atklātā matemātikas olimpiāde']

    tsv_text = client.get('/sparql', query_string={'query': q},
                          headers={'Accept': 'text/tab-separated-values'}).get_data(as_text=True)
    assert tsv_text.splitlines()[:2] == ['?code\t?name',
                                         '"AMO"\t"Atklātā matemātikas olimpiāde"@lv']


def test_format_parameter_overrides_accept(client):
    r = client.get('/sparql', query_string={'query': COUNT_OLYMPIADS, 'format': 'csv'},
                   headers={'Accept': JSON_RESULTS})
    assert r.headers['Content-Type'].startswith('text/csv')


def test_unacceptable_format_is_406(client):
    r = client.get('/sparql', query_string={'query': COUNT_OLYMPIADS},
                   headers={'Accept': 'image/png'})
    assert r.status_code == 406


@pytest.mark.parametrize('accept,expected', [
    (JSON_RESULTS, '{"head":{},"boolean":true}'),
    ('application/sparql-results+xml', '<boolean>true</boolean>'),
    ('text/csv', '_askResult\ntrue'),
])
def test_ask(client, accept, expected):
    r = client.get('/sparql', query_string={'query': PREFIX + 'ASK { ?o a eliozo:Olympiad }'},
                   headers={'Accept': accept})
    assert r.status_code == 200
    assert expected in r.get_data(as_text=True)


@pytest.mark.parametrize('accept,media,marker', [
    ('text/turtle', 'text/turtle', 'eliozo:LV.AMO'),
    ('application/n-triples', 'application/n-triples', '<http://www.dudajevagatve.lv/eliozo#LV.AMO>'),
    ('application/rdf+xml', 'application/rdf+xml', 'rdf:RDF'),
    ('application/ld+json', 'application/ld+json', '"@id"'),
    (None, 'text/turtle', '@prefix'),
])
def test_construct_formats(client, accept, media, marker):
    q = PREFIX + 'CONSTRUCT { ?o eliozo:olympiadCode ?c } WHERE { ?o eliozo:olympiadCode ?c }'
    headers = {'Accept': accept} if accept else {}
    r = client.get('/sparql', query_string={'query': q}, headers=headers)
    assert r.status_code == 200
    assert r.headers['Content-Type'].split(';')[0] == media
    assert marker in r.get_data(as_text=True)


def test_describe(client):
    r = client.get('/sparql', query_string={'query': PREFIX + 'DESCRIBE eliozo:LV.AMO'},
                   headers={'Accept': 'application/n-triples'})
    assert r.status_code == 200
    assert 'olympiadCode' in r.get_data(as_text=True)


# --- dataset parameters -------------------------------------------------------

def test_default_graph_uri(client):
    q = 'SELECT ?o WHERE { ?s ?p ?o }'
    r = client.get('/sparql', query_string={'query': q, 'default-graph-uri': GRAPH})
    bindings = select_json(r)['results']['bindings']
    assert [b['o']['value'] for b in bindings] == ['in a named graph']


def test_named_graph_uri(client):
    q = 'SELECT ?g WHERE { GRAPH ?g { ?s ?p ?o } }'
    r = client.get('/sparql', query_string={'query': q, 'named-graph-uri': GRAPH})
    assert [b['g']['value'] for b in select_json(r)['results']['bindings']] == [GRAPH]
    r = client.get('/sparql', query_string={'query': q,
                                            'named-graph-uri': 'http://example.org/none'})
    assert select_json(r)['results']['bindings'] == []


def test_invalid_graph_iri_is_400(client):
    r = client.get('/sparql', query_string={'query': 'ASK {}', 'default-graph-uri': 'not an iri'})
    assert r.status_code == 400


# --- refused queries and limits -----------------------------------------------

@pytest.mark.parametrize('kwargs', [
    {'query_string': {'update': 'INSERT DATA { <a:b> <a:c> <a:d> }'}},
    {'data': {'update': 'INSERT DATA { <a:b> <a:c> <a:d> }'}},
    {'data': 'INSERT DATA { <a:b> <a:c> <a:d> }', 'content_type': 'application/sparql-update'},
    {'query_string': {'query': 'INSERT DATA { <a:b> <a:c> <a:d> }'}},
    {'query_string': {'query': 'DROP ALL'}},
])
def test_updates_are_refused(client, kwargs):
    method = client.post if 'data' in kwargs else client.get
    r = method('/sparql', **kwargs)
    assert r.status_code == 400
    assert 'read-only' in r.get_data(as_text=True)


@pytest.mark.parametrize('query', [
    'SELECT * WHERE { SERVICE <http://127.0.0.1:9/sparql> { ?s ?p ?o } }',
    'select * where { service silent <http://example.org/sparql> { ?s ?p ?o } }',
    'SELECT * WHERE { SERVICE ?endpoint { ?s ?p ?o } VALUES ?endpoint { <http://x> } }',
])
def test_service_is_refused(client, query):
    r = client.get('/sparql', query_string={'query': query})
    assert r.status_code == 400
    assert 'SERVICE' in r.get_data(as_text=True)


def test_service_in_a_string_or_comment_is_fine(client):
    q = 'SELECT ?x WHERE { BIND("SERVICE" AS ?x) } # SERVICE'
    assert client.get('/sparql', query_string={'query': q}).status_code == 200


def test_syntax_error_is_400(client):
    r = client.get('/sparql', query_string={'query': 'SELECT * WHERE { ?s ?p }'})
    assert r.status_code == 400
    assert 'syntax' in r.get_data(as_text=True).lower()


def test_query_too_long_is_413(store_path):
    client, _ = make_client(store_path, max_query_length=50)
    r = client.get('/sparql', query_string={'query': 'SELECT * WHERE { ?s ?p ?o } # ' + 'x' * 50})
    assert r.status_code == 413


def test_body_too_large_is_413(store_path):
    client, _ = make_client(store_path, max_request_bytes=100)
    r = client.post('/sparql', data={'query': 'ASK {} #' + 'x' * 200})
    assert r.status_code == 413


def test_rows_are_truncated_with_header(store_path):
    client, _ = make_client(store_path, max_rows=3)
    r = client.get('/sparql', query_string={'query': 'SELECT * WHERE { ?s ?p ?o }'})
    assert len(select_json(r)['results']['bindings']) == 3
    assert r.headers['X-SPARQL-Truncated'] == 'true'
    assert r.headers['X-SPARQL-Limit'] == '3'
    r = client.get('/sparql', query_string={'query': COUNT_OLYMPIADS})
    assert 'X-SPARQL-Truncated' not in r.headers


def test_construct_is_truncated_too(store_path):
    client, _ = make_client(store_path, max_triples=2)
    r = client.get('/sparql', query_string={'query': 'CONSTRUCT WHERE { ?s ?p ?o }'},
                   headers={'Accept': 'application/n-triples'})
    assert r.headers['X-SPARQL-Truncated'] == 'true'
    assert len(r.get_data(as_text=True).strip().splitlines()) == 2


def test_soft_timeout_is_503(store_path):
    ticks = iter(range(0, 10_000, 100))     # every clock call is 100 s later
    client, _ = make_client(store_path, clock=lambda: next(ticks), query_timeout=20)
    r = client.get('/sparql', query_string={'query': 'SELECT * WHERE { ?s ?p ?o }'})
    assert r.status_code == 503
    assert 'took longer' in r.get_data(as_text=True)


# --- descriptions, graph store, health, CORS ----------------------------------

def test_service_description(client):
    r = client.get('/sparql', headers={'Accept': 'text/turtle'})
    text = r.get_data(as_text=True)
    assert r.status_code == 200 and r.headers['Content-Type'].startswith('text/turtle')
    assert '<https://example.org/sparql> a sd:Service' in text
    assert 'formats:SPARQL_Results_JSON' in text
    assert 'sd:SPARQL11Query' in text
    assert 'BasicFederatedQuery' not in text


def test_browser_gets_help_page(client):
    r = client.get('/sparql', headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'})
    assert r.headers['Content-Type'].startswith('text/html')
    assert 'read-only' in r.get_data(as_text=True)


def test_void(client):
    r = client.get('/sparql/void', headers={'Accept': 'application/n-triples'})
    text = r.get_data(as_text=True)
    assert r.status_code == 200
    assert '<http://rdfs.org/ns/void#classPartition>' in text
    assert '<http://www.dudajevagatve.lv/eliozo#Olympiad>' in text
    assert '<http://rdfs.org/ns/void#sparqlEndpoint> <https://example.org/sparql>' in text
    assert f'<http://www.w3.org/ns/sparql-service-description#name> <{GRAPH}>' in text


def test_graph_store_get(client):
    r = client.get('/sparql/graph', query_string={'graph': GRAPH},
                   headers={'Accept': 'application/n-triples'})
    assert r.get_data(as_text=True).strip() == \
        '<http://example.org/s> <http://example.org/p> "in a named graph" .'
    assert client.get('/sparql/graph?default').status_code == 200
    assert client.get('/sparql/graph', query_string={'graph': 'http://x/none'}).status_code == 404
    assert client.get('/sparql/graph').status_code == 400
    assert client.put('/sparql/graph?default', data='x').status_code == 405


def test_health(client):
    r = client.get('/sparql/health')
    body = json.loads(r.get_data(as_text=True))
    assert r.status_code == 200 and body['status'] == 'ok' and body['triples'] > 10


def test_health_without_store_is_503(tmp_path):
    client, _ = make_client(str(tmp_path / 'missing'))
    assert client.get('/sparql/health').status_code == 503
    assert client.get('/sparql', query_string={'query': 'ASK {}'}).status_code == 503


def test_cors(client):
    r = client.get('/sparql', query_string={'query': 'ASK {}'})
    assert r.headers['Access-Control-Allow-Origin'] == '*'
    r = client.options('/sparql', headers={'Origin': 'https://yasgui.example',
                                           'Access-Control-Request-Method': 'POST',
                                           'Access-Control-Request-Headers': 'content-type'})
    assert r.status_code == 204
    assert 'POST' in r.headers['Access-Control-Allow-Methods']
    assert r.headers['Access-Control-Allow-Headers'] == 'content-type'
    assert client.get('/sparql', query_string={'query': 'bad'}) \
        .headers['Access-Control-Allow-Origin'] == '*'


def test_unknown_path_and_method(client):
    assert client.get('/sparql/nothing').status_code == 404
    assert client.delete('/sparql').status_code == 405


def test_head(client):
    r = client.head('/sparql/health')
    assert r.status_code == 200 and r.get_data() == b''


# --- following a reload of the store ------------------------------------------

class FakeClock:
    """Monotonic clock for the check interval; ``wall`` is real time plus ``offset``."""

    def __init__(self):
        self.now = 0.0
        self.offset = 0.0

    def __call__(self):
        return self.now

    def wall(self):
        return time.time() + self.offset


def count(store):
    return int(next(iter(store.query(COUNT_OLYMPIADS)))['n'].value)


def test_holder_reopens_a_rebuilt_store_after_it_settles(store_path):
    clock = FakeClock()
    holder = StoreHolder(store_path, check_interval=2, settle=5, clock=clock,
                         wallclock=clock.wall)
    assert count(holder.get()) == 2

    shutil.rmtree(store_path)               # load_rdf: drop ...
    clock.now = 3
    assert count(holder.get()) == 2         # old data while the store is missing
    build_store(store_path, extra=3)        # ... and rebuild
    clock.now = 6
    assert count(holder.get()) == 2         # just written: not settled yet
    clock.now = 7
    clock.offset = 10                       # 10 s later, no writes since
    assert count(holder.get()) == 2         # within the check interval: not checked
    clock.now = 8
    assert count(holder.get()) == 5         # reopened
    assert holder.generation == 2
    clock.now = 20
    assert count(holder.get()) == 5 and holder.generation == 2


def test_holder_waits_while_a_writer_holds_the_store(store_path):
    if not sys.platform.startswith('linux'):
        pytest.skip('the writer-lock probe is Linux-only')
    clock = FakeClock()
    holder = StoreHolder(store_path, check_interval=1, settle=5, clock=clock,
                         wallclock=clock.wall)
    holder.get()
    script = textwrap.dedent(f'''
        import sys, pyoxigraph as ox
        s = ox.Store({store_path!r})
        s.add(ox.Quad(ox.NamedNode('http://e/x'), ox.NamedNode('http://www.w3.org/1999/02/22-rdf-syntax-ns#type'),
                      ox.NamedNode('http://www.dudajevagatve.lv/eliozo#Olympiad')))
        s.flush()
        print('ready', flush=True)
        sys.stdin.readline()
    ''')
    writer = subprocess.Popen([sys.executable, '-c', script], stdin=subprocess.PIPE,
                              stdout=subprocess.PIPE, text=True)
    try:
        assert writer.stdout.readline().strip() == 'ready'
        assert writer_active(store_path)
        clock.offset = 60                    # long settled, but the writer is still open
        for t in (2, 4, 6):
            clock.now = t
            assert count(holder.get()) == 2
    finally:
        writer.communicate('done\n', timeout=30)
    assert not writer_active(store_path)
    clock.now, clock.offset = 8, 120
    assert count(holder.get()) == 3


def test_fingerprint_of_missing_store(tmp_path):
    assert fingerprint(str(tmp_path / 'none')) is None


# --- serializers and negotiation ----------------------------------------------

def test_tsv_escapes_tabs_and_newlines():
    row = (Literal('a\tb\nc "d"'), Literal('5', datatype=NamedNode(
        'http://www.w3.org/2001/XMLSchema#integer')))
    out = results.select_tsv(['x', 'y'], [row]).decode()
    assert out == '?x\t?y\n"a\\tb\\nc \\"d\\""\t"5"^^<http://www.w3.org/2001/XMLSchema#integer>\n'


def test_csv_quotes_and_unbound():
    out = results.select_csv(['x', 'y'], [(Literal('a,"b"'), None)]).decode()
    assert out == 'x,y\r\n"a,""b""",\r\n'


def test_json_literal_forms():
    xsd = 'http://www.w3.org/2001/XMLSchema#'
    assert results.json_term(Literal('a')) == {'type': 'literal', 'value': 'a'}
    assert results.json_term(Literal('a', language='lv')) == \
        {'type': 'literal', 'value': 'a', 'xml:lang': 'lv'}
    assert results.json_term(Literal('1', datatype=NamedNode(xsd + 'integer')))['datatype'] \
        == xsd + 'integer'


def test_negotiation_helpers():
    assert parse_accept('text/csv;q=0.2, */*;q=0.1') == [('text/csv', 0.2), ('*/*', 0.1)]
    assert negotiate(RESULT_FORMATS, 'text/*') == ('csv', 'text/csv')
    assert negotiate(RESULT_FORMATS, None) == ('json', JSON_RESULTS)
    assert negotiate(RESULT_FORMATS, 'application/sparql-results+json;q=0') is None
    assert prefers_html('text/html') and not prefers_html('text/turtle') \
        and not prefers_html('*/*')
