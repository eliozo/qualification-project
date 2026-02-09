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

from blueprints.curriculum import curriculum_bp
from blueprints.problems import problems_bp
from blueprints.indexes import indexes_bp
from blueprints.stats import stats_bp
from blueprints.references import references_bp
from blueprints.search import search_bp
from blueprints.worksheets import worksheets_bp
from blueprints.filter import filter_bp
from .navigation import get_navigation

import logging
from flask_babel import Babel, gettext as original_gettext

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

from eliozo_dao import FUSEKI_URL


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

    # Register Google OAuth client
    oauth.register(
        name='google',
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
    app.register_blueprint(worksheets_bp)
    app.register_blueprint(filter_bp)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404



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
            if 'problem_number' in item:
                problem_number_value = item['problem_number']['value']
            else:
                problem_number_value = ''
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


