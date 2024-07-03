import rdflib
from rdflib.namespace import Namespace
import pytest

g = rdflib.Graph()
ELIOZO = Namespace("http://www.dudajevagatve.lv/eliozo#")

def contains_triple(graph, subject, predicate, object):
    s = subject if isinstance(subject, rdflib.term.Identifier) else rdflib.URIRef(subject)
    p = predicate if isinstance(predicate, rdflib.term.Identifier) else rdflib.URIRef(predicate)
    o = object if isinstance(object, rdflib.term.Identifier) else rdflib.Literal(object)
    return (s, p, o) in graph

@pytest.fixture
def setup_graph():
    graph = rdflib.Graph()
    """Fixture to setup the graph with necessary namespaces and triples."""
    graph.bind("eliozo", ELIOZO) # Binding the namespace prefix for use in the graph
    graph.add((ELIOZO.EE_PK_1994_7_2, ELIOZO.country, rdflib.Literal("EE")))
    yield graph

def test_dummy(setup_graph):
    subject = ELIOZO.EE_PK_1994_7_2
    predicate = ELIOZO.country
    object = rdflib.Literal("EE")
    assert contains_triple(setup_graph, subject, predicate, object)


