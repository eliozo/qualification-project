import os
from flask import Flask, render_template, abort, url_for, json, jsonify, request
import json
import html
import requests
import re
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.wrappers import Response

FUSEKI_URL = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'

# Integrācija ar Jena Fuseki serveri
def getSPARQLskills():
    ##url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = {'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\n'+
    '''SELECT DISTINCT ?skillIdentifier ?skillNumber ?skillDescription ?problemid WHERE { 
    ?skill eliozo:skillID ?skillIdentifier .
    ?skill eliozo:skillNumber ?skillNumber .
    ?skill eliozo:skillDescription ?skillDescription .
    OPTIONAL {?prob eliozo:hasSkill ?skill . ?prob eliozo:problemID ?problemid . }.
    } ORDER BY ?skillNumber'''
    }

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


def getSPARQLProblem(arg):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = {'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\n'+
'SELECT * WHERE { \n'+
  '?problem eliozo:problemID \'{problemid}\' .\n' .format(problemid=arg)+
  '''OPTIONAL {
    ?problem eliozo:problemText ?text ;
             eliozo:problemYear ?year ;
             eliozo:olympiadCode ?olympiad ;
             eliozo:problemGrade ?grade ;
             eliozo:country ?country .
             } .
      OPTIONAL {
        ?problem eliozo:hasSkill ?skill .
        ?skill eliozo:skillID ?skillIdentifier .
    } .
      OPTIONAL {
        ?problem eliozo:hasVideo ?video .
    } .
    OPTIONAL {
        ?problem eliozo:problemImage ?imageRes .
        ?imageRes eliozo:imageSrc ?imageSrc ;
        eliozo:imageWidth ?imageWidth .
    }
}'''
  }
    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print("myobj= {}".format(myobj))

    print(x.text)

    return x.text

def getSkillProblemsSPARQL(skillID):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = {'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\n'+
    '''SELECT DISTINCT ?problem ?problemid ?subskill ?text ?grade
WHERE {
    ?parent skos:prefLabel \''''+skillID+'''\'  .
    ?parent skos:narrower* ?subskill .
    ?problem eliozo:hasSkill ?subskill ;
             eliozo:problemID ?problemid ;
             eliozo:problemText ?text ;
             eliozo:problemGrade ?grade .
} ORDER BY ?grade
 '''

}

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getAllSkillChildren(skillID):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = {'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\n'+
    '''SELECT ?skillID ?prefLabel ?num ?desc WHERE {
	?alg skos:prefLabel \''''+skillID+'''\' .
    ?skillID skos:broader ?alg ;
             skos:prefLabel ?prefLabel ;
             eliozo:skillDescription ?desc ;
  			 eliozo:skillNumber ?num .
} ORDER BY ?num'''
    }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getSPARQLOlympiads():
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = { 'query': '''PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?olympiadCountry ?olympiad ?olympiadName ?olympiadDescription WHERE { 
    ?problem eliozo:olympiad ?olympiad .
    ?olympiad eliozo:olympiadCountry ?olympiadCountry ;
  				eliozo:olympiadName ?olympiadName ;
                eliozo:olympiadDescription ?olympiadDescription .
} ORDER BY ?olympiadCountry ?olympiadName'''
    }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getSPARQLOlympiadYears(country, olympiad):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = { 'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>\n'+
    'SELECT DISTINCT ?year ?grade WHERE { ?problem eliozo:country \''+country+
    '\' ; eliozo:olympiadCode \''+olympiad+
    '\' ; eliozo:problemYear ?year ; eliozo:problemGrade ?grade . } ORDER BY ?year ?grade'
    }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text

def getSPARQLOlympiadGrades(year, country, grade, olympiad):
    # url = 'http://localhost:8080/jena-fuseki-war-4.6.1/abc/'
    url = FUSEKI_URL
    myobj = { 'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>\n'+
    '''SELECT ?text ?problemid ?problem_number ?imagefile WHERE {
  ?problem eliozo:problemYear \''''+year+'''\' .
  ?problem eliozo:country \''''+country+'''\' .
  ?problem eliozo:problemText ?text .
  ?problem eliozo:problemID ?problemid .
  ?problem eliozo:problem_number ?problem_number .
  ?problem eliozo:problemGrade '''+grade+''' .
  ?problem eliozo:olympiadCode \''''+olympiad+'''\' .
  OPTIONAL {
    ?problem eliozo:image ?imagefile .
  } .
} ORDER BY ?problem_number'''
    }

    print('**********myobj={}'.format(myobj))

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
    myobj = { 'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
    'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
    'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
    'PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>\n'+
    '''SELECT ?problemid WHERE {
  ?problem eliozo:problemID ?problemid ;
           eliozo:problemGrade ?grade ;
  	       eliozo:hasVideo ?video .         
  } ORDER BY ?grade'''
    }

    head = {'Content-Type' : 'application/x-www-form-urlencoded'}

    x = requests.post(url, myobj, head)

    print(x.text)

    return x.text


def mathBeautify(a): # Izskaistina formulas ar MathJax Javascript bibliotēku
    b0 = re.sub(r"\$\$([^\$]+)\$\$", r"<p><span class='math display'>\[\1\]</span></p>", a) # Aizstāj vairākrindu formulas $$..$$
    b = re.sub(r"\$([^\$]+)\$", r"<span class='math inline'>\(\1\)</span>", b0) # Aizstāj inline formulas $...$ (Svarīga secība, kā aizstāj)
    return b

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

    # json 
    @app.route("/json")
    def getJson():
        # Lasa failu
        with open('C:/Users/eliz_/Documents/qualification-project/flask-application/data/file.json', 'r', encoding="utf-8") as myfile:
            data = myfile.read()
        return render_template('index.html', title="page", jsonfile=json.dumps(data))

    @app.route("/info")
    def getInfo():
        return render_template("info.html")

    @app.route("/video")
    def getVideo():
        data = json.loads(getAllSPARQLVideos())

        all_problemids = []

        for item in data['results']['bindings']:
            problem_id_with_video = item['problemid']['value']
            all_problemids.append(problem_id_with_video)

        template_context = {
            'all_problemids' : all_problemids
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

        return render_template('video.html', **template_context)

    @app.route('/skills', methods=['GET','POST'])
    def getSkills():
        data = json.loads(getSPARQLskills())

        all_skills = []
        all_skill_info = dict() # Vārdnīca visai prasmju tabulai

        current_skill = "NA"

        for item in data['results']['bindings']:
            if item['skillIdentifier']['value'] != current_skill:
                all_skills.append(item['skillIdentifier']['value']) # Pievienojam jaunu prasmi sarakstam all_skills
                current_skill = item['skillIdentifier']['value'] # Atceramies pēdējo pievienoto vērtību, lai neiespraustu atkārtoti
                current_skill_info = dict() # Vārdnīca vienai tabulas rindai
                current_skill_info['skillIdentifier'] = current_skill
                current_skill_info['skillNumber'] = item['skillNumber']['value']
                beautiful_description = mathBeautify(item['skillDescription']['value'])
                current_skill_info['skillDescription'] = beautiful_description
                if "problemid" in item:
                    current_skill_info['problems'] = [item['problemid']['value']]
                else:
                    current_skill_info['problems'] = []
                all_skill_info[current_skill] = current_skill_info # Lielajā vārdnīcā iesprauž mazo vārdnīcu
            else:
                current_skill_info['problems'].append(item['problemid']['value']) # Pievieno tikai jauno uzdevuma ID

        template_context = {
            'all_skills': all_skills,
            'all_skill_info' : all_skill_info
        }

        return render_template('skills.html', **template_context)


    @app.route('/topics', methods=['GET','POST'])
    def getTopics():

        all_topics = json.loads(getSPARQLtopics('eliozo:analysis'))
        topic_list = ["Pirmā tēma", "Otrā tēma"]
        for item in all_topics['results']['bindings']:
            topic_list.append(item['topicTitle']['value'])

        myTree = {
            "root": ["child1", "child2"],
            "child1": ["grandchild1", "grandchild2"],
            "child2": [],
            "grandchild1": [],
            "grandchild2": []
        }

        template_context = {
            'all_topics': topic_list,
            'tree': myTree
        }
        return render_template('topics.html', **template_context)

    @app.route('/skill_tasks', methods=['GET','POST']) # Kontrolieris, kas iegūst prasmes kopā ar uzdevumiem
    def getSkill():
        skill = request.args.get('skillIdentifier')
        all_skills = json.loads(getAllSkillChildren(skill))
        skill_list = []
        for skill_item in all_skills['results']['bindings']: # all_skills saraksts ar vārdnīcām
            prefLabel = skill_item['prefLabel']['value']
            desc = skill_item['desc']['value']
            dd = {'prefLabel': prefLabel, 'desc' : desc}
            skill_list.append(dd)

        data = json.loads(getSkillProblemsSPARQL(skill))
        problem_list = []
        for data_item in data['results']['bindings']:
            a = data_item['text']['value']
            b = mathBeautify(a)
            problem_list.append({'problemid': data_item['problemid']['value'], 'text': b})

        template_context = {
            'skill': skill,
            'problem_list': problem_list,
            'skill_list' : skill_list
        }
        return render_template('skill_tasks.html', **template_context)


    @app.route('/problem', methods=['GET','POST'])
    def getProblem():
        problemid = request.args.get('problemid')
        data = json.loads(getSPARQLProblem(problemid))

        a = data['results']['bindings'][0]['text']['value']
        text = mathBeautify(a)

        if 'video' in data['results']['bindings'][0]:
            hasVideo = data['results']['bindings'][0]['video']['value'] != ''
        else:
            hasVideo = False

        if 'imageSrc' in data['results']['bindings'][0]:
            image_src = data['results']['bindings'][0]['imageSrc']['value']
        else:
            image_src = ''

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

        template_context = {
            'problemid': problemid,
            'data': data['results']['bindings'],
            'text': text,
            'hasVideo': hasVideo,
            'video_title': video_title,
            'bookmarks': bookmarks,
            'youtubeID': youtubeID,
            'image_src' : image_src
        }
        return render_template('problem.html', **template_context)


    @app.route('/olympiads', methods=['GET', 'POST'])
    def getOlympiads():
        olympiads = json.loads(getSPARQLOlympiads())
        print(olympiads)
        olympiadData = []
        for rr in olympiads['results']['bindings']:
            olympiadName = rr['olympiadName']
            olympiadDescription = rr['olympiadDescription']
            olyString = rr['olympiad']['value'].split("#")[-1]
            (olympiadCountry,olympiadCode) = olyString.split(".")
            olympiadData.append({'olympiadName': olympiadName, 'olympiadDescription': olympiadDescription, 'olympiadCountry':olympiadCountry, 'olympiadCode': olympiadCode})

        template_context = {
            'links': olympiadData
        }

        return render_template('olympiads.html', **template_context)

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
            'olympiad_id': olympiad_id          
        }
        # Kontrolieris izlemj, uz kuru skatu sūtīs klientu
        return render_template('olympiad.html', **template_context)

#year, country, grade, olympiad
    @app.route('/grade', methods=['GET', 'POST'])
    def getGrades():
        year = request.args.get('year')
        country= request.args.get('country')
        grade= request.args.get('grade')
        olympiad= request.args.get('olympiad')
        print('Gads = {}, country - {}, grade = {}, olympiad = {}'.format(year,country,grade,olympiad))
        link = json.loads(getSPARQLOlympiadGrades(year,country,grade,olympiad))

        problems = []
        
        for item in link['results']['bindings']:
            problem_id_value = item['problemid']['value']
            problem_imagefile = ''
            if 'imagefile' in item:
                problem_imagefile = item['imagefile']['value']
            problem_number_value = item['problem_number']['value']
            problem_text_value = mathBeautify(item['text']['value'])
            d = {'problemid': problem_id_value, 'problem_number':problem_number_value, 'text': problem_text_value, 'imagefile': problem_imagefile}
            problems.append(d)


        template_context = {
            'problems': problems,
            'year': year,
            'country': country,
            'grade': grade,
            'olympiad': olympiad
        }

        return render_template('grade.html', **template_context)

    # register the database commands

    from eliozo import db
    
    db.init_app(app)

    app.wsgi_app = DispatcherMiddleware(
        Response('Not Found', status=404),
        {'/eliozo': app.wsgi_app}
    )   

    return app


