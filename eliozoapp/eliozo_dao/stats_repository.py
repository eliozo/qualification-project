import requests
import platform
import json
from eliozo_dao import FUSEKI_URL

def getSPARQLProblemCounts():
    url = FUSEKI_URL
    query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

SELECT ?country ?code ?olympiadName (COUNT(DISTINCT ?problem) AS ?ProblemCount)
WHERE {
  ?olympiad eliozo:olympiadName ?olympiadName ;
            eliozo:olympiadDescription ?olympiadDescription ;
            eliozo:olympiadCountry ?country ;
            eliozo:olympiadCode ?code .
  ?problem rdf:type eliozo:Problem ;
           eliozo:country ?country ;
           eliozo:olympiadCode ?code .
  FILTER (lang(?olympiadName) = "lv")
            FILTER (lang(?olympiadDescription) = "lv")
}
GROUP BY ?country ?code ?olympiadName"""
    myobj = {'query': query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLProblemSolvedCounts():
    url = FUSEKI_URL
    query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT ?country ?code ?olympiadName (COUNT(DISTINCT ?problem) AS ?ProblemCount)
    WHERE {
    ?olympiad eliozo:olympiadName ?olympiadName ;
                eliozo:olympiadDescription ?olympiadDescription ;
                eliozo:olympiadCountry ?country ;
                eliozo:olympiadCode ?code .
    ?problem rdf:type eliozo:Problem ;
            eliozo:problemSolution ?soln ;
            eliozo:country ?country ;
            eliozo:olympiadCode ?code .
    FILTER (lang(?olympiadName) = "lv")
                FILTER (lang(?olympiadDescription) = "lv")
    }
    GROUP BY ?country ?code ?olympiadName"""
    myobj = {'query': query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text 


def getSPARQLPropertyCount(arg):
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT ?sourceType (COUNT(DISTINCT ?problem) AS ?ProblemCount)
    WHERE {{
    ?problem rdf:type eliozo:Problem ;
            {propertyClause}
            eliozo:olympiadType ?sourceType .
    }}
    GROUP BY ?sourceType"""
    if arg == 'total':
        actual_query = queryTemplate.format(propertyClause='')
    else:
        actual_query = queryTemplate.format(propertyClause=f'eliozo:{arg} ?dummy ; ')
    myobj = {'query': actual_query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLActualValueCount(arg):
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT (COUNT(DISTINCT ?tt) AS ?ValueCount)
    WHERE {{
    ?problem rdf:type eliozo:Problem ;
            eliozo:{propertyName} ?tt .
    }}"""
    actual_query = queryTemplate.format(propertyName=arg)
    myobj = {'query': actual_query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLMaxValueCount(arg): 
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT (COUNT(DISTINCT ?vv) AS ?MaxCount)
    WHERE {{
    ?vv rdf:type eliozo:{propType} .
    }}
    """
    
    if arg == 'questionType':
        propType = 'Question'
    elif arg == 'method':
        propType = 'Method'
    elif arg == 'topic':
        propType = 'Topic'
    elif arg == 'subdomain': 
        propType = 'Domain'
    elif arg == 'concepts':
        propType = 'Concept'
    elif arg == 'olympiad': 
        propType = 'Olympiad'
    else:
        propType = 'Question'

    actual_query = queryTemplate.format(propType=propType)
    myobj = {'query': actual_query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text
