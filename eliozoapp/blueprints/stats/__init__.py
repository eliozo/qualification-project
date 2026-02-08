from flask import Blueprint, render_template, json
from eliozo_dao.stats_repository import (
    getSPARQLProblemCounts,
    getSPARQLProblemSolvedCounts,
    getSPARQLPropertyCount,
    getSPARQLActualValueCount,
    getSPARQLMaxValueCount
)

stats_bp = Blueprint('stats_bp', __name__)

@stats_bp.route('/problem_counts', methods=['GET', 'POST'])
def getProblemCounts():
    olympiads = ['LV.SOL', 'LV.NOL', 'LV.VOL', 'LV.AMO', 
                 'WW.IMOSHL']    
    
    x = getSPARQLProblemCounts()
    probCounts = json.loads(x)

    all_counts = dict()
    for item in probCounts['results']['bindings']:
        country = item['country']['value']
        code = item['code']['value']
        olympiadName = item['olympiadName']['value']
        entered = int(item['ProblemCount']['value'])
        all_counts[f'{country}.{code}'] = {'lv':olympiadName, 'entered': entered, 'solved': 0}


    x = getSPARQLProblemSolvedCounts()
    probSolvedCounts = json.loads(x)
    for item in probSolvedCounts['results']['bindings']:
        country = item['country']['value']
        code = item['code']['value']
        solved = int(item['ProblemCount']['value'])
        all_counts[f'{country}.{code}']['solved'] = solved

    template_context = {
        'olympiads': olympiads,
        'all_counts': all_counts,
        'active': 'statistics',
        'navlinks': [
            {'title':'Statistics'}, 
            {'url':'stats_bp.getProblemCounts', 'title':'Problem Count'}
        ],
        'title': 'Problem Count'
    }

    return render_template('stats_problemcounts.html', **template_context)


@stats_bp.route('/property_counts', methods=['GET', 'POST'])
def getPropertyCounts():
    properties = ['questionType', 'domain', 'subdomain', 'topic', 'method', 'concepts', 'olympiad', 'suggestedGrade', 'total']
    problem_counts = dict()
    actual_values = dict()
    max_values = dict()

    values_total = 0
    maxvalues_total = 0
    for prop in properties:
        propResultStr = getSPARQLPropertyCount(prop)
        propResultJson = json.loads(propResultStr)
        current_counts = {'olympiads': 0, 'takehome': 0, 'textbooks': 0, 'training': 0}
        for item in propResultJson['results']['bindings']:
            kk = item["sourceType"]["value"]
            vv = int(item["ProblemCount"]["value"])

            if kk == 'RegionalOrOpen':
                current_counts['olympiads'] = current_counts['olympiads'] + vv
            elif kk == 'National':
                current_counts['olympiads'] = current_counts['olympiads'] + vv
            elif kk == 'International':
                current_counts['olympiads'] = current_counts['olympiads'] + vv
            elif kk == 'Book': 
                current_counts['textbooks'] = current_counts['textbooks'] + vv
        problem_counts[prop] = current_counts

        propActualStr = getSPARQLActualValueCount(prop)
        propActualJson = json.loads(propActualStr)
        for item in propActualJson['results']['bindings']:
            vv = int(item["ValueCount"]["value"])
        actual_values[prop] = vv
        values_total += vv

        if prop == 'domain':
            vv = 4 # Alg, Comb, Geom, NT
        elif prop == 'suggestedGrade':
            vv = 8
        else:
            propMaxStr = getSPARQLMaxValueCount(prop)
            propMaxJson = json.loads(propMaxStr)
            for item in propMaxJson['results']['bindings']:
                vv = int(item["MaxCount"]["value"])
        max_values[prop] = vv
        maxvalues_total += vv

    actual_values['total'] = values_total
    max_values['total'] = maxvalues_total

    template_context = {
        'properties': properties,
        'problem_counts': problem_counts,
        'actual_values': actual_values,
        'max_values': max_values,
        'navlinks': [
            {'title':'Statistics'}, 
            {'url':'stats_bp.getPropertyCounts', 'title':'Property Count'}
        ],
        'title': 'Property Count'
    }
    return render_template('stats_propertycounts.html', **template_context)


@stats_bp.route('/results', methods=['GET', 'POST'])
def getResults():
    template_context = {
        'active': 'statistics',
        'navlinks': [
            {'title':'Statistics'}, 
            {'url':'stats_bp.getResults', 'title':'Result Summary'}
        ],
        'title': 'Result Summary'
    }

    return render_template('stats_results.html', **template_context)
