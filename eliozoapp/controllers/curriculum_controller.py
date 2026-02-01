import platform
import requests
import json
import datetime
from flask import Blueprint, render_template, request, session, url_for, redirect
from collections import defaultdict
from eliozo.webmd_utils import mathBeautify

curriculum_bp = Blueprint('curriculum_bp', __name__)

FUSEKI_URL_LINUX = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'
os_name = platform.system()
if os_name == 'Windows':
    FUSEKI_URL = FUSEKI_URL_LINUX
else:
    FUSEKI_URL = FUSEKI_URL_LINUX


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


@curriculum_bp.route('/getCurriculum', methods=['GET', 'POST'])
def getCurriculum():
    today = datetime.date.today()
    current_year = today.year

    # Handle both old linking style (comma separated GET) and new MultiDict from checkboxes
    olympiads = request.args.getlist('olympiad_list') # From form
    if not olympiads:
        # Fallback to single 'olympiad' arg or form list
        single_olymp = request.args.get('olympiad')
        if single_olymp:
            olympiads = [single_olymp]
        else: 
             # Could occur if validation failed or weird state
             olympiads = []

    # Get years and grades
    try:
        minyear = int(request.args.get('minyear', 2000))
        maxyear = int(request.args.get('maxyear', current_year))
        mingrade = int(request.args.get('mingrade', 5))
        maxgrade = int(request.args.get('maxgrade', 12))
    except ValueError:
        minyear = 2000
        maxyear = current_year
        mingrade = 5
        maxgrade = 12

    domains=('Alg', 'Comb', 'Geom', 'NT')
    domains = list(domains)
    matrix = defaultdict(lambda: {d: 0 for d in domains})
    qtypes = set()
    
    all_topics = []
    all_topics_info = dict()
    
    all_methods = []
    all_methods_info = dict()

    # Only fetch data if we have selected olympiads
    if olympiads:
        # We will loop over selected olympiads and aggregate
        for olympiad_id in olympiads:
            try:
                # 1. QType Stats
                data_qtypes = json.loads(getSPARQLCurriculumQtypeStats(olympiad_id, (mingrade, maxgrade), (minyear, maxyear)))
                for b in data_qtypes.get("results", {}).get("bindings", []):
                    d = b["domain"]["value"]
                    qt = b["questionType"]["value"]
                    if d not in domains: continue
                    cnt = int(b["count"]["value"])
                    matrix[qt][d] += cnt # Add to existing
                    qtypes.add(qt)

                # 2. Topic Overview
                data = json.loads(getSPARQLOlympiadOverview(olympiad_id, (mingrade, maxgrade), (minyear, maxyear)))
                
                for item in data.get('results', {}).get('bindings', []):
                    t_id = item['topicID']['value']
                    
                    if t_id not in all_topics_info:
                        all_topics.append(t_id) # Maintain order of first appearance
                        all_topics_info[t_id] = {
                            'topicNumber': item['topicNumber']['value'],
                            'topicName': item['topicName']['value'],
                            'topicDescription': mathBeautify(item['topicDescription']['value']),
                            'problems': []
                        }
                    
                    p_id = item['problemID']['value']
                    if p_id not in all_topics_info[t_id]['problems']:
                        all_topics_info[t_id]['problems'].append(p_id)

                # 3. Method Overview
                data_methods = json.loads(getSPARQLCurriculumMethods(olympiad_id, (mingrade, maxgrade), (minyear, maxyear)))
                for item in data_methods.get('results', {}).get('bindings', []):
                    m_id = item['methodID']['value']
                    
                    if m_id not in all_methods_info:
                        all_methods.append(m_id)
                        all_methods_info[m_id] = {
                            'methodNumber': item['methodNumber']['value'],
                            'methodName': item['methodName']['value'],
                            'methodDescription': mathBeautify(item['methodDescription']['value']),
                            'problems': []
                        }
                    
                    p_id = item['problemID']['value']
                    if p_id not in all_methods_info[m_id]['problems']:
                        all_methods_info[m_id]['problems'].append(p_id)

            except Exception as e:
                print(f"Error fetching data for {olympiad_id}: {e}")
                continue

    question_types = sorted(qtypes)
    
    all_domains_meta = [
        {"name": "Algebra", "prefix": "1."},
        {"name": "Combinatorics", "prefix": "2."},
        {"name": "Geometry", "prefix": "3."},
        {"name": "Number theory", "prefix": "4."},
    ]

    template_context = {
        'olympiads': olympiads, # List for checkboxes
        'olympiad_id': ",".join(olympiads), # Display purpose if needed
        'minyear': minyear, 
        'maxyear': maxyear,
        'mingrade': mingrade, 
        'maxgrade': maxgrade, 
        'current_year': current_year,
        'all_topics': all_topics,
        'all_topics_info': all_topics_info,
        'all_domains': all_domains_meta,
        'all_methods': all_methods,
        'all_methods_info': all_methods_info,
        'active': 'statistics',
        'domains': domains, 
        'question_types': question_types, 
        'matrix': matrix,
        'navlinks': [
            {'title':'Reports'}, 
            {'url':'curriculum_bp.getCurriculum', 'title':'Olympiad Curriculum'}
        ]
    }

    return render_template('curriculum_content.html', **template_context)
