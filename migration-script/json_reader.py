import json
import re
# from rdflib import Graph, URIRef, Literal, Namespace, BNode
import rdflib
from rdflib.namespace import RDF, FOAF, SKOS

eozol_ns = "http://www.dudajevagatve.lv/eozol#"

def addToRdfGraph(g, title, text, country, olympiad, year, grade):
    global eozol_ns
    problem_node = rdflib.URIRef(eozol_ns+title)
    problem_text_property = rdflib.URIRef(eozol_ns+'text')
    problem_country_property = rdflib.URIRef(eozol_ns+'country')
    problem_olympiad_property = rdflib.URIRef(eozol_ns+'olympiad')
    problem_year_property = rdflib.URIRef(eozol_ns+'year')
    problem_grade_property = rdflib.URIRef(eozol_ns+'grade')
    problem_text = rdflib.term.Literal(text, lang=u'lv')
    problem_id = rdflib.URIRef(eozol_ns+'problemid')
    g.add((problem_node, problem_text_property, problem_text))
    g.add((problem_node, problem_country_property, rdflib.term.Literal(country)))
    g.add((problem_node, problem_olympiad_property, rdflib.term.Literal(olympiad)))
    g.add((problem_node, problem_year_property, rdflib.term.Literal(year)))
    g.add((problem_node, problem_grade_property, rdflib.term.Literal(grade)))
    g.add((problem_node, problem_id, rdflib.term.Literal(title)))

current_problem_id = "NA"

def addSkillToRdfGraph(g, title, skill):
    global eozol_ns
    problem_node = rdflib.URIRef(eozol_ns+title) # subjekts
    problem_skill_property = rdflib.URIRef(eozol_ns+'skill') # property vienmēr eozol:skill, predikāts
    problem_skill_object = rdflib.URIRef(eozol_ns+skill) # konkrētā prasme, īpašība var atkāroties, objekts
    g.add((problem_node, problem_skill_property, problem_skill_object))

def produceRDF(in_file, out_file):
    EOZOL = rdflib.Namespace("http://www.dudajevagatve.lv/eozol#")

    g = rdflib.Graph()

    g.bind("foaf", FOAF)
    g.bind("skos", SKOS)
    g.bind("eozol", EOZOL)

    # Opening JSON file
    f = open(in_file)
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)

    # print(data['children'][1])
    items = data['children']

    state = 0

    problem_title = 'undefined'

    for item in items:
        # for subitem in item:
            # if subitem.type == 'Heading':
                # print(subitem)
        if item['type'] == 'Heading':
            state = 1
            problem_title = item['children'][0]['content']

            if problem_title.startswith('<lo-sample/>'):
                print()
                print(problem_title)
                print("************************")
            else:
                state = 0
    #    elif state == 1 and item['children'][0]['content'].startswith('<small>'):
    #        state = 0
        elif state == 1 and item['type'] == 'Paragraph':
            country = "NA"
            olympiad = "NA"
            year = "NA"
            grade = "NA"
            problem_title = problem_title[13:]
            current_problem_id = problem_title
            problem_id = re.compile(r"([A-Z]{2})\.(\w+)\.(\d+)\.(\d+)\.(\d+)")
            match_id = problem_id.match(problem_title)
            if (match_id):
                country = match_id.group(1)
                olympiad = match_id.group(2)
                year = match_id.group(3)
                grade = match_id.group(4)
                if int(grade) < 10:
                    grade = '0'+ grade
            problem_text = ""
            for line in item['children']:
                if line['type'] == 'RawText':
                    problem_text = problem_text+line['content']
                elif line['type'] == 'LineBreak':
                    problem_text = problem_text+'\n'
            print(problem_text)
            addToRdfGraph(g, problem_title, problem_text, country, olympiad, year, grade)
            state = 0
        elif state == 0 and item['type'] == 'Paragraph' and ('content' in item['children'][0].keys()) and item['children'][0]['content'] == '<small>':
            state = 2
        elif state == 2 and item['type'] == 'List':
            skill_items = item['children']
            for skill_item in skill_items:
                # print('#################{}'.format(skill_item))
                if skill_item['type'] == 'ListItem':
                    skill = skill_item['children'][0]['children'][0]['children'][0]['content']
                    print('{}'.format(skill))
                    addSkillToRdfGraph(g, current_problem_id, skill)
        else:
            state = 0
    g.serialize(destination=out_file)

# produceRDF(in_file="LV-AO-out.json", out_file="tbl.ttl")