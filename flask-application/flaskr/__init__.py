import os
from flask import Flask, render_template, abort, url_for, json, jsonify, request
import json
import html
import requests
import re

def getSPARQLtopics():

    url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    myobj = {'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eozol: <http://www.dudajevagatve.lv/eozol#>\n'+
    # 'SELECT * WHERE { ?sub eozol:skill ?obj . ?obj skos:prefLabel ?label . } LIMIT 10\n'
    'SELECT * WHERE { ?sub eozol:skill ?obj . } ORDER BY ?sub \n'
    }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x)

    return x.text

def getSkillProblemsSPARQL(skillID):
    url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    myobj = {'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eozol: <http://www.dudajevagatve.lv/eozol#>\n'+
    # 'SELECT ?sub ?text WHERE { ?sub eozol:skill \''+skillID+'\' ; eozol:text ?text . } ORDER BY ?obj '
    'SELECT ?problemid ?text WHERE { ?sub eozol:problemid ?problemid . ?sub eozol:skill \''+skillID+'\' . ?sub eozol:text ?text . } ORDER BY ?problemid'
    }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

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

    @app.route('/')
    def main():
        return render_template('main.html')

    @app.route('/skills')
    def topics():
        return render_template('skills.html')


    # json 
    @app.route("/json")
    def getJson():
        # read file
        with open('C:/Users/eliz_/Documents/qualification-project/flask-application/data/file.json', 'r', encoding="utf-8") as myfile:
            data = myfile.read()
        return render_template('index.html', title="page", jsonfile=json.dumps(data))

    @app.route('/index', methods=['GET','POST'])
    def getIndex():
        data = json.loads(getSPARQLtopics()) 

        template_context = {
            'my_id': 'index',
            'links': data['results']['bindings']
        }
    
        return render_template('index.html', **template_context)

    @app.route('/skill', methods=['GET','POST'])
    def getSkill():
        skill = request.args.get('skillID') 
        data = json.loads(getSkillProblemsSPARQL(skill))
        problem_list = []
        for data_item in data['results']['bindings']:
            a = data_item['text']['value']
            b = re.sub(r"\$([^\$]+)\$", r"<span class='math inline'>\(\1\)</span>", a)
            problem_list.append({'problemid': data_item['problemid']['value'], 'text': b})

        template_context = {
            'skill': skill,
            'problem_list': problem_list
        }
        return render_template('skill.html', **template_context)

    # register the database commands

    from flaskr import db
    
    db.init_app(app)

    return app