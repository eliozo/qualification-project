"""SPARQL 1.1 Service Description and VoID description of the store.

* Service Description (https://www.w3.org/TR/sparql11-service-description/)
  is returned for ``GET /sparql`` without a ``query`` parameter. It names
  the supported result formats and points to the VoID dataset.
* VoID (https://www.w3.org/TR/void/) at ``/sparql/void`` gives the size of
  the data, its classes and properties with counts. It is computed with a
  few aggregate queries the first time it is asked for after the store was
  (re)opened, then cached until the next reload.
"""

from pyoxigraph import BlankNode, Literal, NamedNode, Triple

SD = 'http://www.w3.org/ns/sparql-service-description#'
VOID = 'http://rdfs.org/ns/void#'
FORMATS = 'http://www.w3.org/ns/formats/'
RDF_TYPE = NamedNode('http://www.w3.org/1999/02/22-rdf-syntax-ns#type')
DCT = 'http://purl.org/dc/terms/'
XSD = 'http://www.w3.org/2001/XMLSchema#'

DESCRIPTION_PREFIXES = {
    'sd': SD, 'void': VOID, 'formats': FORMATS, 'dcterms': DCT, 'xsd': XSD,
    'rdf': 'http://www.w3.org/1999/02/22-rdf-syntax-ns#',
}

RESULT_FORMAT_IRIS = ['SPARQL_Results_JSON', 'SPARQL_Results_XML', 'SPARQL_Results_CSV',
                      'SPARQL_Results_TSV', 'Turtle', 'N-Triples', 'RDF_XML', 'JSON-LD']


def _n(prefix, name):
    return NamedNode(prefix + name)


def _int(value):
    return Literal(str(int(value)), datatype=NamedNode(XSD + 'integer'))


def service_description(endpoint_url, settings, triple_count=None):
    """Triples of the Service Description; ``endpoint_url`` is the public URL."""
    svc = NamedNode(endpoint_url)
    dataset = NamedNode(endpoint_url + '/void#dataset')
    graph = BlankNode()
    t = [
        Triple(svc, RDF_TYPE, _n(SD, 'Service')),
        Triple(svc, _n(SD, 'endpoint'), svc),
        Triple(svc, _n(SD, 'supportedLanguage'), _n(SD, 'SPARQL11Query')),
        Triple(svc, _n(DCT, 'title'), Literal('Eliozo SPARQL endpoint (read-only)')),
        Triple(svc, _n(DCT, 'description'), Literal(
            'Read-only SPARQL 1.1 Protocol endpoint for the Eliozo math olympiad problem '
            f'data. Limits: queries up to {settings.max_query_length} characters, '
            f'{settings.max_rows} result rows, {settings.max_triples} triples, '
            f'{int(settings.query_timeout)} s per query. SERVICE and updates are refused.')),
        Triple(svc, _n(SD, 'defaultDataset'), dataset),
        Triple(dataset, RDF_TYPE, _n(SD, 'Dataset')),
        Triple(dataset, RDF_TYPE, _n(VOID, 'Dataset')),
        Triple(dataset, _n(SD, 'defaultGraph'), graph),
        Triple(graph, RDF_TYPE, _n(SD, 'Graph')),
    ]
    t += [Triple(svc, _n(SD, 'resultFormat'), _n(FORMATS, f)) for f in RESULT_FORMAT_IRIS]
    if triple_count is not None:
        t.append(Triple(graph, _n(VOID, 'triples'), _int(triple_count)))
    return t


_CLASS_QUERY = 'SELECT ?c (COUNT(DISTINCT ?s) AS ?n) WHERE { ?s a ?c } GROUP BY ?c ORDER BY ?c'
_PROPERTY_QUERY = '''SELECT ?p (COUNT(*) AS ?n) (COUNT(DISTINCT ?s) AS ?ds) (COUNT(DISTINCT ?o) AS ?do)
WHERE { ?s ?p ?o } GROUP BY ?p ORDER BY ?p'''
_TOTALS_QUERY = '''SELECT (COUNT(*) AS ?n) (COUNT(DISTINCT ?s) AS ?ds) (COUNT(DISTINCT ?o) AS ?do)
WHERE { ?s ?p ?o }'''
_GRAPH_QUERY = 'SELECT ?g (COUNT(*) AS ?n) WHERE { GRAPH ?g { ?s ?p ?o } } GROUP BY ?g ORDER BY ?g'


def _value(term):
    return int(term.value) if term is not None else 0


def void_description(store, endpoint_url, settings, modified=None):
    """Triples of the VoID description of the store's default graph."""
    ds = NamedNode(endpoint_url + '/void#dataset')
    t = [
        Triple(ds, RDF_TYPE, _n(VOID, 'Dataset')),
        Triple(ds, _n(DCT, 'title'), Literal('Eliozo math olympiad problems')),
        Triple(ds, _n(VOID, 'sparqlEndpoint'), NamedNode(endpoint_url)),
        Triple(ds, _n(VOID, 'uriSpace'), Literal(settings.void_uri_space)),
    ]
    for f in ('Turtle', 'N-Triples', 'RDF_XML', 'JSON-LD'):
        t.append(Triple(ds, _n(VOID, 'feature'), _n(FORMATS, f)))
    if modified:
        t.append(Triple(ds, _n(DCT, 'modified'), Literal(
            modified, datatype=NamedNode(XSD + 'dateTime'))))

    totals = next(iter(store.query(_TOTALS_QUERY)))
    t += [Triple(ds, _n(VOID, 'triples'), _int(_value(totals['n']))),
          Triple(ds, _n(VOID, 'distinctSubjects'), _int(_value(totals['ds']))),
          Triple(ds, _n(VOID, 'distinctObjects'), _int(_value(totals['do'])))]

    classes = list(store.query(_CLASS_QUERY))
    t.append(Triple(ds, _n(VOID, 'classes'), _int(len(classes))))
    for row in classes:
        part = BlankNode()
        t += [Triple(ds, _n(VOID, 'classPartition'), part),
              Triple(part, _n(VOID, 'class'), row['c']),
              Triple(part, _n(VOID, 'entities'), _int(_value(row['n'])))]

    properties = list(store.query(_PROPERTY_QUERY))
    t.append(Triple(ds, _n(VOID, 'properties'), _int(len(properties))))
    for row in properties:
        part = BlankNode()
        t += [Triple(ds, _n(VOID, 'propertyPartition'), part),
              Triple(part, _n(VOID, 'property'), row['p']),
              Triple(part, _n(VOID, 'triples'), _int(_value(row['n']))),
              Triple(part, _n(VOID, 'distinctSubjects'), _int(_value(row['ds']))),
              Triple(part, _n(VOID, 'distinctObjects'), _int(_value(row['do'])))]

    for row in store.query(_GRAPH_QUERY):
        sub = BlankNode()
        t += [Triple(ds, _n(VOID, 'subset'), sub),
              Triple(sub, RDF_TYPE, _n(VOID, 'Dataset')),
              Triple(sub, _n(SD, 'name'), row['g']),
              Triple(sub, _n(VOID, 'triples'), _int(_value(row['n'])))]
    return t
