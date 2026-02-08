import datetime
import json
from flask import Blueprint, render_template, request, url_for
from collections import defaultdict
from eliozo.webmd_utils import mathBeautify
from eliozo_dao.curriculum_repository import (
    getSPARQLCurriculumQtypeStats,
    getSPARQLOlympiadOverview,
    getSPARQLCurriculumMethods,
    getSPARQLCurriculumSubdomains
)

curriculum_bp = Blueprint('curriculum_bp', __name__)

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

    all_subdomains = []
    all_subdomains_info = dict()

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

                # 4. Subdomain Overview
                data_subdomains = json.loads(getSPARQLCurriculumSubdomains(olympiad_id, (mingrade, maxgrade), (minyear, maxyear)))
                for item in data_subdomains.get('results', {}).get('bindings', []):
                    sd_id = item['domainID']['value']

                    if sd_id not in all_subdomains_info:
                        all_subdomains.append(sd_id)
                        all_subdomains_info[sd_id] = {
                            'domainName': item['domainName']['value'],
                            'domainDescription': mathBeautify(item['domainDescription']['value']),
                            'domainNumber': f"{item['L1']['value']}.{item['L2']['value']}.{item['L3']['value']}",
                            'problems': []
                        }

                    p_id = item['problemID']['value']
                    if p_id not in all_subdomains_info[sd_id]['problems']:
                        all_subdomains_info[sd_id]['problems'].append(p_id)

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
        'all_subdomains': all_subdomains,
        'all_subdomains_info': all_subdomains_info,
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
