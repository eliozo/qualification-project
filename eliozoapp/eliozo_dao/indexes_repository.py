import requests
from eliozo_dao import FUSEKI_URL

# Integrācija ar Jena Fuseki serveri
def getSPARQLtopics():
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?topicIdentifier ?topicNumber ?topicDescription ?topicName ?problemid WHERE { 
    ?topic eliozo:topicID ?topicIdentifier .
    ?topic eliozo:topicNumber ?topicNumber .
    ?topic eliozo:topicDescription ?topicDescription .
    ?topic eliozo:topicName ?topicName .
    ?topic eliozo:sorter_L1 ?L1 ; 
            eliozo:sorter_L2 ?L2 ; 
            eliozo:sorter_L3 ?L3 ; 
            eliozo:sorter_L4 ?L4 ; 
            eliozo:sorter_L5 ?L5 .
    OPTIONAL {
        ?prob eliozo:topic ?topic ;
            eliozo:problemID ?problemid . 
    }.
    } ORDER BY ?L1 ?L2 ?L3 ?L4 ?L5
    """

    myobj = {'query': queryTemplate }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLconcepts():
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?concept ?termLV ?termEN ?conceptID ?descLV ?problemID WHERE {
  ?concept a eliozo:Concept ;
           eliozo:termLV ?termLV ; 
           eliozo:termEN ?termEN ;
           eliozo:conceptID ?conceptID .
  OPTIONAL {
    ?concept eliozo:descLV ?descLV .
  }
  ?problem eliozo:concepts ?concept ;
           eliozo:problemID ?problemID .
} ORDER BY ?termEN ?problemID
"""

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    myobj = {'query': queryTemplate}
    x = requests.post(url, myobj, head)
    return x.text



def getSPARQLmethods():
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

SELECT ?methodID ?methodNumber ?methodName ?methodDescription ?problemid ?L1 ?L2 WHERE {
  ?method a eliozo:Method ;
            eliozo:methodID ?methodID ;
            eliozo:methodNumber ?methodNumber ;
            eliozo:methodName ?methodName ;
            eliozo:methodDescription ?methodDescription ;
            eliozo:sorter_L1 ?L1 ;
            eliozo:sorter_L2 ?L2 .
  OPTIONAL {
    ?prob eliozo:method ?method ;
    eliozo:problemID ?problemid . 
  }
} ORDER BY ?L1 ?L2
"""
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    myobj = {'query': queryTemplate}
    x = requests.post(url, myobj, head)
    return x.text



def getSPARQLdomains():
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?domainID ?domainNumber ?domainName ?domainDescription ?problemid ?L1 ?L2 ?L3 WHERE {
  ?domain a eliozo:Domain ;
            eliozo:domainID ?domainID ;
            eliozo:domainNumber ?domainNumber ;
            eliozo:domainName ?domainName ;
            eliozo:domainDescription ?domainDescription ;
            eliozo:sorter_L1 ?L1 ;
            eliozo:sorter_L2 ?L2 ;
            eliozo:sorter_L3 ?L3 .
  OPTIONAL {
    ?prob eliozo:subdomain ?domain ;
    eliozo:problemID ?problemid . 
  }
} ORDER BY ?L1 ?L2 ?L3
"""
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    myobj = {'query': queryTemplate}
    x = requests.post(url, myobj, head)
    return x.text


def getTopicProblemsSPARQL(topicID):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problem ?problemid ?subtopic ?text ?grade
WHERE {{
    ?parent skos:prefLabel '{topic}' .
    ?parent skos:narrower* ?subtopic .
    ?problem eliozo:topic ?subtopic ;
             eliozo:problemID ?problemid ;
             eliozo:problemTextHtml ?text ;
             eliozo:problemGrade ?grade .
}} ORDER BY ?grade
"""

    myobj = {'query': queryTemplate.format(topic=topicID)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getTopicDetails(topicID):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?topicID ?topicNumber ?topicName ?topicDesc WHERE {{
  ?topic skos:prefLabel '{topic}' ;
      eliozo:topicNumber ?topicNumber ;
      eliozo:topicName ?topicName ;
      eliozo:topicDescription ?topicDesc .
}}
"""

    myobj = {'query': queryTemplate.format(topic=topicID)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getAllTopicChildren(topicID):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?topicID ?prefLabel ?num ?topicName WHERE {{
  ?parentTopic skos:prefLabel '{topic}' .
  ?topicID skos:broader ?parentTopic ;
      skos:prefLabel ?prefLabel ;
      eliozo:topicName ?topicName ;
      eliozo:topicNumber ?num .
}} ORDER BY ?num
"""
    myobj = {'query': queryTemplate.format(topic=topicID)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getAllTopicsTableSPARQL():
    url = FUSEKI_URL
    query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?topicIdentifier ?topicNumber ?topicDescription ?topicName ?L1 ?L2 ?L3 ?L4 ?L5 WHERE { 
    ?topic eliozo:topicID ?topicIdentifier .
    ?topic eliozo:topicNumber ?topicNumber .
    ?topic eliozo:topicDescription ?topicDescription .
    ?topic eliozo:topicName ?topicName .
    ?topic eliozo:sorter_L1 ?L1 ; 
            eliozo:sorter_L2 ?L2 ; 
            eliozo:sorter_L3 ?L3 ; 
            eliozo:sorter_L4 ?L4 ; 
            eliozo:sorter_L5 ?L5 .
    } ORDER BY ?L1 ?L2 ?L3 ?L4 ?L5"""
    myobj = {'query': query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text
