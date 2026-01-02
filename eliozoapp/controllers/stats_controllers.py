from flask import Flask, render_template, abort, url_for, json, jsonify, request, session, redirect, send_from_directory

import requests
import platform

FUSEKI_URL_LINUX = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'


os_name = platform.system()

# Check if it's Windows
if os_name == 'Windows':
    FUSEKI_URL=FUSEKI_URL_LINUX
else:
    FUSEKI_URL=FUSEKI_URL_LINUX

def getSPARQLProblemCounts():
    url = FUSEKI_URL
    query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

SELECT ?country ?code ?olympiadName (COUNT(DISTINCT ?problem) AS ?ProblemCount)
WHERE {
  ?olympiad eliozo:olympiadName ?olympiadName ;
            eliozo:olympiadDescription ?olympiadDescription ;
            eliozo:olympiadCountry ?country ;
            eliozo:olympiadCode ?code .
  ?problem rdf:type eliozo:Problem ;
           eliozo:country ?country ;
           eliozo:olympiadCode ?code .
  FILTER (lang(?olympiadName) = "lv")
            FILTER (lang(?olympiadDescription) = "lv")
}
GROUP BY ?country ?code ?olympiadName"""
    myobj = {'query': query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLProblemSolvedCounts():
    url = FUSEKI_URL
    query = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT ?country ?code ?olympiadName (COUNT(DISTINCT ?problem) AS ?ProblemCount)
    WHERE {
    ?olympiad eliozo:olympiadName ?olympiadName ;
                eliozo:olympiadDescription ?olympiadDescription ;
                eliozo:olympiadCountry ?country ;
                eliozo:olympiadCode ?code .
    ?problem rdf:type eliozo:Problem ;
            eliozo:problemSolution ?soln ;
            eliozo:country ?country ;
            eliozo:olympiadCode ?code .
    FILTER (lang(?olympiadName) = "lv")
                FILTER (lang(?olympiadDescription) = "lv")
    }
    GROUP BY ?country ?code ?olympiadName"""
    myobj = {'query': query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text 


def getSPARQLPropertyCount(arg):
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT ?sourceType (COUNT(DISTINCT ?problem) AS ?ProblemCount)
    WHERE {{
    ?problem rdf:type eliozo:Problem ;
            {propertyClause}
            eliozo:olympiadType ?sourceType .
    }}
    GROUP BY ?sourceType"""
    if arg == 'total':
        actual_query = queryTemplate.format(propertyClause='')
    else:
        actual_query = queryTemplate.format(propertyClause=f'eliozo:{arg} ?dummy ; ')
    myobj = {'query': actual_query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text


def getSPARQLActualValueCount(arg):
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT (COUNT(DISTINCT ?tt) AS ?ValueCount)
    WHERE {{
    ?problem rdf:type eliozo:Problem ;
            eliozo:{propertyName} ?tt .
    }}"""
    actual_query = queryTemplate.format(propertyName=arg)
    myobj = {'query': actual_query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

def getSPARQLMaxValueCount(arg): 
    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT (COUNT(DISTINCT ?vv) AS ?MaxCount)
    WHERE {{
    ?vv rdf:type eliozo:{propType} .
    }}
    """
    
    if arg == 'questionType':
        propType = 'Question'
    elif arg == 'method':
        propType = 'Method'
    elif arg == 'topic':
        propType = 'Topic'
    elif arg == 'subdomain': 
        propType = 'Domain'
    elif arg == 'concepts':
        propType = 'Concept'
    elif arg == 'olympiad': 
        propType = 'Olympiad'
    else:
        propType = 'Question'

    actual_query = queryTemplate.format(propType=propType)
    myobj = {'query': actual_query}
    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)
    return x.text

# @app.route('/problem_counts', methods=['GET', 'POST'])
def getProblemCounts():
    olympiads = ['LV.SOL', 'LV.NOL', 'LV.VOL', 'LV.AMO', 
                 'WW.IMOSHL']    
                #  'LV.TST', 
                #  'LT.LJMO', 'LT.SAV', 'LT.LMMO', 'LT.LKMMO', 'LT.LDK', 'LT.VUMIF', 'LT.TST',
                #  'EE.PK', 'EE.LO', 'EE.LHT', 'EE.TST']
    
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

    print('------------------')
    print(f'all_counts = {all_counts}')
    print('==================')

    template_context = {
        'olympiads': olympiads,
        'all_counts': all_counts,
        'active': 'statistics',
        'navlinks': [
            {'title':'Statistics'}, 
            {'url':'getProblemCounts', 'title':'Problem Count'}
        ],
        'lang': session.get('lang', 'lv'),
        'title': 'Problem Count'
    }

    return render_template('stats_problemcounts.html', **template_context)

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
            {'url':'getPropertyCounts', 'title':'Property Count'}
        ],
        'lang': session.get('lang', 'lv'),
        'title': 'Property Count'
    }
    return render_template('stats_propertycounts.html', **template_context)