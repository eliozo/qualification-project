import os
from flask import Flask, render_template, abort, url_for, json, jsonify, request, session, redirect
from flask_babel import Babel, _
import json
import html
import requests
import re
from .webmd_utils import fix_image_links

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
def getSPARQLskills():
    ##url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL

    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?skillIdentifier ?skillNumber ?skillDescription ?skillName ?problemid WHERE { 
  ?skill eliozo:skillID ?skillIdentifier .
  ?skill eliozo:skillNumber ?skillNumber .
  ?skill eliozo:skillDescription ?skillDescription .
  ?skill eliozo:skillName ?skillName .
  OPTIONAL {
    ?prob eliozo:topic ?skill ;
          eliozo:problemID ?problemid . 
  }.
} ORDER BY ?skillNumber
    """

    myobj = {'query': queryTemplate }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text


def getSPARQLtopics(root):
    ##url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = {'query': '''PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?topicID ?topicParent ?topicTitle ?topicDesc WHERE {
  ?topic rdf:type eliozo:Topic ; 
         eliozo:topicID ?topicID ; 
         eliozo:topicTitle ?topicTitle ;
  		 eliozo:topicDescription ?topicDesc ;
     	 skos:broader ?topicParent ;''' +
         'skos:broader* {topParent} .'.format(topParent=root) +
'''}'''
    }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

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

    print(x.text)

    return x.text




def getSPARQLProblem(arg, lang):
    url = FUSEKI_URL

    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemTextHtml ?video ?problemYear ?country ?olympiad 
?problemBook ?problemBookSection ?problemGrade ?problem_number
?strategy ?topic ?LTopic ?concepts ?questionType ?domain WHERE {{
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
    ?problem eliozo:topic ?skill .
    ?skill eliozo:skillID ?skillIdentifier .
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
    ?problem eliozo:strategy ?strategy .
  }}  
  OPTIONAL {{
    ?problem eliozo:topic ?topic .
  }}  
  OPTIONAL {{
    ?problem eliozo:LTopic ?LTopic .
  }}  
  OPTIONAL {{
    ?problem eliozo:concepts ?concepts .
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

    print("myobj= {}".format(myobj))

    print(x.text)

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

    myobj = {'query':  queryTemplate.format(problemid=arg, language=lang)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    print("myobj= {}".format(myobj))
    print(x.text)
    return x.text


def getSkillProblemsSPARQL(skillID):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL

    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problem ?problemid ?subskill ?text ?grade
WHERE {{
    ?parent skos:prefLabel '{skill}' .
    ?parent skos:narrower* ?subskill .
    ?problem eliozo:topic ?subskill ;
             eliozo:problemID ?problemid ;
             eliozo:problemTextHtml ?text ;
             eliozo:problemGrade ?grade .
}} ORDER BY ?grade
"""

    myobj = {'query': queryTemplate.format(skill=skillID)}

    head = {'Content-Type': 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getProblemsByKeywordSPARQL(keyword):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = {'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\n'+
    '''SELECT DISTINCT ?problem ?problemid ?text ?grade
WHERE {
    ?problem
             eliozo:problemID ?problemid ;
             eliozo:problemTextHtml ?text .
    OPTIONAL {
        eliozo:problemGrade ?grade .
    }
    FILTER(contains(lcase(?text), "'''+keyword+'''"))
} ORDER BY ?grade ?problemid
  LIMIT 10'''
}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    print(x.text)
    return x.text

def getProblemsByFiltersSPARQL(grade, olympiad, domain, questionType, method, theOffset):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemid ?text ?grade WHERE {{
  ?problem eliozo:problemID ?problemid ;
           {grade}
           {olympiad}
           {domain}
           {questionType}
           {method}
      eliozo:problemTextHtml ?text .
      OPTIONAL {{
        ?problem eliozo:problemGrade ?grade .
      }}
}} ORDER BY ?grade ?problemid LIMIT 10 OFFSET {offset}
"""
    theGrade = "" if grade in ["", "NA"] else f'eliozo:suggestedGrade {grade} ; '
    theOlympiad = "" if olympiad in ["", "NA"] else f'eliozo:olympiadType "{olympiad}" ; '
    theDomain = "" if domain in ["", "NA"] else f'eliozo:domain "{domain}" ; '
    theQuestionType = "" if questionType in ["", "NA"] else f'eliozo:questionType "{questionType}" ; '
    theMethod = "" if method in ["", "NA"] else f'eliozo:LTopic "{method}" ; '

    q = queryTemplate.format(grade=theGrade, olympiad=theOlympiad,
                             domain=theDomain, questionType=theQuestionType,
                             method=theMethod, offset=theOffset)
    print(f"****query = ******'{q}'")
    myobj = {'query': q}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    print(x.text)
    return x.text


def getProblemCountsByFiltersSPARQL(grade, olympiad, domain, questionType, method):
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
           {method} .
}}
"""
    theGrade = '' if grade in ['', 'NA'] else f'eliozo:suggestedGrade {grade} ; '
    theOlympiad = '' if olympiad in ['', 'NA'] else f'eliozo:olympiadType "{olympiad}" ; '
    theDomain = '' if domain in ['', 'NA'] else f'eliozo:domain "{domain}" ; '
    theQuestionType = '' if questionType in ['', 'NA'] else f'eliozo:questionType "{questionType}" ; '
    theMethod = '' if method in ['', 'NA'] else f'eliozo:LTopic "{method}" ; '
    q = queryTemplate.format(grade=theGrade, olympiad=theOlympiad,
                             domain=theDomain, questionType=theQuestionType,
                             method=theMethod)
    print(f"****CountQuery = ******'{q}'")
    myobj = {'query': q}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSkillDetails(skillID):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?skillID ?skillNumber ?skillName ?skillDesc WHERE {{
  ?skill skos:prefLabel '{skill}' ;
      eliozo:skillNumber ?skillNumber ;
      eliozo:skillName ?skillName ;
      eliozo:skillDescription ?skillDesc .
}}
"""

    myobj = {'query': queryTemplate.format(skill=skillID)}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    print(x.text)
    return x.text


def getAllSkillChildren(skillID):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL

    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?skillID ?prefLabel ?num ?skillName WHERE {{
  ?parentskill skos:prefLabel '{skill}' .
  ?skillID skos:broader ?parentskill ;
      skos:prefLabel ?prefLabel ;
      eliozo:skillName ?skillName ;
      eliozo:skillNumber ?num .
}} ORDER BY ?num
"""


    myobj = {'query': queryTemplate.format(skill=skillID)}

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getSPARQLOlympiads():
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL

    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?olympiadCountry ?olympiad ?olympiadCode ?olympiadName ?olympiadDescription WHERE { 
  ?olympiad eliozo:olympiadName ?olympiadName ;
            eliozo:olympiadDescription ?olympiadDescription ;
            eliozo:olympiadCode ?olympiadCode .
  OPTIONAL {
    ?olympiad eliozo:olympiadCountry ?olympiadCountry .
  }
} ORDER BY ?olympiadCountry ?olympiadName
"""


    myobj = { 'query': queryTemplate }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getSPARQLOlympiadYears(country, olympiad):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
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

    # myobj = { 'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    # 'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    # 'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    # 'PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>\n'+
    # 'SELECT DISTINCT ?year ?grade WHERE { ?problem eliozo:country \''+country+
    # '\' ; eliozo:olympiadCode \''+olympiad+
    # '\' ; eliozo:problemYear ?year ; eliozo:problemGrade ?grade . } ORDER BY DESC(?year) ?grade'
    # }

    myobj = {'query': queryTemplate.format(country=country, olympiad=olympiad)}

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getSPARQLOlympiadGrades(year, country, grade, olympiad, lang):
    url = FUSEKI_URL
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?text ?problemid ?problem_number WHERE {{
      ?problem eliozo:problemYear {year} .
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
        queryTemplate.format(year=year, country=country, grade=grade, olympiad_code=olympiad, language=lang)
    }

    print('**********myobj={}'.format(myobj))

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getSPARQLOlympiadYear(year, country, olympiad, lang):
    url = FUSEKI_URL
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
SELECT ?text ?problemid ?problem_number ?problem_grade ?suffix WHERE {{
  ?problem eliozo:problemYear {year} .
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
        queryTemplate.format(year=year, country=country, olympiad_code=olympiad, language=lang)
    }

    print('**********myobj={}'.format(myobj))

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

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

    print(x.text)

    return x.text
              


def getSPARQLVideoBookmarks(problemid):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
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

    print(x.text)

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

    print(x.text)

    return x.text


def mathBeautify(a): # Izskaistina formulas ar MathJax Javascript bibliotēku
    b0 = re.sub(r"\$\$([^\$]+)\$\$", r"<p><span class='math display'>\[\1\]</span></p>", a) # Aizstāj vairākrindu formulas $$..$$
    b = re.sub(r"\$([^\$]+)\$", r"<span class='math inline'>\(\1\)</span>", b0) # Aizstāj inline formulas $...$ (Svarīga secība, kā aizstāj)
    return b


def get_locale():
    locale = session.get('lang', 'lv')
    # print(f"&&&&&& Selected locale: {locale}")
    return locale

# def log_missing_translations(exception, *args, **kwargs):
#     if isinstance(exception, MissingTranslationError):
#         logging.warning(f"Missing translation for: {args[0]}")
#     return exception


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
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    # Configure the available languages
    LANGUAGES = {
        'en': 'English',
        'lv': 'Latvian',
        'lt': 'Lithuanian'
    }
    app.config['BABEL_DEFAULT_LOCALE'] = 'lv'
    app.config['BABEL_TRANSLATION_DIRECTORIES'] = 'translations'
    babel = Babel(app, locale_selector=get_locale)


    # Configure Babel logging for missing translations
    # app.config['BABEL_MISSING_TRANSLATION'] = log_missing_translations

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

    # def fix_image_links(arg):
    #     img_regex1 = r'<img\s+(alt\S*)\s+src="([^"/]*)" />\{ width=([^"]*) \}'
    #     img_replace1 = r'<img \1 style="width:\3" src="https://www.dudajevagatve.lv/static/eliozo/images/\2"/>'
    #     img_regex2 = r'<img\s+(alt\S*)\s+src="([^"/]*)" />'
    #     img_replace2 = r'<img \1 src="https://www.dudajevagatve.lv/static/eliozo/images/\2"/>'
    #     arg = re.sub(img_regex1, img_replace1, arg)
    #     arg = re.sub(img_regex2, img_replace2, arg)
    #     return arg

    @app.route('/setlang')
    def setLanguage():
        lang = request.args.get('lang')
        next_url = request.args.get('next')
        next_url = '/eliozo' + request.args.get('next') if next_url else url_for('main')
        print(f'lang = {lang}')
        print(f'next_url = {next_url}')

        if lang in LANGUAGES:
            session['lang'] = lang
        else:
            session['lang'] = 'lv'

        return redirect(next_url)

    @app.route('/')
    def main():
        keyword = request.args.get('keyword')
        if keyword is None or keyword == "":
            template_context = {
                'active': 'main',
                'lang': session.get('lang', 'lv')
            }
            return render_template('main_content.html',  **template_context)
        new_keyword = replace_non_ascii_with_unicode_escape(keyword)
        link = json.loads(getProblemsByKeywordSPARQL(new_keyword))

        problems = []
        
        for item in link['results']['bindings']:
            problem_id_value = item['problemid']['value']
            problem_imagefile = ''
            if 'imagefile' in item:
                problem_imagefile = item['imagefile']['value']
            problem_text_value = mathBeautify(item['text']['value'])
            d = {'problemid': problem_id_value, 'text': problem_text_value, 'imagefile': problem_imagefile}
            problems.append(d)


        template_context = {
            'problems': problems,
            'keyword' : keyword,
            'active': 'main',
            'lang': session.get('lang', 'lv'),
            'title': 'Sākumlapa'
        }

        return render_template('main_content.html', **template_context)

    # faceted browse
    @app.route('/filter')
    def getFilter():
        grade = request.args.get('grade')
        if grade is None:
            grade = "NA"
        olympiad = request.args.get('olympiad')
        if olympiad is None:
            olympiad = "NA"
        domain = request.args.get('domain')
        if domain is None:
            domain = "NA"
        questionType = request.args.get('questionType')
        if questionType is None:
            questionType = "NA"
        method = request.args.get('method')
        if method is None:
            method = "NA"
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
                            ('International', {'en':'International', 'lt':'Tarptautinė', 'lv':'Starptautiska'})]

        methodDict = [('LTInduction', {'en':'Induction', 'lt':'Indukcija', 'lv':'Indukcija'}),
                      ('LTMeanValuePrinciple', {'en':'MeanValue', 'lt':'Vidutinė Vertė', 'lv':'Vid.Vērtība'}),
                      ('LTExtremeElement', {'en':'Extreme element','lt':'Kraštinis Elementas', 'lv':'Ekstr.Elements'}),
                      ('LTInvariant', {'en':'Invariant','lt':'Invariantas', 'lv':'Invariants'}),
                      ('LTContradiction', {'en':'Contradiction', 'lt':'Prieštaravimas', 'lv': 'Pretruna'}),
                      ('LTInterpretation', {'en':'Interpretation', 'lt': 'Interpretacija', 'lv':'Interpretācija'}),
                      ('LTExpressionTransforms', {'en':'Transforms', 'lt':'Pertvarkymai', 'lv':'Pārveidojumi'}),
                      ('LTStructureAugmentation', {'en':'Structure augmentation', 'lt':'Pagalbinės Konstrukcijos', 'lv':'Papildkonstrukcijas'}),
                      ('', {'en':'Unspecified', 'lt':'Nežinomas', 'lv':'Nenorādīta'})]

        if grade == "NA" and olympiad == "NA" and  domain == "NA" and questionType == "NA" and method == "NA":
            template_context = {
                'problems': problems,
                'active': 'filter',
                'lang': session.get('lang', 'lv'),
                'olympiadTypeDict': olympiadTypeDict,
                'methodDict': methodDict,
                'title': 'Filtri'
            }
            return render_template('filter_content.html', **template_context)

        else:
            print(f"***Grade IS @{grade}@**")
            link = json.loads(getProblemsByFiltersSPARQL(grade, olympiad, domain, questionType, method, offset))
            for item in link['results']['bindings']:
                problem_id_value = item['problemid']['value']
                # problem_imagefile = ''
                # if 'imagefile' in item:
                #     problem_imagefile = item['imagefile']['value']
                problem_text_value = mathBeautify(item['text']['value'])
                problem_text_value = fix_image_links(problem_text_value)
                d = {'problemid': problem_id_value, 'text': problem_text_value}
                problems.append(d)


            all_grades = ['5', '6', '7', '8', '9', '10', '11', '12']
            grade_counts = dict()
            for curr_grade in all_grades:
                count_json = json.loads(getProblemCountsByFiltersSPARQL(curr_grade, olympiad, domain, questionType, method))
                grade_counts[curr_grade] = count_json['results']['bindings'][0]['count']['value']

            all_olympiads = ['Contest', 'Book', 'RegionalOrOpen', 'National', 'TeamSelection', 'International']
            olympiad_counts = dict()
            for curr_olympiad in all_olympiads:
                count_json = json.loads(getProblemCountsByFiltersSPARQL(grade, curr_olympiad, domain, questionType, method))
                olympiad_counts[curr_olympiad] = count_json['results']['bindings'][0]['count']['value']

            all_domains = ['Alg', 'Comb', 'Geom', 'NT', '']
            domain_counts = dict()
            for curr_domain in all_domains:
                count_json = json.loads(getProblemCountsByFiltersSPARQL(grade, olympiad, curr_domain, questionType, method))
                domain_counts[curr_domain] = count_json['results']['bindings'][0]['count']['value']


            all_questionTypes = ['FindAll', 'FindCount', 'FindOptimal', 'FindExample', 'Prove', 'ProveDisprove', 'Algorithm']
            questionType_counts = dict()
            for curr_questionType in all_questionTypes:
                count_json = json.loads(getProblemCountsByFiltersSPARQL(grade, olympiad, domain, curr_questionType, method))
                questionType_counts[curr_questionType] = count_json['results']['bindings'][0]['count']['value']

            #                 {% for (val,lbl) in [('LTInduction','Indukcija'), ('LTMeanValuePrinciple','Vid.Vērtība'),
            #                 ('LTExtremeElement', 'Ekstr.Elements'),('LTInvariant', 'Invariants'),
            #                 ('LTContradiction', 'Pretruna'),('LTInterpretation','Interpretācijas'),
            #                 ('LTExpressionTransforms','Pārveidojumi'),('LTStructureAugmentation','Papildkonstrukcijas'),
            #                 ('', 'Jebkāda')] %}
            all_methods = ['LTInduction', 'LTMeanValuePrinciple', 'LTExtremeElement', 'LTInvariant',
                           'LTContradiction', 'LTInterpretation', 'LTExpressionTransforms', 'LTStructureAugmentation', '']
            method_counts = dict()
            for curr_method in all_methods:
                count_json = json.loads(
                    getProblemCountsByFiltersSPARQL(grade, olympiad, domain, questionType, curr_method))
                method_counts[curr_method] = count_json['results']['bindings'][0]['count']['value']

            if domain not in domain_counts:
                domain = ''
            page_offsets = []
            print(f'domain_counts = {int(domain_counts[domain])}')
            if int(domain_counts[domain]) > 10:
                current_offset = 0
                while int(domain_counts[domain]) - current_offset > 0:
                    page_offsets.append(current_offset)
                    current_offset += 10

            print(f'page_offsets = {len(page_offsets)}')
            template_context = {
                'problems': problems,
                'grade': grade,
                'olympiad': olympiad,
                'domain': domain,
                'questionType': questionType,
                'method': method,
                'grade_counts': grade_counts,
                'olympiad_counts': olympiad_counts,
                'domain_counts': domain_counts,
                'questionType_counts': questionType_counts,
                'method_counts': method_counts,
                'olympiadTypeDict': olympiadTypeDict,
                'methodDict': methodDict,
                'page_offsets': page_offsets,
                'myoffset': offset,
                'active': 'filter',
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
        template_context = {
            'active': 'references',
            'lang': session.get('lang', 'lv'),
            'title': 'Atsauces'
        }
        return render_template('references_content.html', **template_context)


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
            'active': 'video',
            'lang': session.get('lang', 'lv'),
            'title': 'Video'
        }

        # problemid = request.args.get('problemid')

        # problemid = "LV.AO.2011.5.1"

        # data = json.loads(getSPARQLVideoBookmarks(problemid))

        # bookmarks = []
        # video_title = "NA"
        # youtubeID = "NA"

        # for item in data['results']['bindings']:
        #     video_title = item['videoTitle']['value']
        #     youtubeID = item['youtubeID']['value']
        #     minutes = int(item['tstamp']['value']) // 60
        #     if minutes < 10:
        #         minutes = '0' + str(minutes)
        #     seconds = int(item['tstamp']['value']) % 60
        #     if seconds < 10:
        #         seconds = '0' + str(seconds)
        #     bookmarks.append({'tstamp': item['tstamp']['value'], 'bmtext': item['bmtext']['value'], 'minutes': minutes, 'sec': seconds}) # Bookmarkos sakrāta informācija par tstamp un bmtext

        # template_context = {
        #     'video_title': video_title,
        #     'bookmarks': bookmarks,
        #     'youtubeID': youtubeID,
        # }

        return render_template('video_content.html', **template_context)

    @app.route('/topics', methods=['GET','POST'])
    def getTopics():
        data = json.loads(getSPARQLskills())

        all_skills = []
        all_skill_info = dict() # Vārdnīca visai prasmju tabulai

        current_skill = "NA"

        for item in data['results']['bindings']:
            # A new skill appears
            if item['skillIdentifier']['value'] != current_skill:
                all_skills.append(item['skillIdentifier']['value']) # Pievienojam jaunu prasmi sarakstam all_skills
                current_skill = item['skillIdentifier']['value'] # Atceramies pēdējo pievienoto vērtību, lai neiespraustu atkārtoti
                print(f'current_skill = {current_skill}')

                current_skill_info = dict() # Vārdnīca vienai tabulas rindai
                current_skill_info['skillIdentifier'] = current_skill
                current_skill_info['skillNumber'] = item['skillNumber']['value']
                number_items = item['skillNumber']['value'].split(".")
                # current_skill_info['skillIndent'] = '&nbsp;&nbsp;'*(4 - sum([theItem == "0" for theItem in number_items]))

                beautiful_description = mathBeautify(item['skillDescription']['value'])
                current_skill_info['skillDescription'] = beautiful_description
                current_skill_info['skillName'] = mathBeautify(item['skillName']['value'])
                if "problemid" in item:
                    current_skill_info['problems'] = [item['problemid']['value']]
                else:
                    current_skill_info['problems'] = []
                all_skill_info[current_skill] = current_skill_info # Lielajā vārdnīcā iesprauž mazo vārdnīcu
            else:
                current_skill_info['problems'].append(item['problemid']['value']) # Pievieno tikai jauno uzdevuma ID

        # domain_titles = {'1': 'Algebra', '2': 'Kombinatorika', '3': 'Ģeometrija', '4': 'Skaitļu teorija'}
        structured_skills = []
        current_LTopics = None
        current_subtopics = None
        current_subsubtopics = None
        for skill in all_skills:
            skillNumber = all_skill_info[skill]['skillNumber']

            if skillNumber.endswith('.0.0.0.0'):
                LTopics = []
                current_LTopics = LTopics
                L1_number = skillNumber[:-len('.0.0.0.0')]
                L1_name = all_skill_info[skill]['skillName']
                L1_desc = all_skill_info[skill]['skillDescription']
                L1_prob = all_skill_info[skill]['problems']
                structured_skills.append({'number':L1_number,
                                          'name':L1_name,
                                          'desc':L1_desc,
                                          'prob':L1_prob,
                                          'subtopics': LTopics})
            elif skillNumber.endswith('.0.0.0'):
                subtopics = []
                current_subtopics = subtopics
                L2_number = skillNumber[:-len('.0.0.0')]
                L2_label = L2_number.replace('.', '_')
                L2_name = all_skill_info[skill]['skillName']
                L2_desc = all_skill_info[skill]['skillDescription']
                L2_prob = all_skill_info[skill]['problems']
                current_LTopics.append({'number':L2_number,
                                        'label':L2_label,
                                        'name':L2_name,
                                        'desc':L2_desc,
                                        'prob': L2_prob,
                                        'subtopics': subtopics})
            elif skillNumber.endswith('.0.0'):
                subsubtopics = []
                current_subsubtopics = subsubtopics
                L3_number = skillNumber[:-len('.0.0')]
                L3_name = all_skill_info[skill]['skillName']
                L3_desc = all_skill_info[skill]['skillDescription']
                L3_prob = all_skill_info[skill]['problems']
                current_subtopics.append({'number':L3_number,
                                          'name':L3_name,
                                          'desc': L3_desc,
                                          'prob': L3_prob,
                                          'subtopics':subsubtopics})
            else:
                L45_number = skillNumber
                if skillNumber.endswith('.0'):
                    L45_number = skillNumber[:-len('.0')]
                L45_name = all_skill_info[skill]['skillName']
                L45_desc = all_skill_info[skill]['skillDescription']
                L45_prob = all_skill_info[skill]['problems']
                current_subsubtopics.append({'number':L45_number, 'name':L45_name, 'desc': L45_desc, 'prob':L45_prob})

        template_context = {
            'all_skills': all_skills,
            'all_skill_info': all_skill_info,
            'active': 'topics',
            'lang': session.get('lang', 'lv'),
            'title': 'Tēmas',
            'structured_topics': structured_skills
        }

        return render_template('topics_content.html', **template_context)


    @app.route('/concepts', methods=['GET','POST'])
    def getConcepts():

        # all_topics = json.loads(getSPARQLtopics('eliozo:analysis'))
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
            'active': 'concepts',
            'lang': session.get('lang', 'lv'),
            'title': 'Jēdzieni'
        }
        return render_template('concepts_content.html', **template_context)

    @app.route('/topic_tasks', methods=['GET','POST']) # Kontrolieris, kas iegūst prasmes kopā ar uzdevumiem
    def getTopic():
        skill = request.args.get('skillIdentifier')

        skill_details = json.loads(getSkillDetails(skill))
        parentNumber = skill_details['results']['bindings'][0]['skillNumber']['value']
        parentName = skill_details['results']['bindings'][0]['skillName']['value']
        parentDesc = skill_details['results']['bindings'][0]['skillDesc']['value']
        parentDesc = mathBeautify(parentDesc)

        all_skills = json.loads(getAllSkillChildren(skill))
        skill_list = []
        for skill_item in all_skills['results']['bindings']: # all_skills saraksts ar vārdnīcām
            prefLabel = skill_item['prefLabel']['value']
            skillName = skill_item['skillName']['value']
            skillName = mathBeautify(skillName)
            skillNum = skill_item['num']['value']
            dd = {'prefLabel': prefLabel, 'skillNum': skillNum, 'skillName': skillName}
            skill_list.append(dd)

        data = json.loads(getSkillProblemsSPARQL(skill))
        problem_list = []
        for data_item in data['results']['bindings']:
            problemTextHtml = data_item['text']['value']
            problemTextHtml = fix_image_links(problemTextHtml)
            problemTextHtml = mathBeautify(problemTextHtml)
            problem_list.append({'problemid': data_item['problemid']['value'], 'text': problemTextHtml})

        template_context = {
            'skill': skill,
            'parentNumber': parentNumber,
            'parentName': parentName,
            'parentDesc': parentDesc,
            'problem_list': problem_list,
            'skill_list' : skill_list,
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
        problemid = request.args.get('problemid')

        print(f"**************** problemid = {problemid}")
        solnData = json.loads(getSPARQLProblemSolutions(problemid, lang))
        hasSolution = False
        if 'solutionTextHtml' in solnData['results']['bindings'][0]:
            hasSolution = True


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

        # metaitems = [
        #     {'key':'olympiad', 'value': 'AMO'},
        #     {'key':'country', 'value':'EEFF'},
        #     {'key':'grade', 'value': '10'},
        #     {'key':'problemID','value': 'LV.AMO.2000.10.2'}
        # ]

        metaitems = []
        problemYear = "NA"
        country = "NA"
        olympiad = "NA"
        problemBook = "NA"
        problemBookSection = "NA"
        problemGrade = "NA"
        problem_number = "NA"
        problemStrategy = "NA"
        LTopic = "NA"
        topic = "NA"
        strategy = "NA"
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

        if 'strategy' in data['results']['bindings'][0]:
            strategy = data['results']['bindings'][0]['strategy']['value']
        if 'topic' in data['results']['bindings'][0]:
            topic = data['results']['bindings'][0]['topic']['value']
        if 'LTopic' in data['results']['bindings'][0]:
            LTopic = data['results']['bindings'][0]['LTopic']['value']
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

        if problem_number != 'NA':
            metaitems.append({'key': 'num', 'value': problem_number})
        if LTopic != 'NA':
            metaitems.append({'key': 'LTopic', 'value': LTopic})
        if topic != 'NA':
            metaitems.append({'key': 'topic', 'value': topic.replace('http://www.dudajevagatve.lv/eliozo#', '')})
        if strategy != 'NA':
            metaitems.append({'key': 'strategy', 'value': strategy})
        if concepts != 'NA':
            metaitems.append({'key': 'concepts', 'value': concepts.replace('http://www.dudajevagatve.lv/eliozo#TRM-','')})
        if questionType != 'NA':
            metaitems.append({'key': 'questionType', 'value': questionType})
        if domain in ['Alg', 'Comb', 'Geom', 'NT']:
            all_domains = {"Alg":"Algebra", "Comb":"Kombinatorika", "Geom":"Ģeometrija", "NT":"Skaitļu teorija"}
            metaitems.append({'key': 'domain', 'value': all_domains[domain]})

        template_context = {
            'problemid': problemid,
            'data': data['results']['bindings'],
            'problemTextHtml': problemTextHtml,
            'hasVideo': hasVideo,
            'video_title': video_title,
            'bookmarks': bookmarks,
            'youtubeID': youtubeID,
            # 'solutionTextHtml': solutionTextHtml,
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

        print(f"**************** problemid = {problemid}")
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
        olympiads = json.loads(getSPARQLOlympiads())
        print(olympiads)
        olympiadData = []
        for rr in olympiads['results']['bindings']:
            olympiadName = rr['olympiadName']['value']
            olympiadDescription = rr['olympiadDescription']['value']
            olympiadCode = rr['olympiadCode']['value']

            country = ''
            if 'olympiadCountry' in rr:
                olympiadCountry = rr['olympiadCountry']['value']
                if olympiadCountry.find('#') >= 0:
                    country = olympiadCountry[olympiadCountry.find('#')+1:]
            # olyString = rr['olympiad']['value'].split("#")[-1]
            # print(f'olyString={olyString}')
            # (olympiadCountry,olympiadCode) = olyString.split(".")
            olympiadData.append({'olympiadName': olympiadName, 'olympiadDescription': olympiadDescription, 'olympiadCountry':country, 'olympiadCode': olympiadCode})

        template_context = {
            'links': olympiadData,
            'active': 'archive',
            'lang': session.get('lang', 'lv'),
            'title': 'Arhīvs'
        }

        return render_template('archive_content.html', **template_context)

    @app.route('/olympiad', methods=['GET', 'POST'])
    def getOlympiad():
        country_id = request.args.get('country_id')
        olympiad_id= request.args.get('olympiad_id')

        # Sākas datu piekļuve (Modelis)
        x = getSPARQLOlympiadYears(country_id, olympiad_id)
        print(x)
        olympiads = json.loads(x)


        all_years = []
        all_grades = dict()

        current_year = "NA"

        for item in olympiads['results']['bindings']:
            if item['year']['value'] != current_year:
                all_years.append(item['year']['value']) # Pievienojam jaunu gadu sarakstam all_years
                current_year = item['year']['value'] # Atceramies pēdējo pievienoto vērtību, lai neiespraustu atkārtoti
                all_grades[current_year] = ['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'] # Sagatavojamies pievienot visas klases
            grade = int(item['grade']['value'])
            all_grades[current_year][grade-5] = item['grade']['value'] # 0. 5.klase, 1. 6.klase utt.

        # Kontrolieris izlemj, kādus datus sūtīs klientam, saliek tos vārdnīcā
        template_context = {
            'all_years': all_years,
            'all_grades': all_grades,
            'country_id': country_id,
            'olympiad_id': olympiad_id,
            'active': 'archive',
            'lang': session.get('lang', 'lv'),
            'title': 'Olimpiāde'
        }
        # Kontrolieris izlemj, uz kuru skatu sūtīs klientu
        return render_template('olympiad_content.html', **template_context)

#year, country, grade, olympiad
    @app.route('/grade', methods=['GET', 'POST'])
    def getGrades():
        lang = session.get('lang', 'lv')
        year = request.args.get('year')
        country = request.args.get('country')
        grade = request.args.get('grade')
        olympiad= request.args.get('olympiad')
        print('Gads = {}, country - {}, grade = {}, olympiad = {}'.format(year,country,grade,olympiad))

        if grade == '-1':
            link = json.loads(getSPARQLOlympiadYear(year, country, olympiad, lang))
        else:
            link = json.loads(getSPARQLOlympiadGrades(year,country,grade,olympiad, lang))

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
            'year': year,
            'country': country,
            'grade': grade,
            'olympiad': olympiad,
            'active': 'archive',
            'lang': session.get('lang', 'lv'),
            'title': 'Klase'
        }

        return render_template('grade_content.html', **template_context)

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


