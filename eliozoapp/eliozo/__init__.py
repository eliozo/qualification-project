import os
from flask import Flask, render_template, abort, url_for, json, jsonify, request, session, redirect, send_from_directory
from flask_babel import Babel, _
import json
import html
import requests
import re
from .webmd_utils import fix_image_links, mathBeautify
from collections import defaultdict
from authlib.integrations.flask_client import OAuth


from eliozo_dao.sparql_access import SparqlAccess
from controllers.worksheets import getWorksheets


import logging
# from babel.support import MissingTranslationError

from flask_babel import Babel, gettext as original_gettext

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response


FUSEKI_URL_LINUX = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'

import platform

# Get the operating system name
os_name = platform.system()

# Check if it's Windows
if os_name == 'Windows':
    FUSEKI_URL=FUSEKI_URL_LINUX
else:
    FUSEKI_URL=FUSEKI_URL_LINUX

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



def getSPARQLProblem(arg, lang):
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemTextHtml ?video ?problemYear ?country ?olympiad 
?problemBook ?problemBookSection ?problemGrade ?problem_number
?topicIdentifier ?methodIdentifier ?questionType ?domain WHERE {{
  ?problem eliozo:problemID '{problemid}' ;
           eliozo:problemTextHtml ?problemTextHtml .
           FILTER (lang(?problemTextHtml) = "{language}")
  OPTIONAL {{
    ?problem eliozo:problemYear ?year ;
             eliozo:olympiadCode ?olympiad ;
             eliozo:problemGrade ?grade ;
             eliozo:country ?country .
  }}
  OPTIONAL {{
    ?problem eliozo:hasVideo ?video .
  }}
  OPTIONAL {{
    ?problem eliozo:problemYear ?problemYear .
  }}
  OPTIONAL {{
    ?problem eliozo:country ?country .
  }}
  OPTIONAL {{
    ?problem eliozo:olympiad ?olympiad .
  }}
  OPTIONAL {{
    ?problem eliozo:problemBook ?problemBook .
  }}
  OPTIONAL {{
    ?problem eliozo:problemBookSection ?problemBookSection .
  }}
  OPTIONAL {{
    ?problem eliozo:problemGrade ?problemGrade .
  }}
  OPTIONAL {{
    ?problem eliozo:problem_number ?problem_number .
  }}  
  OPTIONAL {{
    ?problem eliozo:topic ?topic .
    ?topic eliozo:topicID ?topicIdentifier .
  }}  
  OPTIONAL {{
    ?problem eliozo:method ?method .
    ?method eliozo:topicID ?methodIdentifier .
  }}  
  OPTIONAL {{
    ?problem eliozo:questionType ?questionType .
  }}  
  OPTIONAL {{
    ?problem eliozo:domain ?domain .
  }}  
}}"""

    myobj = {'query':  queryTemplate.format(problemid=arg, language=lang) }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLProblemSolutions(arg, lang):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemTextHtml ?solutionTextHtml WHERE {{
  ?problem eliozo:problemID '{problemid}' ;
  eliozo:problemTextHtml ?problemTextHtml .
  FILTER (lang(?problemTextHtml) = "{language}")
  FILTER (lang(?solutionTextHtml) = "{language}")
  OPTIONAL {{
    ?problem eliozo:problemSolution ?problemSolution . 
    ?problemSolution eliozo:solutionTextHtml ?solutionTextHtml .
  }}  
}}    
"""

    actual_query = queryTemplate.format(problemid=arg, language=lang)
    myobj = {'query':  actual_query}
    print('*** query ***')
    print(actual_query)
    print('*** end query ***')
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    print('*** results ***')
    print(x.text)
    print('*** end results ***')
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

def getProblemsByKeywordSPARQL(thePattern, isCaseSensitive):
    if not isCaseSensitive:
        escapedPattern = thePattern.lower()
        isLcase = 'lcase'
    else:
        escapedPattern = thePattern
        isLcase = ''

    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problem ?problemid ?text ?textHtml ?grade
WHERE {{
    ?problem eliozo:problemID ?problemid ;
    eliozo:problemText ?text ;
    eliozo:problemTextHtml ?textHtml .
    OPTIONAL {{
        ?problem eliozo:problemGrade ?grade .
    }}
    FILTER (contains({lcase}(?text), "{pattern}"))
}} ORDER BY ?grade ?problemid
LIMIT 10
"""
    escapedPattern = escapedPattern.replace('"', '\\"')

    query = queryTemplate.format(pattern=escapedPattern, lcase=isLcase)
    myobj = {'query': query}
    print(f"***** query in getProblemsByKeywordSPARQL('{thePattern}')")
    print(query)
    print("===== END =====")

    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    print("===== THEEND =====")
    x = requests.post(url, myobj, head)
    print("===== THETHEEND =====")
    print(f"***** x.text in getProblemsByKeywordSPARQL('{thePattern}')")
    print(x.text)
    print("===== END =====")

    return x.text

def getProblemsByRegexSPARQL(thePattern, isCaseSensitive):
    # so far no escaping pattern
    if not isCaseSensitive:
        escapedPattern = thePattern.lower()
        isLcase = 'lcase'
    else:
        escapedPattern = thePattern
        isLcase = ''

    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problem ?problemid ?text ?textHtml ?grade
WHERE {{
    ?problem eliozo:problemID ?problemid ;
    eliozo:problemText ?text ;
    eliozo:problemTextHtml ?textHtml ;
    OPTIONAL {{
        ?problem eliozo:problemGrade ?grade .
    }}
    FILTER (regex({lcase}(?text), "{pattern}"))
}} ORDER BY ?grade ?problemid
LIMIT 10
"""
    escapedPattern = escapedPattern.replace('"', '\\"')
    escapedPattern = escapedPattern.replace('\\', '\\\\')

    query = queryTemplate.format(pattern=escapedPattern, lcase=isLcase)
    myobj = {'query': query}
    print(f"***** query in getProblemsByRegexSPARQL('{thePattern}')")
    print(query)
    print("===== END =====")

    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    print("===== THEEND =====")
    x = requests.post(url, myobj, head)
    print("===== THETHEEND =====")
    print(f"***** x.text in getProblemsByRegexSPARQL('{thePattern}')")
    print(x.text)
    print("===== END =====")

    return x.text




def getProblemsByFiltersSPARQL(params, theOffset):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemid ?text ?grade WHERE {{
  {extraClauses}
  ?problem eliozo:problemID ?problemid ;
           {grade}
           {olympiad}
           {domain}
           {questionType}
           {method}
           {solution}
           {video}
      eliozo:problemTextHtml ?text .
      
      {fGrade} {fOlympiad} {fDomain} {fQuestionType} {fMethod} {fSolution} {fVideo}
      
      OPTIONAL {{
        ?problem eliozo:problemGrade ?grade .
      }}
}} ORDER BY ?grade ?problemid LIMIT 10 OFFSET {offset}
"""
    theGrade = "" if params["grade"] in ["NA","-"] else f'eliozo:suggestedGrade {params["grade"]} ; '
    theOlympiad = "" if params["olympiad"] in ["NA","-"] else f'eliozo:olympiadType "{params["olympiad"]}" ; '
    theDomain = "" if params["domain"] in ["NA","-"] else f'eliozo:domain "{params["domain"]}" ; '
    theQuestionType = "" if params["questionType"] in ["NA","-"] else f'eliozo:questionType "{params["questionType"]}" ; '
    theMethod = "" if params["method"] in ["NA","-"] else f'eliozo:method ?mymethod ; '
    theSolution = "" if params["hasSolution"] in ["NA","-"] else f'eliozo:problemSolution ?someSolution ; '
    theVideo = "" if params["hasVideo"] in ["NA","-"] else f'eliozo:hasVideo ?someVideo ; '
    theExtraClauses = "" if params["method"] in ["NA", "-"] else f'?mymethod skos:broader* {params["method"]} . '

    theFGrade = "" if params["grade"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:suggestedGrade ?gg . }"
    theFOlympiad = "" if params["olympiad"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:olympiadType ?oo . }"
    theFDomain = "" if params["domain"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:domain ?dd . }"
    theFQuestionType = "" if params["questionType"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:questionType ?qq . }"
    theFMethod = "" if params["method"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:method ?mm . }"
    theFSolution = "" if params["hasSolution"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:problemSolution ?ss . }"
    theFVideo = "" if params["hasVideo"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:hasVideo ?vv . }"

    q = queryTemplate.format(grade=theGrade, olympiad=theOlympiad,
                             domain=theDomain, questionType=theQuestionType,
                             method=theMethod, offset=theOffset,
                             solution=theSolution, video=theVideo,
                             extraClauses=theExtraClauses,
                             fGrade=theFGrade, fOlympiad=theFOlympiad, fDomain=theFDomain,
                             fQuestionType=theFQuestionType, fMethod=theFMethod,
                             fSolution=theFSolution, fVideo=theFVideo)
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(f"filter_query = {q}")
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")


    myobj = {'query': q}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getProblemCountsByFiltersSPARQL(params):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT (COUNT(*) AS ?count) WHERE {{
  ?problem eliozo:problemID ?problemid ;
           {grade}
           {olympiad}
           {domain}
           {questionType}
           {method} 
           {solution}
           {video} .
           {fGrade} {fOlympiad} {fDomain} {fQuestionType} {fMethod} {fSolution} {fVideo}
}}
"""
    theGrade = '' if params["grade"] in ["NA","-"] else f'eliozo:suggestedGrade {params["grade"]} ; '
    theOlympiad = '' if params["olympiad"] in ["NA","-"] else f'eliozo:olympiadType "{params["olympiad"]}" ; '
    theDomain = '' if params["domain"] in ["NA","-"] else f'eliozo:domain "{params["domain"]}" ; '
    theQuestionType = '' if params["questionType"] in ["NA","-"] else f'eliozo:questionType "{params["questionType"]}" ; '
    theMethod = '' if params["method"] in ["NA","-"] else f'eliozo:method ?mymethod . ?mymethod skos:broader* {params["method"]} ; '
    theSolution = "" if params["hasSolution"] in ["NA","-"] else f'eliozo:problemSolution ?someSolution ; '
    theVideo = "" if params["hasVideo"] in ["NA","-"] else f'eliozo:hasVideo ?someVideo ; '
    theFGrade = "" if params["grade"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:suggestedGrade ?gg . }"
    theFOlympiad = "" if params["olympiad"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:olympiadType ?oo . }"
    theFDomain = "" if params["domain"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:domain ?dd . }"
    theFQuestionType = "" if params["questionType"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:questionType ?qq . }"
    theFMethod = "" if params["method"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:method ?mm . }"
    theFSolution = "" if params["hasSolution"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:problemSolution ?ss . }"
    theFVideo = "" if params["hasVideo"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:hasVideo ?vv . }"

    q = queryTemplate.format(grade=theGrade, olympiad=theOlympiad,
                             domain=theDomain, questionType=theQuestionType,
                             method=theMethod, solution=theSolution, video=theVideo,
                             fGrade=theFGrade, fOlympiad=theFOlympiad, fDomain=theFDomain,
                             fQuestionType=theFQuestionType, fMethod=theFMethod,
                             fSolution=theFSolution, fVideo=theFVideo)
    myobj = {'query': q}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    # print('************')
    # print(f'q = {q}')
    # print("============")
    x = requests.post(url, myobj, head)
    # print(f'x = "{x.text}"')
    return x.text


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
  FILTER (?grade < {gradeMax} && ?grade > {gradeMin})
  FILTER (?year < {yearMax} && ?year > {yearMin})
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
                             gradeMax = (grades[1]),
                             gradeMin = (grades[0]-1),
                             yearMax = (years[1]),
                             yearMin = (years[0] - 1))
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
    FILTER (?grade < {gradeMax} && ?grade > {gradeMin})
    FILTER (?year < {yearMax} && ?year > {yearMin})
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
                             gradeMax = (grades[1]),
                             gradeMin = (grades[0]-1),
                             yearMax = (years[1]),
                             yearMin = (years[0] - 1))
    }
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


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
        FILTER (?grade < {gradeMax} && ?grade > {gradeMin})
        FILTER (?year < {yearMax} && ?year > {yearMin})
    }}
    GROUP BY ?domain ?questionType
    ORDER BY ?domain ?questionType
    """
    myobj = {'query': 
        queryTemplate.format(olympiadCode=olympiad, 
                             gradeMax = (grades[1]),
                             gradeMin = (grades[0]-1),
                             yearMax = (years[1]),
                             yearMin = (years[0] - 1))
    }
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


# @app.route("/report/domains-by-qtype")
# def domains_by_qtype():
#     # If you already have the JSON, skip the request and pass it in directly
#     r = requests.get(
#         SPARQL_ENDPOINT,
#         params={"query": SPARQL_QUERY, "format": "application/sparql-results+json"},
#         timeout=30,
#     )
#     r.raise_for_status()
#     sparql_json = r.json()

#     domains, question_types, matrix = build_matrix(sparql_json)
#     return render_template(
#         "domain_qtype_table.html",
#         domains=domains,
#         question_types=question_types,
#         matrix=matrix,
#     )





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
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLOlympiads(lang):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?olympiadCountry ?olympiad ?olympiadCode ?olympiadName ?olympiadDescription WHERE {{ 
  ?olympiad eliozo:olympiadName ?olympiadName ;
            eliozo:olympiadDescription ?olympiadDescription ;
            eliozo:olympiadCode ?olympiadCode .
            FILTER (lang(?olympiadDescription) = "{language}")
            FILTER (lang(?olympiadName) = "{language}")
  OPTIONAL {{
    ?olympiad eliozo:olympiadCountry ?olympiadCountry .
  }}
}} ORDER BY ?olympiadCountry ?olympiadName
"""

    myobj = { 'query': queryTemplate.format(language=lang) }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLOlympiadYears(country, olympiad):
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?year ?grade WHERE {{ 
  ?problem eliozo:country '{country}' ;
           eliozo:olympiadCode '{olympiad}' ; 
           eliozo:problemYear ?year ; 
           eliozo:problemGrade ?grade . 
}} ORDER BY DESC(?year) ?grade"""

    myobj = {'query': queryTemplate.format(country=country, olympiad=olympiad)}
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLOlympiadTimeIDs(country, olympiad):
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problemTimeID  WHERE {{
  ?problem eliozo:country '{country}' ;
           eliozo:olympiadCode '{olympiad}' ; 
           eliozo:problemTimeID ?problemTimeID . 
}} ORDER BY DESC(?problemTimeID)"""
    myobj = {'query': queryTemplate.format(country=country, olympiad=olympiad)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLOlympiadTimeIDsGrades(country, olympiad):
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problemTimeID ?grade WHERE {{
  ?problem eliozo:country '{country}' ;
           eliozo:olympiadCode '{olympiad}' ; 
           eliozo:problemTimeID ?problemTimeID ; 
           eliozo:problemGrade ?grade . 
}} ORDER BY DESC(?problemTimeID) ?grade"""
    myobj = {'query': queryTemplate.format(country=country, olympiad=olympiad)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text




def getSPARQLOlympiadProblemsByEventAndGrade(event, country, grade, olympiad, lang):
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?text ?problemid ?problem_number WHERE {{
      ?problem eliozo:problemTimeID '{event}' .
      ?problem eliozo:country '{country}' .
      ?problem eliozo:problemTextHtml ?text .
      ?problem eliozo:problemID ?problemid .
      ?problem eliozo:problem_number ?problem_number .
      ?problem eliozo:problemGrade {grade} .
      ?problem eliozo:olympiadCode '{olympiad_code}' .
      FILTER (lang(?text) = "{language}")
    }} ORDER BY ?problem_number
    """


    myobj = { 'query':
        queryTemplate.format(event=event, country=country, grade=grade, olympiad_code=olympiad, language=lang)
    }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLOlympiadProblemsByEvent(event, country, olympiad, lang):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?text ?problemid ?problem_number ?problem_grade ?suffix WHERE {{
  ?problem eliozo:problemTimeID '{event}' .
  ?problem eliozo:country '{country}' .
  ?problem eliozo:problemTextHtml ?text .
  ?problem eliozo:problemID ?problemid .
  ?problem eliozo:problem_number ?problem_number .
  ?problem eliozo:problemGrade ?problem_grade .
  ?problem eliozo:olympiadCode '{olympiad_code}' .
  ?problem eliozo:suffix ?suffix .
  FILTER (lang(?text) = "{language}")
}} ORDER BY ?problem_grade ?suffix ?problem_number
"""


    myobj = { 'query':
        queryTemplate.format(event=event, country=country, olympiad_code=olympiad, language=lang)
    }
    # print(f"wrongSPARQL = {myobj}")

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    # print(f'myxtext = {x.text}')
    return x.text

def getSPARQLBook(bookid, sectionid):
    url = FUSEKI_URL

    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?text ?problemid ?problem_number ?imagefile WHERE {{
  ?problem eliozo:problemBook '{book}' ;
           eliozo:problemBookSection '{section}' ;
           eliozo:problemTextHtml ?text ;
           eliozo:problemID ?problemid ;
           eliozo:problem_number ?problem_number .
  OPTIONAL {{
    ?problem eliozo:image ?imagefile .
  }} .
}} ORDER BY ?problem_number   
"""


    myobj = {'query':
        queryTemplate.format(book=bookid, section=sectionid)
    }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text
              


def getSPARQLVideoBookmarks(problemid):
    url = FUSEKI_URL
    myobj = { 'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>\n'+
    '''SELECT ?videoTitle ?youtubeID ?tstamp ?bmtext WHERE {
  ?problem eliozo:problemID \''''+problemid+'''\' .
  OPTIONAL {
    ?problem eliozo:hasVideo ?video .
    ?video eliozo:videoTitle ?videoTitle ;
           eliozo:videoYoutube ?youtubeID ;
           eliozo:videoBookmarks ?videoBookmarks .
    ?videoBookmarks ?prop ?bookmark .
    ?bookmark eliozo:videoBookmarkTstamp ?tstamp ;
              eliozo:videoBookmarkText ?bmtext .
  }.
} ORDER BY ?tstamp'''
    }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getAllSPARQLVideos():
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL

    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemid ?text ?textHtml WHERE {
  ?problem eliozo:problemID ?problemid ;
           eliozo:problemText ?text ;
           eliozo:problemTextHtml ?textHtml ;
           eliozo:problemGrade ?grade ;
  	       eliozo:hasVideo ?video .         
  } ORDER BY ?grade ?problemid
"""

    myobj = { 'query': queryTemplate }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


# def mathBeautify(a): # Izskaistina formulas ar MathJax Javascript bibliotēku
#     b0 = re.sub(r"\$\$([^\$]+)\$\$", r"<p><span class='math display'>\[\1\]</span></p>", a) # Aizstāj vairākrindu formulas $$..$$
#     b = re.sub(r"\$([^\$]+)\$", r"<span class='math inline'>\(\1\)</span>", b0) # Aizstāj inline formulas $...$ (Svarīga secība, kā aizstāj)
#     return b


def get_locale():
    locale = session.get('lang', 'lv')
    return locale


def configure_logging():
    logging.basicConfig(level=logging.WARNING)
    logger = logging.getLogger(__name__)
    return logger

logger = configure_logging()

def custom_gettext(string, **variables):
    translation = original_gettext(string, **variables)
    if translation == string:
        logger.warning(f"Missing translation for: {string}")
    return translation

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_pyfile(os.path.join(os.path.dirname(__file__), '..', 'config.py'))
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.secret_key = 'random_secret'  # Set a strong secret in production

    # Create OAuth instance
    oauth = OAuth(app)

    my_client_id= os.environ['GOOGLE_CLIENT_ID']
    my_secret=os.environ['GOOGLE_CLIENT_SECRET']

    # with open('/tmp/eliozo.txt', 'w') as f:
    #     f.write(f"client_id={my_client_id}\n")
    #     f.write(f"client_secret={my_secret}\n")

    # Register Google OAuth client
    # oauth.register(
    #     name='google',
    #     client_id= os.environ['GOOGLE_CLIENT_ID'],
    #     client_secret=os.environ['GOOGLE_CLIENT_SECRET'],
    #     access_token_url='https://oauth2.googleapis.com/token',
    #     access_token_params=None,
    #     authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
    #     authorize_params=None,
    #     api_base_url='https://www.googleapis.com/oauth2/v2/',
    #     userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
    #     client_kwargs={'scope': 'openid email profile'},
    # )

    # Register Google OAuth client
    oauth.register(
        name='google',
        #client_id= my_client_id,
        #client_secret=my_secret,
        client_id=os.environ['GOOGLE_CLIENT_ID'].strip(),
        client_secret=os.environ['GOOGLE_CLIENT_SECRET'].strip(),

        access_token_url='https://oauth2.googleapis.com/token',
        access_token_params=None,
        authorize_url='https://accounts.google.com/o/oauth2/v2/auth',
        authorize_params=None,
        api_base_url='https://www.googleapis.com/oauth2/v2/',
        userinfo_endpoint='https://openidconnect.googleapis.com/v1/userinfo',
        # Add this line explicitly:
        jwks_uri='https://www.googleapis.com/oauth2/v3/certs',
        client_kwargs={'scope': 'openid email profile'},
    )

    # The directory where your images are
    STATIC_IMAGE_ROOT = os.path.join(app.root_path, 'static', 'eliozo', 'images')

    # Configure the available languages
    LANGUAGES = {
        'en': 'English',
        'lv': 'Latvian',
        'lt': 'Lithuanian'
    }
    app.config['BABEL_DEFAULT_LOCALE'] = 'lv'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
    babel = Babel(app, locale_selector=get_locale)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    def replace_non_ascii_with_unicode_escape(text):
        non_ascii_characters = {'ā': '\\u0101', 'č': '\\u010D', 'ē': '\\u0113', 'ģ': '\\u0123', 'ī': '\\u012B',
                            'ķ': '\\u0137', 'ļ': '\\u013C', 'ņ': '\\u0146', 'š': '\\u0161', 'ū': '\\u016B',
                            'ž': '\\u017E'}
        replaced_text = ''
        for char in text:
            if char in non_ascii_characters:
                replaced_text += non_ascii_characters[char]
            else:
                replaced_text += char
        return replaced_text

    @app.route('/setlang')
    def setLanguage():
        lang = request.args.get('lang')
        next_url = request.args.get('next')
        next_url = '/eliozo' + request.args.get('next') if next_url else url_for('main')

        if lang in LANGUAGES:
            session['lang'] = lang
        else:
            session['lang'] = 'lv'

        return redirect(next_url)

    @app.route('/eliozo/static/eliozo/images/<path:filename>')
    def eliozo_static_images(filename):
        # Return file from $APP_ROOT/eliozo/static/eliozo/images/
        return send_from_directory(STATIC_IMAGE_ROOT, filename)


    @app.route('/')
    def main():
        keyword = request.args.get('keyword')
        
        fuseki_url = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'
        
        if keyword is None or keyword == "":
            template_context = {
                'active': 'main',
                'lang': session.get('lang', 'lv'),
                'searchMode': 'exact'
            }
            return render_template('main_content.html',  **template_context)
        new_keyword = replace_non_ascii_with_unicode_escape(keyword)
        # caseSensitive = request.args.get('caseSensitive')
        # print(f'caseSensitive = {caseSensitive}')
        # isCaseSensitive = (caseSensitive == '1')
        # regex = request.args.get('regex')
        # print(f'regex = {regex}')
        searchMode = request.args.get('searchMode')

        isRegex = (searchMode == 'regex')

        if not isRegex:
            link = json.loads(getProblemsByKeywordSPARQL(new_keyword, False))
        else:
            link = json.loads(getProblemsByRegexSPARQL(new_keyword, False))

        problems = []
        
        for item in link['results']['bindings']:
            problem_id_value = item['problemid']['value']
            problem_imagefile = ''
            # if 'imagefile' in item:
            #     problem_imagefile = item['imagefile']['value']
            problem_text_value = mathBeautify(item['textHtml']['value'])
            problem_text_value = fix_image_links(problem_text_value)
            d = {'problemid': problem_id_value, 'text': problem_text_value, 'imagefile': problem_imagefile}
            problems.append(d)

        template_context = {
            'problems': problems,
            'keyword' : keyword,
            'active': 'main',
            # 'regex': regex,
            # 'caseSensitive': caseSensitive,
            'searchMode': searchMode,
            'lang': session.get('lang', 'lv'),
            'title': 'Sākumlapa'
        }
        return render_template('main_content.html', **template_context)

    # faceted browse
    @app.route('/filter')
    def getFilter():
        requestParams = ['grade', 'olympiad', 'domain', 'questionType', 'method', 'hasSolution', 'hasVideo']
        params = dict()
        all_counts = {'grade': dict(), 'olympiad': dict(), 'domain': dict(),
                      'questionType': dict(), 'method': dict(), 'hasSolution': dict(), 'hasVideo': dict()}

        for requestParam in requestParams:
            requestVal = request.args.get(requestParam)
            if requestVal is None:
                requestVal = "NA"
            params[requestParam] = requestVal

        offset = request.args.get('offset')
        if offset is None or offset == '':
            offset = 0
        else:
            offset = int(offset)

        problems = []

        olympiadTypeDict = [('Contest', {'en':'Contest', 'lt':'Konkursas', 'lv':'Konkurss'}),
                            ('Book', {'en':'Book', 'lt':'Knyga', 'lv':'Grāmata'}),
                            ('RegionalOrOpen', {'en':'Regional/Open', 'lt':'Rajoninės/atviros', 'lv':'Reģionālās/atklātās'}),
                            ('National', {'en':'National', 'lt':'Respublikinė', 'lv':'Nacionālā'}),
                            ('TeamSelection', {'en':'Team selection', 'lt':'Atrankos', 'lv':'Papildsacensības'}),
                            ('International', {'en':'International', 'lt':'Tarptautinė', 'lv':'Starptautiska'}),
                            ('-', {'en':'NA', 'lt':'NA', 'lv':'NA'})]

        methodDict = [('eliozo:MTH_MathematicalInduction', {'en':'Induction', 'lt':'Indukcija', 'lv':'Indukcija'}),
                      ('eliozo:MTH_MeanValuePrinciple', {'en':'MeanValue', 'lt':'Vidutinė Vertė', 'lv':'Vid.Vērtība'}),
                      ('eliozo:MTH_ExtremePrinciple', {'en':'Extreme element','lt':'Kraštinis Elementas', 'lv':'Ekstr.Elements'}),
                      ('eliozo:MTH_InvariantMethod', {'en':'Invariant','lt':'Invariantas', 'lv':'Invariants'}),
                      ('eliozo:MTH_ContradictionMethod', {'en':'Contradiction', 'lt':'Prieštaravimas', 'lv': 'Pretruna'}),
                      ('eliozo:MTH_InterpretationMethod', {'en':'Interpretation', 'lt': 'Interpretacija', 'lv':'Interpretācija'}),
                      ('eliozo:MTH_Transformations', {'en':'Transforms', 'lt':'Pertvarkymai', 'lv':'Pārveidojumi'}),
                      ('eliozo:MTH_Augmentation', {'en':'Structure augmentation', 'lt':'Pagalbinės Konstrukcijos', 'lv':'Papildkonstrukcijas'}),
                      ('eliozo:MTH_Algorithms', {'en':'Algorithms', 'lt':'Algoritmai', 'lv':'Algoritmi'}),
                      ('-', {'en':'NA', 'lt':'NA', 'lv':'NA'})]

        solutionDict = [('1', {'en':'Yes', 'lt':'Yra', 'lv':'Ir'}),
                        ('-', {'en':'No', 'lt':'Nėra', 'lv':'Nav'})]

        if all(value == 'NA' for value in params.values()):
        # if grade == "NA" and olympiad == "NA" and  domain == "NA" and questionType == "NA" and method == "NA" and hasSolution == "NA" and hasVideo == "NA":
            template_context = {
                'problems': problems,
                'active': 'filter',
                'navlinks': [
                    {
                        'url': 'getFilter', 
                        'title': 'Filters'
                    }
                ],
                'lang': session.get('lang', 'lv'),
                'params': params,
                'all_counts': all_counts,
                'olympiadTypeDict': olympiadTypeDict,
                'methodDict': methodDict,
                'solutionDict': solutionDict,
                'title': 'Filtri'
            }
            return render_template('filter_content.html', **template_context)

        else:
            link = json.loads(getProblemsByFiltersSPARQL(params, offset))
            for item in link['results']['bindings']:
                problem_id_value = item['problemid']['value']
                problem_text_value = mathBeautify(item['text']['value'])
                problem_text_value = fix_image_links(problem_text_value)
                d = {'problemid': problem_id_value, 'text': problem_text_value}
                problems.append(d)

            all_values = {'grade':['5', '6', '7', '8',
                                   '9', '10', '11', '12', '-'],
                          'olympiad':['Contest', 'Book', 'RegionalOrOpen',
                                      'National', 'TeamSelection', 'International', '-'],
                          'domain':['Alg', 'Comb', 'Geom', 'NT', '-'],
                          'questionType':['FindAll', 'FindCount', 'FindOptimal', 'FindExample',
                                          'Prove', 'ProveDisprove', 'Algorithm', 'ShortAnswer', '-'],
                          'method':['eliozo:MTH_MathematicalInduction', 
                                    'eliozo:MTH_MeanValuePrinciple', 
                                    'eliozo:MTH_ExtremePrinciple',
                                    'eliozo:MTH_InvariantMethod', 
                                    'eliozo:MTH_ContradictionMethod', 
                                    'eliozo:MTH_InterpretationMethod',
                                    'eliozo:MTH_Transformations', 
                                    'eliozo:MTH_Augmentation', 
                                    'eliozo:MTH_Algorithms',
                                    '-'],
                          'hasSolution':['1', '-'],
                          'hasVideo':['1', '-']}

            for par in ['grade', 'olympiad', 'domain', 'questionType', 'method', 'hasSolution', 'hasVideo']:
                params1 = params.copy()
                for curr_val in all_values[par]:
                    params1[par] = curr_val

                    count_json = json.loads(getProblemCountsByFiltersSPARQL(params1))
                    all_counts[par][curr_val] = count_json['results']['bindings'][0]['count']['value']

            # if params['domain'] not in all_counts['domain']:
            #     params['domain'] = ''
            page_offsets = []
            count_json = json.loads(getProblemCountsByFiltersSPARQL(params))
            curr_filter_count = int(count_json['results']['bindings'][0]['count']['value'])

            if curr_filter_count > 10:
                current_offset = 0
                while curr_filter_count - current_offset > 0:
                    page_offsets.append(current_offset)
                    current_offset += 10

            print('======================')
            print(f'all_counts = {all_counts}')
            print('++++++++++++++++++++++')

            template_context = {
                'problems': problems,
                'params': params,
                'all_counts': all_counts,
                'olympiadTypeDict': olympiadTypeDict,
                'methodDict': methodDict,
                'solutionDict': solutionDict,
                'page_offsets': page_offsets,
                'myoffset': offset,
                'active': 'filter',
                'navlinks': [
                    {
                        'url': 'getFilter', 
                        'title': 'Filters'
                    }
                ],
                'lang': session.get('lang', 'lv'),
                'title': 'Filtri'
            }
            return render_template('filter_content.html', **template_context)

    # json 
    @app.route("/json")
    def getJson():
        # Lasa failu
        with open('C:/Users/eliz_/Documents/qualification-project/flask-application/data/file.json', 'r', encoding="utf-8") as myfile:
            data = myfile.read()
        return render_template('index.html', title="page", jsonfile=json.dumps(data))

    @app.route("/references")
    def getReferences():
        # return render_template("info.html")
        lang = session.get('lang', 'lv')
        fuseki_url = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'
        sparql_access = SparqlAccess(fuseki_url)
        sources = sparql_access.getSPARQLSources(lang)
        template_context = {
            'active': 'about_us',
            'navlinks': [
                {
                    'url': 'getReferences', 
                    'title': 'References'
                }
            ],
            'lang': lang,
            'sources': sources,
            'title': 'Atsauces'
        }
        return render_template('references_content.html', **template_context)




    @app.route('/topics', methods=['GET','POST'])
    def getTopics():
        data = json.loads(getSPARQLtopics())

        all_topics = []
        all_topic_info = dict() # Vārdnīca visai prasmju tabulai

        current_topic = "NA"

        for item in data['results']['bindings']:
            # A new topic appears
            if item['topicIdentifier']['value'] != current_topic:
                all_topics.append(item['topicIdentifier']['value']) # Pievienojam jaunu prasmi sarakstam all_topics
                current_topic = item['topicIdentifier']['value'] # Atceramies pēdējo pievienoto vērtību, lai neiespraustu atkārtoti
                current_topic_info = dict() # Vārdnīca vienai tabulas rindai
                current_topic_info['topicIdentifier'] = current_topic
                current_topic_info['topicNumber'] = item['topicNumber']['value']
                number_items = item['topicNumber']['value'].split(".")

                beautiful_description = mathBeautify(item['topicDescription']['value'])
                current_topic_info['topicDescription'] = beautiful_description
                current_topic_info['topicName'] = mathBeautify(item['topicName']['value'])
                if "problemid" in item:
                    current_topic_info['problems'] = [item['problemid']['value']]
                else:
                    current_topic_info['problems'] = []
                all_topic_info[current_topic] = current_topic_info # Lielajā vārdnīcā iesprauž mazo vārdnīcu
            else:
                current_topic_info['problems'].append(item['problemid']['value']) # Pievieno tikai jauno uzdevuma ID

        # domain_titles = {'1': 'Algebra', '2': 'Kombinatorika', '3': 'Ģeometrija', '4': 'Skaitļu teorija'}
        structured_topics = []
        current_LTopics = None
        current_subtopics = None
        current_subsubtopics = None
        for topic in all_topics:
            topicNumber = all_topic_info[topic]['topicNumber']
            topicId = all_topic_info[topic]['topicIdentifier']

            if topicNumber.endswith('.0.0.0.0'):
                LTopics = []
                current_LTopics = LTopics
                L1_number = topicNumber[:-len('.0.0.0.0')]
                L1_name = all_topic_info[topic]['topicName']
                L1_desc = all_topic_info[topic]['topicDescription']
                L1_prob = all_topic_info[topic]['problems']
                structured_topics.append({'number':L1_number,
                                          'topicId':topicId,
                                          'name':L1_name,
                                          'desc':L1_desc,
                                          'prob':L1_prob,
                                          'subtopics': LTopics})
            elif topicNumber.endswith('.0.0.0'):
                subtopics = []
                current_subtopics = subtopics
                L2_number = topicNumber[:-len('.0.0.0')]
                L2_label = L2_number.replace('.', '_')
                L2_name = all_topic_info[topic]['topicName']
                L2_desc = all_topic_info[topic]['topicDescription']
                L2_prob = all_topic_info[topic]['problems']
                current_LTopics.append({'number':L2_number,
                                        'topicId':topicId,
                                        'label':L2_label,
                                        'name':L2_name,
                                        'desc':L2_desc,
                                        'prob': L2_prob,
                                        'subtopics': subtopics})
            elif topicNumber.endswith('.0.0'):
                subsubtopics = []
                current_subsubtopics = subsubtopics
                L3_number = topicNumber[:-len('.0.0')]
                L3_name = all_topic_info[topic]['topicName']
                L3_desc = all_topic_info[topic]['topicDescription']
                L3_prob = all_topic_info[topic]['problems']
                current_subtopics.append({'number':L3_number,
                                          'topicId':topicId,
                                          'name':L3_name,
                                          'desc': L3_desc,
                                          'prob': L3_prob,
                                          'subtopics':subsubtopics})
            else:
                L45_number = topicNumber
                if topicNumber.endswith('.0'):
                    L45_number = topicNumber[:-len('.0')]
                L45_name = all_topic_info[topic]['topicName']
                L45_desc = all_topic_info[topic]['topicDescription']
                L45_prob = all_topic_info[topic]['problems']
                current_subsubtopics.append({'number':L45_number,
                                             'topicId':topicId,
                                             'name':L45_name, 
                                             'desc': L45_desc, 
                                             'prob':L45_prob})

        template_context = {
            'all_topics': all_topics,
            'all_topic_info': all_topic_info,
            'active': 'topics',
            'navlinks': [
                {
                    'url': 'getTopics', 
                    'title': 'Topics'
                }
            ],
            'lang': session.get('lang', 'lv'),
            'title': 'Tēmas',
            'structured_topics': structured_topics
        }

        return render_template('topics_content.html', **template_context)


    @app.route('/methods', methods=['GET', 'POST'])
    def getMethods():
        lang = session.get('lang', 'lv')
        template_context = {
            'active': 'order_by',
            'navlinks': [
                {
                    'url': 'getMethods', 
                    'title': 'Methods'
                }
            ],
            'lang': lang,
            'title': 'Metodes'
        }
        return render_template('methods_content.html', **template_context)
    

    @app.route('/genres', methods=['GET', 'POST'])
    def getGenres():
        lang = session.get('lang', 'lv')
        data = json.loads(getSPARQLdomains())

        all_genres = {'1':[], '2':[], '3':[], '4':[]}
        all_genres_info = dict()

        current_genre = "NA"

        for item in data['results']['bindings']:
            if item['domainNumber']['value'].endswith('0.0'):
                pass

            elif item['domainID']['value'] != current_genre:
                current_genre = item['domainID']['value']
                current_domain = item['L1']['value']
                all_genres[current_domain].append(item['domainID']['value'])

                current_genre_info = dict()
                current_genre_info['domainIdentifier'] = item['domainID']['value'][4:]
                current_genre_info['domainNumber'] = item['domainNumber']['value']
                current_genre_info['domainName'] = item['domainName']['value']
                beautiful_description = mathBeautify(item['domainDescription']['value'])
                current_genre_info['domainDescription'] = beautiful_description
                if "problemid" in item:
                    current_genre_info['problems'] = [item['problemid']['value']]
                else:
                    current_genre_info['problems'] = []
                all_genres_info[current_genre] = current_genre_info # Lielajā vārdnīcā iesprauž mazo vārdnīcu
            else:
                current_genre_info['problems'].append(item['problemid']['value']) # Pievieno tikai jauno uzdevuma ID


        template_context = {
            'all_genres': all_genres,
            'domain_names': {'1':'Alg', '2':'Comb', '3':'Geom', '4':'NT'},
            'domain_keys': ['1', '2', '3', '4'],
            'all_genres_info': all_genres_info,
            'active': 'order_by',
            'navlinks': [
                {
                    'url': 'getGenres', 
                    'title': 'Genres'
                }
            ],
            'lang': lang,
            'title': 'Žanri'
        }
        return render_template('genres_content.html', **template_context)    


    @app.route('/concepts', methods=['GET','POST'])
    def getConcepts():
        concepts_problems = json.loads(getSPARQLconcepts())

        concept_list = []
        current_concept = "NA"
        current_problems = []
        for item in concepts_problems['results']['bindings']:
            concept = item['concept']['value']
            if concept != current_concept:
                termLV = item['termLV']['value']
                termEN = item['termEN']['value']
                conceptID = item['conceptID']['value']
                descLV = ''
                if 'descLV' in item:
                    descLV = mathBeautify(item['descLV']['value'])

                current_concept = concept
                current_problems = [item['problemID']['value']]
                concept_list.append({
                    'termLV': termLV,
                    'termEN': termEN,
                    'conceptID': conceptID,
                    'descLV': descLV,
                    'problems': current_problems
                })

            else:
                current_problems.append(item['problemID']['value'])
        concept_list.append({
                    'termLV': termLV,
                    'termEN': termEN,
                    'conceptID': conceptID,
                    'descLV': descLV,
                    'problems': current_problems})

        template_context = {
            'all_concepts': concept_list,
            'active': 'order_by',
            'navlinks': [
                {
                    'url': 'getConcepts', 
                    'title': 'Concepts'
                }
            ],
            'lang': session.get('lang', 'lv'),
            'title': 'Jēdzieni'
        }
        return render_template('concepts_content.html', **template_context)

    @app.route('/topic_tasks', methods=['GET','POST']) # Kontrolieris, kas iegūst prasmes kopā ar uzdevumiem
    def getTopic():
        topic = request.args.get('topicIdentifier')

        topic_details = json.loads(getTopicDetails(topic))
        parentNumber = topic_details['results']['bindings'][0]['topicNumber']['value']
        parentName = topic_details['results']['bindings'][0]['topicName']['value']
        parentDesc = topic_details['results']['bindings'][0]['topicDesc']['value']
        parentDesc = mathBeautify(parentDesc)

        all_topics = json.loads(getAllTopicChildren(topic))
        topic_list = []
        for topic_item in all_topics['results']['bindings']: # all_topics saraksts ar vārdnīcām
            prefLabel = topic_item['prefLabel']['value']
            topicName = topic_item['topicName']['value']
            topicName = mathBeautify(topicName)
            topicNum = topic_item['num']['value']
            dd = {'prefLabel': prefLabel, 'topicNum': topicNum, 'topicName': topicName}
            topic_list.append(dd)

        data = json.loads(getTopicProblemsSPARQL(topic))
        problem_list = []
        for data_item in data['results']['bindings']:
            problemTextHtml = data_item['text']['value']
            problemTextHtml = fix_image_links(problemTextHtml)
            problemTextHtml = mathBeautify(problemTextHtml)
            problem_list.append({'problemid': data_item['problemid']['value'], 'text': problemTextHtml})

        template_context = {
            'topic': topic,
            'parentNumber': parentNumber,
            'parentName': parentName,
            'parentDesc': parentDesc,
            'problem_list': problem_list,
            'topic_list' : topic_list,
            'active': 'topics',
            'lang': session.get('lang', 'lv'),
            'title': 'Tēma'
        }
        return render_template('topic_tasks_content.html', **template_context)
    
    @app.route('/book_problems', methods=['GET', 'POST'])
    def getBook():
        bookid = request.args.get('book_id')
        sectionid = request.args.get('section_id')
        link = json.loads(getSPARQLBook(bookid, sectionid))

        problems = []
        
        for item in link['results']['bindings']:
            problem_id_value = item['problemid']['value']
            problem_imagefile = ''
            if 'imagefile' in item:
                problem_imagefile = item['imagefile']['value']
            problem_number_value = item['problem_number']['value']
            problemTextHtml = mathBeautify(item['text']['value'])
            problemTextHtml = fix_image_links(problemTextHtml)
            problemTextHtml = mathBeautify(problemTextHtml)

            d = {'problemid': problem_id_value, 'problem_number':problem_number_value, 'text': problemTextHtml, 'imagefile': problem_imagefile}
            problems.append(d)


        template_context = {
            'problems': problems,
            'bookid' : bookid,
            'active': 'archive',
            'lang': session.get('lang', 'lv'),
            'title': 'Grāmata'
        }

        return render_template('book_problems_content.html', **template_context)


    @app.route('/problem', methods=['GET','POST'])
    def getProblem():
        lang = session.get('lang', 'lv')
        # lang = 'lv'
        problemid = request.args.get('problemid')
        solnData = json.loads(getSPARQLProblemSolutions(problemid, lang))
        hasSolution = False
        if len(solnData['results']['bindings']) > 0 and 'solutionTextHtml' in solnData['results']['bindings'][0]:
            hasSolution = True
        # if 'solutionTextHtml' in solnData['results']['bindings'][0]:
        #     hasSolution = True


        data = json.loads(getSPARQLProblem(problemid, lang))

        problemTextHtml = data['results']['bindings'][0]['problemTextHtml']['value']

        problemTextHtml = fix_image_links(problemTextHtml)
        problemTextHtml = mathBeautify(problemTextHtml)

        if 'video' in data['results']['bindings'][0]:
            hasVideo = data['results']['bindings'][0]['video']['value'] != ''
        else:
            hasVideo = False

        # if 'solutionTextHtml' in data['results']['bindings'][0]:
        #     solutionTextHtml = data['results']['bindings'][0]['solutionTextHtml']['value']
        #     solutionTextHtml = fix_image_links(solutionTextHtml)
        #     solutionTextHtml = mathBeautify(solutionTextHtml)
        # else:
        #     solutionTextHtml = ''

        bookmarks = []
        video_title = "NA"
        youtubeID = "NA"

        if hasVideo:

            video_data = json.loads(getSPARQLVideoBookmarks(problemid))

            for item in video_data['results']['bindings']:
                video_title = item['videoTitle']['value']
                youtubeID = item['youtubeID']['value']
                minutes = int(item['tstamp']['value']) // 60
                if minutes < 10:
                    minutes = '0' + str(minutes)
                seconds = int(item['tstamp']['value']) % 60
                if seconds < 10:
                    seconds = '0' + str(seconds)
                bookmarks.append({'tstamp': item['tstamp']['value'], 'bmtext': item['bmtext']['value'], 'minutes': minutes, 'sec': seconds}) # Bookmarkos sakrāta informācija par tstamp un bmtext

        metaitems = []
        problemYear = "NA"
        country = "NA"
        olympiad = "NA"
        problemBook = "NA"
        problemBookSection = "NA"
        problemGrade = "NA"
        problem_number = "NA"
        methodIdentifier = "NA"
        topicIdentifier = "NA"
        concepts = "NA"
        questionType = "NA"
        domain = "NA"

        metaitems.append({'key':'problemID','value': problemid})

        if 'problemYear' in data['results']['bindings'][0]:
            problemYear = data['results']['bindings'][0]['problemYear']['value']
        if 'country' in data['results']['bindings'][0]:
            country = data['results']['bindings'][0]['country']['value']
        if 'olympiad' in data['results']['bindings'][0]:
            olympiad = data['results']['bindings'][0]['olympiad']['value']
        if 'problemBook' in data['results']['bindings'][0]:
            problemBook = data['results']['bindings'][0]['problemBook']['value']
        if 'problemBookSection' in data['results']['bindings'][0]:
            problemBookSection = data['results']['bindings'][0]['problemBookSection']['value']
        if 'problemGrade' in data['results']['bindings'][0]:
            problemGrade = data['results']['bindings'][0]['problemGrade']['value']
        if 'problem_number' in data['results']['bindings'][0]:
            problem_number = data['results']['bindings'][0]['problem_number']['value']
        if 'topicIdentifier' in data['results']['bindings'][0]:
            topicIdentifier = data['results']['bindings'][0]['topicIdentifier']['value']
        if 'methodIdentifier' in data['results']['bindings'][0]:
            methodIdentifier = data['results']['bindings'][0]['methodIdentifier']['value']
        if 'concepts' in data['results']['bindings'][0]:
            concepts = data['results']['bindings'][0]['concepts']['value']
        if 'questionType' in data['results']['bindings'][0]:
            questionType = data['results']['bindings'][0]['questionType']['value']
        if 'domain' in data['results']['bindings'][0]:
            domain = data['results']['bindings'][0]['domain']['value']

        if problemYear != 'NA':
            metaitems.append({'key':'year', 'value': problemYear})
            if country != 'NA':
                metaitems.append({'key':'country', 'value': country})
            if olympiad != 'NA':
                metaitems.append({'key': 'olympiad', 'value': olympiad})
            if problemGrade != 'NA':
                metaitems.append({'key': 'grade', 'value': problemGrade})
        else:
            if problemBook != 'NA':
                metaitems.append({'key': 'book', 'value': problemBook})
            if problemBookSection != 'NA':
                metaitems.append({'key': 'section', 'value': problemBookSection})

        all_topics = []
        if problem_number != 'NA':
            metaitems.append({'key': 'num', 'value': problem_number})
        if methodIdentifier != 'NA':
            metaitems.append({'key': 'method', 'value': methodIdentifier})
        if topicIdentifier != 'NA':
            metaitems.append({'key': 'topic', 'value': topicIdentifier})
            all_topics.append(topicIdentifier)
        if concepts != 'NA':
            metaitems.append({'key': 'concepts', 'value': concepts.replace('http://www.dudajevagatve.lv/eliozo#TRM-','')})
        if questionType != 'NA':
            metaitems.append({'key': 'questionType', 'value': questionType})
        if domain in ['Alg', 'Comb', 'Geom', 'NT']:
            all_domains = {"Alg":"Algebra", "Comb":"Kombinatorika", "Geom":"Ģeometrija", "NT":"Skaitļu teorija"}
            metaitems.append({'key': 'domain', 'value': all_domains[domain]})

        unique_sorted_topics = list(sorted(set(all_topics)))
        print("---------------------")
        print(f'unique_sorted_topics = {unique_sorted_topics}')
        print("=====================")

        template_context = {
            'problemid': problemid,
            'data': data['results']['bindings'],
            'topics': unique_sorted_topics,
            'problemTextHtml': problemTextHtml,
            'hasVideo': hasVideo,
            'video_title': video_title,
            'bookmarks': bookmarks,
            'youtubeID': youtubeID,
            'hasSolution': hasSolution,
            'active': 'archive',
            'lang': session.get('lang', 'lv'),
            'title': 'Uzdevums',
            'metaitems': metaitems
        }
        return render_template('problem_content.html', **template_context)


    @app.route('/problem_solution', methods=['GET','POST'])
    def getProblemSolution():
        problemid = request.args.get('problemid')
        lang = session.get('lang', 'lv')
        # lang = 'lv'
        data = json.loads(getSPARQLProblemSolutions(problemid, lang))

        problemTextHtml = data['results']['bindings'][0]['problemTextHtml']['value']
        problemTextHtml = fix_image_links(problemTextHtml)
        problemTextHtml = mathBeautify(problemTextHtml)

        solutionsHtml = []
        for item in data['results']['bindings']:
            if 'solutionTextHtml' in item:
                solutionTextHtml = item['solutionTextHtml']['value']
                solutionTextHtml = fix_image_links(solutionTextHtml)
                solutionTextHtml = mathBeautify(solutionTextHtml)
                solutionsHtml.append(solutionTextHtml)

        template_context = {
            'problemid': problemid,
            'data': data['results']['bindings'],
            'problemTextHtml': problemTextHtml,
            'solutionsHtml': solutionsHtml,
            'active': 'archive',
            'lang': session.get('lang', 'lv'),
            'title': 'Uzdevums'
        }
        return render_template('problem_solution_content.html', **template_context)


    @app.route('/archive', methods=['GET', 'POST'])
    def getArchive():
        lang = session.get('lang', 'lv')
        olympiads = json.loads(getSPARQLOlympiads(lang))
        olympiadData = []
        for rr in olympiads['results']['bindings']:
            olympiadName = rr['olympiadName']['value']
            olympiadDescription = rr['olympiadDescription']['value']
            olympiadCode = rr['olympiadCode']['value']

            country = ''
            if 'olympiadCountry' in rr:
                country = rr['olympiadCountry']['value']
                #if olympiadCountry.find('#') >= 0:
                #    country = olympiadCountry[olympiadCountry.find('#')+1:]

            if olympiadCode not in ['AMO', 'NOL', 'SOL', 'VOL', 'IMOSHL']:
                continue

            olympiadEvents = []
            eventData = json.loads(getSPARQLOlympiadTimeIDs(country, olympiadCode))
            for event in eventData['results']['bindings']:
                timeID = event['problemTimeID']['value']
                isComplete = True
                # if country == 'LV' and olympiadCode in ['AMO', 'NOL', 'SOL', 'VOL']:
                #     year = int(timeID[0:4])
                #     if year >= 2004:
                #         isComplete = True
                #     if olympiadCode == 'VOL' and year == 2004:
                #         isComplete = False
                olympiadEvents.append((timeID, isComplete))


            olympiadData.append({'olympiadName': olympiadName,
                                 'olympiadDescription': olympiadDescription,
                                 'olympiadCountry':country,
                                 'olympiadCode': olympiadCode,
                                 'olympiadEvents': olympiadEvents})

        template_context = {
            'links': olympiadData,
            'active': 'archive',
            'navlinks': [
                {'url':'getArchive', 'title':'Archive'}
            ],
            'lang': session.get('lang', 'lv'),
            'title': 'Arhīvs'
        }

        return render_template('archive_content.html', **template_context)

    @app.route('/olympiad', methods=['GET', 'POST'])
    def getOlympiad():
        country_id = request.args.get('country_id')
        olympiad_id= request.args.get('olympiad_id')
        olympiads = json.loads(getSPARQLOlympiadTimeIDsGrades(country_id, olympiad_id))

        all_events = []
        all_grades = dict()

        current_event = "NA"

        for item in olympiads['results']['bindings']:
            timeID = item['problemTimeID']['value']
            if timeID != current_event:
                all_events.append(timeID) # Pievienojam jaunu gadu sarakstam all_years
                current_event = timeID # Atceramies pēdējo pievienoto vērtību, lai neiespraustu atkārtoti
                all_grades[current_event] = ['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'] # Sagatavojamies pievienot visas klases
            grade = int(item['grade']['value'])
            all_grades[current_event][grade-5] = item['grade']['value'] # 0. 5.klase, 1. 6.klase utt.

        template_context = {
            'all_events': all_events,
            'all_grades': all_grades,
            'country_id': country_id,
            'olympiad_id': olympiad_id,
            'active': 'archive',
            'lang': session.get('lang', 'lv'),
            'title': 'Olimpiāde'
        }
        return render_template('olympiad_content.html', **template_context)


    @app.route('/curriculum', methods=['GET', 'POST'])
    def getCurriculum(): 
        lang = session.get('lang', 'lv')
        olympiad_id = request.args.get('olympiad')
        minyear = int(request.args.get('minyear'))
        maxyear = int(request.args.get('maxyear'))
        mingrade = int(request.args.get('mingrade'))
        maxgrade = int(request.args.get('maxgrade'))


        # data_qtypes = 

        domains=('Alg', 'Comb', 'Geom', 'NT')
        domains = list(domains)
        # matrix[questionType][domain] -> count, default 0
        matrix = defaultdict(lambda: {d: 0 for d in domains})
        qtypes = set()
        data_qtypes = json.loads(getSPARQLCurriculumQtypeStats(olympiad_id, (mingrade, maxgrade), (minyear, maxyear)))

        for b in data_qtypes["results"]["bindings"]:
            d = b["domain"]["value"]
            qt = b["questionType"]["value"]
            # skip unexpected domains
            if d not in domains:
                continue
            cnt = int(b["count"]["value"])
            matrix[qt][d] = cnt
            qtypes.add(qt)

        question_types = sorted(qtypes)
        # return domains, question_types, matrix

        data = json.loads(getSPARQLOlympiadOverview(olympiad_id, (mingrade, maxgrade), (minyear, maxyear)))

        all_domains = [
            {"name": "Algebra", "prefix": "1."},
            {"name": "Combinatorics", "prefix": "2."},
            {"name": "Geometry", "prefix": "3."},
            {"name": "Number theory", "prefix": "4."},
        ]
        all_topics = []
        all_topics_info = dict()

        current_topic = "NA"

        for item in data['results']['bindings']:
            if item['topicID']['value'] != current_topic:
                current_problem_id = item['problemID']['value']
                current_topic = item['topicID']['value']
                current_topic_number = item['topicNumber']['value']
                current_topic_name = item['topicName']['value']
                current_topic_description = mathBeautify(item['topicDescription']['value'])
                all_topics.append(current_topic)
                all_topics_info[current_topic] = {
                    'topicNumber': current_topic_number,
                    'topicName': current_topic_name,
                    'topicDescription': current_topic_description 
                }
                all_topics_info[current_topic]['problems'] = [current_problem_id]
            else:
                current_problem_id = item['problemID']['value']
                all_topics_info[current_topic]['problems'].append(current_problem_id)

        data_methods = json.loads(getSPARQLCurriculumMethods(olympiad_id, (mingrade, maxgrade), (minyear, maxyear)))
        
        all_methods = []
        all_methods_info = dict()
        current_method = "NA"

        for item in data_methods['results']['bindings']:
            if item['methodID']['value'] != current_method:
                current_problem_id = item['problemID']['value']
                current_method = item['methodID']['value']
                current_method_number = item['methodNumber']['value']
                current_method_name = item['methodName']['value']
                current_method_description = mathBeautify(item['methodDescription']['value'])
                all_methods.append(current_method)
                all_methods_info[current_method] = {
                    'methodNumber': current_method_number,
                    'methodName': current_method_name,
                    'methodDescription': current_method_description 
                }
                all_methods_info[current_method]['problems'] = [current_problem_id]
            else:
                current_problem_id = item['problemID']['value']
                all_methods_info[current_method]['problems'].append(current_problem_id)


        template_context = {
            'olympiad_id': olympiad_id, 
            'minyear': minyear, 
            'maxyear': maxyear,
            'mingrade': mingrade, 
            'maxgrade': maxgrade, 
            'all_topics': all_topics,
            'all_topics_info': all_topics_info,
            'all_domains': all_domains,
            'all_methods': all_methods,
            'all_methods_info': all_methods_info,
            'active': 'statistics',

            'domains': domains, 
            'question_types': question_types, 
            'matrix': matrix,


            'navlinks': [
                {'title':'Reports'}, 
                {'url':'getCurriculum', 'title':'Olimpiad Curriculum'}
            ]
        }

        return render_template('curriculum_content.html', **template_context)

    @app.route('/problem_counts', methods=['GET', 'POST'])
    def getProblemCounts():
        olympiads = ['LV.SOL', 'LV.NOL', 'LV.VOL', 'LV.AMO']
                     
                    #  , 'LV.TST', 
                    #  'LT.LJMO', 'LT.SAV', 'LT.LMMO', 'LT.LKMMO', 'LT.LDK', 'LT.VUMIF', 'LT.TST',
                    #  'EE.PK', 'EE.LO', 'EE.LHT', 'EE.TST']
        
        x = getSPARQLProblemCounts()
        probCounts = json.loads(x)

        all_counts = dict()
        for item in probCounts['results']['bindings']:
            country = item['country']['value']
            code = item['code']['value']
            olympiadName = item['olympiadName']['value']
            entered = int(item['ProblemCount']['value'])
            all_counts[f'{country}.{code}'] = {'lv':olympiadName, 'entered': entered, 'solved': 0}


        x = getSPARQLProblemSolvedCounts()
        probSolvedCounts = json.loads(x)
        for item in probSolvedCounts['results']['bindings']:
            country = item['country']['value']
            code = item['code']['value']
            solved = int(item['ProblemCount']['value'])
            all_counts[f'{country}.{code}']['solved'] = solved

        # all_counts = {'LV.NOL': {'lv':'Latvijas Novada olimpiāde', 'entered': 100, 'solved': 28}, 
        #               'LV.VOL': {'lv':'Latvijas Valsts olimpiāde', 'entered': 101, 'solved': 39}, 
        #               'LV.AMO': {'lv':'Latvijas atklātā olimpiāde', 'entered': 102, 'solved': 49},
        #               'LT.LJKMO': {'lv':'Lietuvas jaunāko klašu olimpiāde', 'entered': 103, 'solved': 25}}

        print('------------------')
        print(f'all_counts = {all_counts}')
        print('==================')

        template_context = {
            'olympiads': olympiads,
            'all_counts': all_counts,
            'active': 'statistics',
            'navlinks': [
                {'title':'Statistics'}, 
                {'url':'getProblemCounts', 'title':'Problem Count'}
            ],
            'lang': session.get('lang', 'lv'),
            'title': 'Problem Count'
        }

        return render_template('stats_problemcounts.html', **template_context)


    @app.route('/results', methods=['GET', 'POST'])
    def getResults():
        template_context = {
            'active': 'statistics',
            'navlinks': [
                {'title':'Statistics'}, 
                {'url':'getResults', 'title':'Result Summary'}
            ],
            'lang': session.get('lang', 'lv'),
            'title': 'Result Summary'
        }

        return render_template('stats_results.html', **template_context)


    @app.route("/video")
    def getVideo():
        data = json.loads(getAllSPARQLVideos())

        all_problemids = []

        for item in data['results']['bindings']:
            problemID = item['problemid']['value']
            text = item['text']['value']
            text = text.replace("$$", "$")
            text = text[:80]
            # text = mathBeautify(text)
            textHtml = item['textHtml']['value']
            all_problemids.append({'problemID': problemID, 'text': text, 'textHtml': textHtml})

        template_context = {
            'all_problemids' : all_problemids,
            'active': 'statistics',
            'navlinks': [
                {'title':'Statistics'}, 
                {'url':'getVideo', 'title':'Video'}
            ],
            'lang': session.get('lang', 'lv'),
            'title': 'Video'
        }

        return render_template('video_content.html', **template_context)


    app.route("/worksheets")(getWorksheets)


    @app.route('/temp_langswitch', methods=['GET', 'POST'])
    def getTempLangswitch():
        current_problem = { 
            "en": """<p>There are $2023$ boxes, initially containing $1, 2, 3, \\ldots, 2023$ candies respectively. \nIn a single move, you may choose a natural number $n$ and eat $n$ candies from some boxes \n(possibly only from one). What is the smallest number of moves needed to make all boxes empty?</p>""", 
            "lv": """<p>Dotas $2023$ kastes, sākumā tajās ir attiecīgi $1, 2, 3, \\ldots, 2023$ \nkonfektes. Vienā gājienā var izvēlēties naturālu skaitli $n$ un no \ndažām kastēm (varbūt tikai no vienas) apēst $n$ konfektes. \nKāds ir mazākais gājienu skaits, ar kuru var panākt, \nka visas kastes ir tukšas?</p>"""
        }
        template_context = {
            'current_problem': current_problem
        }
        return render_template('temp_langswitch_template.html', **template_context)


#year, country, grade, olympiad
    @app.route('/grade', methods=['GET', 'POST'])
    def getGrades():
        lang = session.get('lang', 'lv')
        # lang = 'lv'
        event = request.args.get('event')
        country = request.args.get('country')
        grade = request.args.get('grade')
        olympiad= request.args.get('olympiad')
        if grade == '-1':
            link = json.loads(getSPARQLOlympiadProblemsByEvent(event, country, olympiad, lang))
        else:
            link = json.loads(getSPARQLOlympiadProblemsByEventAndGrade(event, country, grade, olympiad, lang))

        problems = []
        
        for item in link['results']['bindings']:
            problem_id_value = item['problemid']['value']
            problem_number_value = item['problem_number']['value']
            if grade == -1:
                problem_grade_value = item['problem_grade']['value']
            else:
                problem_grade_value = grade
            problem_text_value = item['text']['value']
            problem_text_value = fix_image_links(problem_text_value)
            problem_text_value = mathBeautify(problem_text_value)
            d = {'problemid': problem_id_value, 'problem_number':problem_number_value, 'text': problem_text_value, 'problem_grade': problem_grade_value}
            problems.append(d)


        template_context = {
            'problems': problems,
            'event': event,
            'country': country,
            'grade': grade,
            'olympiad': olympiad,
            'active': 'archive',
            'navlinks': [
                {
                    'url': 'getArchive', 
                    'title': 'Archive'
                }, 
                {
                    'url': 'getGrades', 
                    'params': {
                        'event': event, 
                        'country': country, 
                        'grade': grade, 
                        'olympiad': olympiad
                    },
                    'title': f'{country}.{olympiad}.{event}'
                }
            ],
            'lang': session.get('lang', 'lv'),
            'title': f'{country}.{olympiad}.{event}'
        }

        return render_template('grade_content.html', **template_context)

    @app.route('/login')
    def login():
        redirect_uri_for_callback = url_for('auth_callback', _external=True)
        return oauth.google.authorize_redirect(redirect_uri_for_callback)

    # @app.route('/auth/callback')
    # def auth_callback():
    #     token = oauth.google.authorize_access_token()
    #     user_info = oauth.google.parse_id_token(token)
    #     return redirect(url_for('dashboard'))

    @app.route('/auth/callback')
    def auth_callback():
        # This function now exchanges the code for a token AND parses the ID token
        token = oauth.google.authorize_access_token()
        
        # The user info is now automatically inside the 'userinfo' key
        user_info = token.get('userinfo')
        
        # Optional: Print to logs to see what you got
        if user_info:
            print(f"User Email: {user_info.get('email')}")
            
        return redirect(url_for('dashboard'))
    


    @app.route('/logout')
    def logout():
        session.clear()
        return redirect(url_for('index'))

    @app.route('/dashboard')
    def dashboard():
        if 'user' not in session:
            return redirect(url_for('login'))
        return render_template('dashboard.html', user=session['user'])

    # register the database commands

    from eliozo import db
    
    db.init_app(app)

    app.wsgi_app = DispatcherMiddleware(
        Response('Not Found', status=404),
        {'/eliozo': app.wsgi_app}
    )

    # Use the custom_gettext function in templates
    app.jinja_env.globals.update(_=custom_gettext)

    return app


