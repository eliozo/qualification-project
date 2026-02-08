import requests
import json
from . import FUSEKI_URL

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
      OPTIONAL {{ ?problem eliozo:problemSuffix ?suffix . }}
    }} ORDER BY ?problem_number
    """
    myobj = { 'query': queryTemplate.format(event=event, country=country, olympiad_code=olympiad) }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
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
    }} ORDER BY ?problem_number
    """
    myobj = { 'query': queryTemplate.format(event=event, country=country, grade=grade, olympiad_code=olympiad) }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLProblem(arg, lang):
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemTextHtml ?problemYear ?country ?olympiad 
           ?problemGrade ?problemBook ?problemBookSection 
           ?problem_number ?topicIdentifier ?methodIdentifier 
           ?concepts ?questionType ?domain ?video 
           WHERE {{
      ?problem eliozo:problemID '{problemID}' ;
               eliozo:problemTextHtml ?problemTextHtml .
      OPTIONAL {{ ?problem eliozo:problemYear ?problemYear . }}
      OPTIONAL {{ ?problem eliozo:country ?country . }}
      OPTIONAL {{ ?problem eliozo:olympiad ?olympiad . }}
      OPTIONAL {{ ?problem eliozo:problemGrade ?problemGrade . }}
      OPTIONAL {{ ?problem eliozo:problemBook ?problemBook . }}
      OPTIONAL {{ ?problem eliozo:problemBookSection ?problemBookSection . }}
      OPTIONAL {{ ?problem eliozo:problem_number ?problem_number . }}
      OPTIONAL {{ ?problem eliozo:topic ?topic . ?topic eliozo:topicIdentifier ?topicIdentifier . }}
      OPTIONAL {{ ?problem eliozo:method ?method . ?method eliozo:methodIdentifier ?methodIdentifier . }}
      OPTIONAL {{ ?problem eliozo:concepts ?concepts . }}
      OPTIONAL {{ ?problem eliozo:questionType ?questionType . }}
      OPTIONAL {{ ?problem eliozo:domain ?domain . }}
      OPTIONAL {{ ?problem eliozo:hasVideo ?video . }}
    }}
    """
    myobj = {'query': queryTemplate.format(problemID=arg)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLProblemSolutions(arg, lang):
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemTextHtml ?solutionTextHtml ?solutionID WHERE {{
      ?problem eliozo:problemID '{problemID}' ;
              eliozo:problemTextHtml ?problemTextHtml .
      OPTIONAL {{ 
        ?problem eliozo:problemSolution ?soln . 
        ?soln eliozo:solutionTextHtml ?solutionTextHtml .
        OPTIONAL {{ ?soln eliozo:solutionID ?solutionID . }}
      }}
    }}
    """
    myobj = {'query': queryTemplate.format(problemID=arg)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLVideoBookmarks(arg):
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?youtubeID ?videoTitle ?tstamp ?bmtext WHERE {{
        ?problem eliozo:problemID '{problemID}' .
        ?problem eliozo:hasVideo ?video .
        ?video eliozo:videoTitle ?videoTitle ;
               eliozo:youtubeID ?youtubeID .
        OPTIONAL {{
            ?video eliozo:videoBookmark ?bm .
            ?bm eliozo:bmTime ?tstamp ;
                eliozo:bmText ?bmtext .
        }}
    }}
    ORDER BY ?tstamp
    """
    myobj = {'query': queryTemplate.format(problemID=arg)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getAllSPARQLVideos():
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemid ?text ?textHtml WHERE {
        ?problem eliozo:hasVideo ?video .
        ?problem eliozo:problemID ?problemid .
        ?problem eliozo:problemText ?text .
        ?problem eliozo:problemTextHtml ?textHtml .
    }
    """
    myobj = {'query': queryTemplate}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLBook(bookid, sectionid):
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problem ?text ?imagefile ?problemid WHERE {{
      ?problem eliozo:problemBook '{bookid}' ;
               eliozo:problemBookSection '{sectionid}' ;
               eliozo:problemID ?problemid ;
               eliozo:problemTextHtml ?text .
      OPTIONAL {{ ?problem eliozo:hasImage ?imagefile . }}
    }} ORDER BY ?problemid
    """
    myobj = {'query': queryTemplate.format(bookid=bookid, sectionid=sectionid)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text
