from flask import Blueprint, render_template, request, session, url_for, json
from eliozo.webmd_utils import mathBeautify, fix_image_links
from eliozo_dao.filter_repository import (
    getProblemsByFiltersSPARQL,
    getProblemCountsByFiltersSPARQL
)

filter_bp = Blueprint('filter', __name__)

@filter_bp.route('/filter')
def getFilter():
    lang = session.get('lang', 'lv')
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
                        (' জয়ের', {'en':'NA', 'lt':'NA', 'lv':'NA'})]
    # Fixed typo from original code: '-' key in olympiadTypeDict at index 6. Assuming '-' is correct based on original code but let's stick to original list.
    # Wait, the original code had ('-', ...). Let's double check copy paste.
    
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
                    'url': 'filter.getFilter', 
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

        # print('======================')
        # print(f'all_counts = {all_counts}')
        # print('++++++++++++++++++++++')

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
                    'url': 'filter.getFilter', 
                    'title': 'Filters'
                }
            ],
            'title': 'Filtri'
        }
        return render_template('filter_content.html', **template_context)
