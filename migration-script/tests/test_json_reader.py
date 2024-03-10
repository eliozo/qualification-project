from json_reader import f
import rdflib
from rdflib.namespace import Namespace
import pytest

g = rdflib.Graph()
ELIOZO = Namespace("http://www.dudajevagatve.lv/eliozo#")

# Function to check if a specific triple exists
def contains_triple(graph, subject, predicate, object):
    s = subject if isinstance(subject, rdflib.term.Identifier) else rdflib.URIRef(subject)
    p = predicate if isinstance(predicate, rdflib.term.Identifier) else rdflib.URIRef(predicate)
    o = object if isinstance(object, rdflib.term.Identifier) else rdflib.Literal(object)
    return (s, p, o) in graph

# def test_f_returns_17():
#     f = open('test_lists.md')
#
#     data = json.load(f)  # Atgriež JSON objektu kā vārdnīcu
#     g = produceRDF(data)
#
#     assert f() == 17


@pytest.fixture
def setup_graph():
    """Fixture to setup the graph with necessary namespaces and triples."""
    g.bind("eliozo", ELIOZO) # Binding the namespace prefix for use in the graph

    # Add the triple to the graph
    # This is only for demonstration; in a real case, the graph 'g' would already have this triple or others
    g.add((ELIOZO.EE_PK_1994_7_2, ELIOZO.country, rdflib.Literal("EE")))



def test_graph_contains_triple(setup_graph):
    subject = ELIOZO.LV.AO.2000.8.3
    predicate = ELIOZO.country
    object = "LV"
    assert contains_triple(setup_graph, subject, predicate, object)

