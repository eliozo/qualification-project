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

from controllers.worksheets import getWorksheets, worksheet_wizard

from blueprints.curriculum import curriculum_bp
from blueprints.problems import problems_bp
from blueprints.indexes import indexes_bp
from blueprints.stats import stats_bp
from blueprints.references import references_bp
from blueprints.search import search_bp
from .navigation import get_navigation

import logging
from flask_babel import Babel, gettext as original_gettext

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

from eliozo_dao import FUSEKI_URL


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
    app.register_blueprint(indexes_bp)
    app.register_blueprint(stats_bp)
    app.register_blueprint(references_bp)
    app.register_blueprint(search_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    app.route("/worksheets", methods=['GET', 'POST'])(getWorksheets)
    app.route("/worksheets/wizard/step/<int:step_id>", methods=['GET', 'POST'])(worksheet_wizard)



    @app.before_request
    def ensure_clickcount():
        session.setdefault("clickcount", 0)

    @app.context_processor
    def inject_globals():
        return {
            "clickcount": session.get("clickcount", 0),
            # you can inject other common vars too:
            "lang": session.get("lang", "lv"),
            "navigation": get_navigation(),
        }


    @app.route('/setlang')
    def setLanguage():
        lang = request.args.get('lang')
        next_url = request.args.get('next')
        next_url = '/eliozo' + request.args.get('next') if next_url else url_for('search_bp.search_problems')

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


