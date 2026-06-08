from eliozo_dao import sparql_query


def getSPARQLtopics():
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
    return sparql_query(queryTemplate)


def getSPARQLconcepts():
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
    return sparql_query(queryTemplate)


def getSPARQLmethods():
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
    return sparql_query(queryTemplate)


def getSPARQLdomains():
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
    return sparql_query(queryTemplate)


def getTopicProblemsSPARQL(topicID):
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
    return sparql_query(queryTemplate.format(topic=topicID))


def getTopicDetails(topicID):
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
    return sparql_query(queryTemplate.format(topic=topicID))


def getAllTopicChildren(topicID):
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
    return sparql_query(queryTemplate.format(topic=topicID))


def getAllTopicsTableSPARQL():
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
    return sparql_query(query)


def getWizardTopicsSPARQL():
    query = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?topicIdentifier ?topicNumber ?topicDescription ?topicName ?L1 ?L2 WHERE {
    ?topic eliozo:topicID ?topicIdentifier .
    ?topic eliozo:topicNumber ?topicNumber .
    ?topic eliozo:topicDescription ?topicDescription .
    ?topic eliozo:topicName ?topicName .
    ?topic eliozo:sorter_L1 ?L1 ;
            eliozo:sorter_L2 ?L2 ;
            eliozo:sorter_L3 ?L3 ;
            eliozo:sorter_L4 ?L4 ;
            eliozo:sorter_L5 ?L5 .
    FILTER (?L3 = 0 && ?L4 = 0 && ?L5 = 0)
    } ORDER BY ?L1 ?L2
    """
    return sparql_query(query)
