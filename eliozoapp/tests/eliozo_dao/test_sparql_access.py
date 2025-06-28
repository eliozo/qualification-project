#from eliozo.dao.sparql_access import SparqlAccess
from eliozo_dao.sparql_access import SparqlAccess

def test_something():
    fuseki_url = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'
    sparql_access = SparqlAccess(fuseki_url)
    hello_message = sparql_access.get_message()
    assert hello_message.startswith("Hello")

