import os
from flask import Flask, render_template, abort, url_for, json, jsonify, request, session, redirect, send_from_directory
from flask_babel import Babel, _
import json
import html
import requests
import re
from .webmd_utils import fix_image_links, mathBeautify
from eliozo_dao.problem_repository import (
    getSPARQLBook
)
from collections import defaultdict
from authlib.integrations.flask_client import OAuth


from eliozo_dao.sparql_access import SparqlAccess
from controllers.worksheets import getWorksheets, worksheet_wizard
from controllers.search_controller import search_problems
from controllers.stats_controllers import getProblemCounts, getPropertyCounts
from controllers.reference_controllers import getReferences, getContactInfo, getOntology
from blueprints.curriculum import curriculum_bp
from blueprints.problems import problems_bp


import logging
# from babel.support import MissingTranslationError

from flask_babel import Babel, gettext as original_gettext

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response


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


# def getSPARQLProblemCounts():
#     url = FUSEKI_URL
#     query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
# PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

# SELECT ?country ?code ?olympiadName (COUNT(DISTINCT ?problem) AS ?ProblemCount)
# WHERE {
#   ?olympiad eliozo:olympiadName ?olympiadName ;
#             eliozo:olympiadDescription ?olympiadDescription ;
#             eliozo:olympiadCountry ?country ;
#             eliozo:olympiadCode ?code .
#   ?problem rdf:type eliozo:Problem ;
#            eliozo:country ?country ;
#            eliozo:olympiadCode ?code .
#   FILTER (lang(?olympiadName) = "lv")
#             FILTER (lang(?olympiadDescription) = "lv")
# }
# GROUP BY ?country ?code ?olympiadName"""
#     myobj = {'query': query}
#     head = {'Content-Type': 'application/x-www-form-urlencoded'}
#     x = requests.post(url, myobj, head)
#     return x.text


# def getSPARQLProblemSolvedCounts():
#     url = FUSEKI_URL
#     query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
# PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
# PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
# PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

# SELECT ?country ?code ?olympiadName (COUNT(DISTINCT ?problem) AS ?ProblemCount)
# WHERE {
#   ?olympiad eliozo:olympiadName ?olympiadName ;
#             eliozo:olympiadDescription ?olympiadDescription ;
#             eliozo:olympiadCountry ?country ;
#             eliozo:olympiadCode ?code .
#   ?problem rdf:type eliozo:Problem ;
#            eliozo:problemSolution ?soln ;
#            eliozo:country ?country ;
#            eliozo:olympiadCode ?code .
#   FILTER (lang(?olympiadName) = "lv")
#             FILTER (lang(?olympiadDescription) = "lv")
# }
# GROUP BY ?country ?code ?olympiadName"""
#     myobj = {'query': query}
#     head = {'Content-Type': 'application/x-www-form-urlencoded'}
#     x = requests.post(url, myobj, head)
#     return x.text 





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


    from . import db
    db.init_app(app)

    app.register_blueprint(problems_bp)
    
    app.register_blueprint(curriculum_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    app.route("/worksheets", methods=['GET', 'POST'])(getWorksheets)
    app.route("/worksheets/wizard/step/<int:step_id>", methods=['GET', 'POST'])(worksheet_wizard)
    app.route('/problem_counts', methods=['GET', 'POST'])(getProblemCounts)
    app.route('/property_counts', methods=['GET', 'POST'])(getPropertyCounts)
    app.route('/references', methods=['GET'])(getReferences)
    app.route('/contact_info', methods=['GET'])(getContactInfo)
    app.route('/ontology', methods=['GET'])(getOntology)


    @app.before_request
    def ensure_clickcount():
        session.setdefault("clickcount", 0)

    @app.context_processor
    def inject_globals():
        return {
            "clickcount": session.get("clickcount", 0),
            # you can inject other common vars too:
            "lang": session.get("lang", "lv"),
        }


    @app.route('/setlang')
    def setLanguage():
        lang = request.args.get('lang')
        next_url = request.args.get('next')
        next_url = '/eliozo' + request.args.get('next') if next_url else url_for('main')

        if lang == 'lv': 
            session['clickcount'] = session.get('clickcount', 0) + 1
        else: 
            session['clickcount'] = 0

        if lang in LANGUAGES:
            session['lang'] = lang
        else:
            session['lang'] = 'lv'

        return redirect(next_url)

    @app.route('/eliozo/static/eliozo/images/<path:filename>')
    def eliozo_static_images(filename):
        # Return file from $APP_ROOT/eliozo/static/eliozo/images/
        return send_from_directory(STATIC_IMAGE_ROOT, filename)


    app.route('/', endpoint='main')(search_problems)

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
            'title': 'Tēmas',
            'structured_topics': structured_topics
        }

        return render_template('topics_content.html', **template_context)


    @app.route('/methods', methods=['GET', 'POST'])
    def getMethods():
        lang = session.get('lang', 'lv')
        data = json.loads(getSPARQLmethods())

        all_methods = []
        all_methods_info = dict()

        current_method = "NA"

        for item in data['results']['bindings']:
            if item['methodID']['value'] != current_method:
                current_method = item['methodID']['value']
                all_methods.append(current_method)

                current_method_info = dict()

                current_method_info['identifier'] = item['methodID']['value'][4:]
                current_method_info['number'] = item['methodNumber']['value']
                current_method_info['name'] = item['methodName']['value']
                current_method_info['description'] = item['methodDescription']['value']

                if "problemid" in item:
                    current_method_info['problems'] = [item['problemid']['value']]
                else:
                    current_method_info['problems'] = []
                all_methods_info[current_method] = current_method_info
            else:
                current_method_info['problems'].append(item['problemid']['value'])    


        template_context = {
            'active': 'order_by',
            'all_methods': all_methods, 
            'all_methods_info': all_methods_info,
            'navlinks': [
                { 'url': 'getMethods', 'title': 'Methods' }
            ],
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
            'title': 'Grāmata'
        }

        return render_template('book_problems_content.html', **template_context)











    @app.route('/curriculum', methods=['GET', 'POST'])



    @app.route('/results', methods=['GET', 'POST'])
    def getResults():
        template_context = {
            'active': 'statistics',
            'navlinks': [
                {'title':'Statistics'}, 
                {'url':'getResults', 'title':'Result Summary'}
            ],
            'title': 'Result Summary'
        }

        return render_template('stats_results.html', **template_context)





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


