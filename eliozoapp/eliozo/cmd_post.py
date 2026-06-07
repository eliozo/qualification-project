"""Ad-hoc SPARQL probe against the embedded oxigraph store.

Run with: ``python -m eliozo.cmd_post`` (with the project venv active).
"""

from eliozo_dao import sparql_query

QUERY = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT * WHERE { ?sub eliozo:skill ?obj . ?obj skos:prefLabel ?label . } LIMIT 10
"""

if __name__ == "__main__":
    print(sparql_query(QUERY))
