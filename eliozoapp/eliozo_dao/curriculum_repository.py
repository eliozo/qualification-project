import requests
import json
from . import FUSEKI_URL

def getSPARQLCurriculumQtypeStats(olympiad, grades, years): 
    url = FUSEKI_URL 
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT ?domain ?questionType (COUNT(DISTINCT ?problem) AS ?count)
    WHERE {{
        ?problem a eliozo:Problem ;
        eliozo:olympiad '{olympiadCode}' ;
        eliozo:problemGrade ?grade ;
        eliozo:problemYear ?year ;
        eliozo:domain ?domain ;
        eliozo:questionType ?questionType .
        FILTER (?grade <= {gradeMax} && ?grade >= {gradeMin})
        FILTER (?year <= {yearMax} && ?year >= {yearMin})
    }}
    GROUP BY ?domain ?questionType
    ORDER BY ?domain ?questionType
    """
    myobj = {'query': 
        queryTemplate.format(olympiadCode=olympiad, 
                             gradeMax = grades[1],
                             gradeMin = grades[0],
                             yearMax = years[1],
                             yearMin = years[0])
    }
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLOlympiadOverview(olympiad, grades, years):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemID ?topicID ?topicNumber ?topicName ?topicDescription ?L1 ?L2 ?L3 WHERE {{
  ?problem eliozo:topic ?topic ; 
           eliozo:problemID ?problemID ;
           eliozo:olympiad '{olympiadCode}' ;
           eliozo:problemGrade ?grade ;
           eliozo:problemYear ?year .
  FILTER (?grade <= {gradeMax} && ?grade >= {gradeMin})
  FILTER (?year <= {yearMax} && ?year >= {yearMin})
  ?topic a eliozo:Topic ;
            eliozo:topicID ?topicID ;
            eliozo:topicNumber ?topicNumber ;
            eliozo:topicName ?topicName ;
            eliozo:topicDescription ?topicDescription ;
            eliozo:sorter_L1 ?L1 ;
            eliozo:sorter_L2 ?L2 ;
            eliozo:sorter_L3 ?L3 ;
            eliozo:sorter_L4 ?L4 ;
            eliozo:sorter_L5 ?L5 .
}} ORDER BY ?L1 ?L2 ?L3 ?L4 ?L5
"""
    myobj = {'query': 
        queryTemplate.format(olympiadCode=olympiad, 
                             gradeMax = grades[1],
                             gradeMin = grades[0],
                             yearMax = years[1],
                             yearMin = years[0])
    }
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text



def getSPARQLCurriculumMethods(olympiad, grades, years): 
    url = FUSEKI_URL 
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID ?methodID ?methodNumber ?methodName ?methodDescription ?L1 ?L2 WHERE {{
    ?problem eliozo:method ?method ;
            eliozo:problemID ?problemID ;
            eliozo:olympiad '{olympiadCode}' ;
            eliozo:problemGrade ?grade ;
            eliozo:problemYear ?year .
    FILTER (?grade <= {gradeMax} && ?grade >= {gradeMin})
    FILTER (?year <= {yearMax} && ?year >= {yearMin})
    ?method a eliozo:Method ;
                eliozo:methodNumber ?methodNumber ; 
                eliozo:methodID ?methodID ;
                eliozo:methodName ?methodName ;
                eliozo:methodDescription ?methodDescription ;
                eliozo:sorter_L1 ?L1 ;
                eliozo:sorter_L2 ?L2 .
    }} ORDER BY ?L1 ?L2
    """
    myobj = {'query': 
        queryTemplate.format(olympiadCode=olympiad, 
                             gradeMax = grades[1],
                             gradeMin = grades[0],
                             yearMax = years[1],
                             yearMin = years[0])
    }
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLCurriculumSubdomains(olympiad, grades, years):
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID ?domainID ?domainName ?domainDescription ?L1 ?L2 ?L3 WHERE {{
      ?problem eliozo:subdomain ?domain ;
               eliozo:problemID ?problemID ;
               eliozo:olympiad '{olympiadCode}' ;
               eliozo:problemGrade ?grade ;
               eliozo:problemYear ?year .
      FILTER (?grade <= {gradeMax} && ?grade >= {gradeMin})
      FILTER (?year <= {yearMax} && ?year >= {yearMin})
      ?domain a eliozo:Domain ;
              eliozo:domainID ?domainID ;
              eliozo:domainName ?domainName ;
              eliozo:domainDescription ?domainDescription ;
              eliozo:sorter_L1 ?L1 ;
              eliozo:sorter_L2 ?L2 ;
              eliozo:sorter_L3 ?L3 .
    }} ORDER BY ?L1 ?L2 ?L3 ?problemID
    """
    myobj = {'query':
        queryTemplate.format(olympiadCode=olympiad,
                             gradeMax=grades[1],
                             gradeMin=grades[0],
                             yearMax=years[1],
                             yearMin=years[0])
    }
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text
