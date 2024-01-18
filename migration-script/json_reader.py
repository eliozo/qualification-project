import json
import re
# from rdflib import Graph, URIRef, Literal, Namespace, BNode
import rdflib
from rdflib.namespace import RDF, FOAF, SKOS, XSD

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"

def addToRdfGraph(g, title, text, country, olympiad, year, grade, problem_number): # Funkcija, kas pievieno RDF datus grafam
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns+title)
    problem_text_property = rdflib.URIRef(eliozo_ns+'problemText')
    problem_country_property = rdflib.URIRef(eliozo_ns+'country')
    problem_olympiad_property = rdflib.URIRef(eliozo_ns+'olympiad')
    problem_year_property = rdflib.URIRef(eliozo_ns+'problemYear')
    problem_grade_property = rdflib.URIRef(eliozo_ns+'problemGrade')
    problem_number_property = rdflib.URIRef(eliozo_ns+'problem_number')
    problem_rdf_property = rdflib.URIRef(RDF_NS+'type')
    problem_text = rdflib.term.Literal(text, lang=u'lv')
    problem_id = rdflib.URIRef(eliozo_ns+'problemID')
    g.add((problem_node, problem_text_property, problem_text))
    g.add((problem_node, problem_country_property, rdflib.term.Literal(country)))
    g.add((problem_node, problem_olympiad_property, rdflib.term.Literal(olympiad)))
    g.add((problem_node, problem_year_property, rdflib.term.Literal(year)))
    g.add((problem_node, problem_grade_property, rdflib.term.Literal(grade, datatype=XSD.integer)))
    g.add((problem_node, problem_number_property, rdflib.term.Literal(problem_number)))
    g.add((problem_node, problem_id, rdflib.term.Literal(title)))
    g.add((problem_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Problem")))

current_problem_id = "NA"

def addSkillToRdfGraph(g, title, skill): # Funkcija, kas pievieno RDF prasmes datus grafam 
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns+title) # subjekts
    problem_skill_property = rdflib.URIRef(eliozo_ns+'hasSkill') # property vienmēr eliozo:skill, predikāts
    problem_skill_object = rdflib.URIRef(eliozo_ns+skill) # konkrētā prasme, īpašība var atkāroties, objekts
    g.add((problem_node, problem_skill_property, problem_skill_object))

def addImageToRDFGraph(g, title, image_src): 
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns+title) # subjekts
    problem_image_property = rdflib.URIRef(eliozo_ns+'image') 
    problem_image_object = rdflib.term.Literal(image_src) 
    g.add((problem_node, problem_image_property, problem_image_object))

def produceRDF(in_file, out_file): # Funkcija, kas pārveido JSON failu par RDF
    ELIOZO = rdflib.Namespace("http://www.dudajevagatve.lv/eliozo#")

    g = rdflib.Graph()

    g.bind("foaf", FOAF)
    g.bind("skos", SKOS)
    g.bind("eliozo", ELIOZO)

    f = open(in_file) # Atver JSON failu
    
    data = json.load(f) # Atgriež JSON objektu kā vārdnīcu

    items = data['children']

    state = 0

    problem_title = 'undefined'

    for item in items:
        if item['type'] == 'Heading':
            state = 1
            problem_title = item['children'][0]['content']

            if problem_title.startswith('<lo-sample/>'):
                pass
            else:
                state = 0
        elif state == 1 and item['type'] == 'Paragraph':
            country = "NA"
            olympiad = "NA"
            year = "NA"
            grade = "NA"
            problem_number = "NA"
            problem_title = problem_title[13:]
            current_problem_id = problem_title
            problem_id = re.compile(r"([A-Z]{2})\.(\w+)\.(\d+)\.(\d+)([A-Za-z_]+\w*)?\.(\d+)") # LV.AO.2000.7.1
            match_id = problem_id.match(problem_title)
            if (match_id):
                country = match_id.group(1)
                olympiad = match_id.group(2)
                year = match_id.group(3)
                grade = match_id.group(4)
                problem_number = match_id.group(6)
            if grade == "NA":
                grade = 0
            problem_text = ""
            for line in item['children']:
                if line['type'] == 'RawText':
                    problem_text = problem_text+line['content']
                elif line['type'] == 'LineBreak':
                    problem_text = problem_text+'\n'
            addToRdfGraph(g, problem_title, problem_text, country, olympiad, year, grade, problem_number)
            state = 0
        elif state == 0 and item['type'] == 'Paragraph' and ('content' in item['children'][0].keys()) and item['children'][0]['content'] == '<small>':
            state = 2
        elif state == 2 and item['type'] == 'List':
            skill_items = item['children']
            for skill_item in skill_items:
                if skill_item['type'] == 'ListItem':
                    skill = skill_item['children'][0]['children'][0]['children'][0]['content']
                    addSkillToRdfGraph(g, current_problem_id, skill)
        elif state == 0 and item['type'] == 'Paragraph' and item['children'][0]['type'] == 'Image':
            image_src = item['children'][0]['src']
            # print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa{}'.format(image_src))
            addImageToRDFGraph(g, current_problem_id, image_src)
        else:
            state = 0
    g.serialize(destination=out_file)