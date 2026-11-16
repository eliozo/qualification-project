import json
from flask import Blueprint, render_template, request, session, url_for
from eliozo.webmd_utils import mathBeautify
from eliozo_dao.problem_listing import _naturalKey
from eliozo_dao.question_type_repository import getQuestionTypes
from eliozo_dao.curriculum_repository import (
    getSPARQLCurriculumCoverage,
    getSPARQLCurriculumQuestionTypes,
    getSPARQLOlympiadOverview,
    getSPARQLCurriculumMethods,
    getSPARQLCurriculumSubdomains
)

curriculum_bp = Blueprint('curriculum_bp', __name__)

# Domains in the order they are listed under each question type; problems
# without a domain are listed last, as NA.
QUESTION_TYPE_DOMAINS = ['Alg', 'Comb', 'Geom', 'NT', 'NA']

# Olympiads offered on the curriculum form
CURRICULUM_OLYMPIADS = ['LV.AMO', 'LV.NOL', 'LV.VOL', 'LV.SOL']


def getCurriculumCoverage():
    """Years and grades that occur in the archive for CURRICULUM_OLYMPIADS (sorted lists)."""
    data = json.loads(getSPARQLCurriculumCoverage(CURRICULUM_OLYMPIADS))
    years, grades = set(), set()
    for b in data.get('results', {}).get('bindings', []):
        try:
            years.add(int(b['year']['value']))
            grades.add(int(b['grade']['value']))
        except ValueError:
            continue
    return {'olympiads': CURRICULUM_OLYMPIADS, 'years': sorted(years), 'grades': sorted(grades)}


def parseInt(value, default):
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


@curriculum_bp.route('/getCurriculum', methods=['GET', 'POST'])
def getCurriculum():
    cov = getCurriculumCoverage()
    question_types = getQuestionTypes(session.get('lang', 'lv'))
    qtype_order = {qid: n for n, qid in enumerate(question_types)}

    # Chips: any combination of olympiads and grades; nothing selected means all.
    sel_olympiads = [o for o in CURRICULUM_OLYMPIADS if o in request.args.getlist('olympiad')]
    requested_grades = {parseInt(g, None) for g in request.args.getlist('grade')}
    sel_grades = [g for g in cov['grades'] if g in requested_grades]

    # Years: an inclusive range, by default the whole archive
    first_year = cov['years'][0] if cov['years'] else 0
    last_year = cov['years'][-1] if cov['years'] else 0
    year_from = min(max(parseInt(request.args.get('year_from'), first_year), first_year), last_year)
    year_to = min(max(parseInt(request.args.get('year_to'), last_year), first_year), last_year)
    if year_from > year_to:
        year_from, year_to = year_to, year_from

    olympiads = sel_olympiads or CURRICULUM_OLYMPIADS
    grades = sel_grades  # empty: no grade filter
    years = (year_from, year_to)

    all_qtypes_info = dict()

    all_topics = []
    all_topics_info = dict()
    
    all_methods = []
    all_methods_info = dict()

    all_subdomains = []
    all_subdomains_info = dict()

    # Aggregate the results of all the olympiads in the query
    for olympiad_id in olympiads:
        try:
            # 1. Question types: problem IDs by question type and domain
            data_qtypes = json.loads(getSPARQLCurriculumQuestionTypes(olympiad_id, grades, years))
            for item in data_qtypes.get('results', {}).get('bindings', []):
                qt = item['questionType']['value']
                if qt not in all_qtypes_info:
                    # Values missing from the vocabulary are shown by their ID, without a description
                    vocabulary = question_types.get(qt, {})
                    all_qtypes_info[qt] = {
                        'questionName': vocabulary.get('name', qt),
                        'questionCanonical': vocabulary.get('canonical', ''),
                        'questionDescription': mathBeautify(vocabulary.get('description', '')),
                        'questionRequiredParts': vocabulary.get('requiredParts', ''),
                        'isSubtype': qt in question_types and not vocabulary['isGroup'],
                        'sorter': qtype_order.get(qt),
                        'problems': {d: [] for d in QUESTION_TYPE_DOMAINS}
                    }
                d = item.get('domain', {}).get('value', 'NA')
                problems = all_qtypes_info[qt]['problems'].setdefault(d, [])
                p_id = item['problemID']['value']
                if p_id not in problems:
                    problems.append(p_id)

            # 2. Topic Overview
            data = json.loads(getSPARQLOlympiadOverview(olympiad_id, grades, years))
            
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
            data_methods = json.loads(getSPARQLCurriculumMethods(olympiad_id, grades, years))
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
            data_subdomains = json.loads(getSPARQLCurriculumSubdomains(olympiad_id, grades, years))
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

    # Question types in vocabulary order (unknown ones last, by ID); problem IDs
    # in natural order; domains without problems are left out
    all_qtypes = sorted(all_qtypes_info, key=lambda qt: (all_qtypes_info[qt]['sorter'] is None,
                                                       all_qtypes_info[qt]['sorter'] or 0, qt))
    for info in all_qtypes_info.values():
        info['problems'] = [(d, sorted(ids, key=_naturalKey)) for d, ids in info['problems'].items() if ids]

    all_domains_meta = [
        {"name": "Algebra", "prefix": "1."},
        {"name": "Combinatorics", "prefix": "2."},
        {"name": "Geometry", "prefix": "3."},
        {"name": "Number theory", "prefix": "4."},
    ]

    template_context = {
        'cov': cov,
        'sel_olympiads': sel_olympiads,
        'sel_grades': sel_grades,
        'year_from': year_from,
        'year_to': year_to,
        'all_topics': all_topics,
        'all_topics_info': all_topics_info,
        'all_domains': all_domains_meta,
        'all_methods': all_methods,
        'all_methods_info': all_methods_info,
        'all_subdomains': all_subdomains,
        'all_subdomains_info': all_subdomains_info,
        'active': 'statistics',
        'all_qtypes': all_qtypes,
        'all_qtypes_info': all_qtypes_info,
        'navlinks': [
            {'title':'Reports'}, 
            {'url':'curriculum_bp.getCurriculum', 'title':'Olympiad Curriculum'}
        ]
    }

    return render_template('curriculum_content.html', **template_context)
