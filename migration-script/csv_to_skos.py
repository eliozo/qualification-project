import copy

from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import rdflib
import requests

eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
SKOS = "http://www.w3.org/2004/02/skos/core#"

def getGoogleSpreadsheet(): # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
    # URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?output=csv'
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("resources/spreadsheet_skos.csv", "wb").write(response.content)

def readCSVfile(g): # Funkcija, kas lasa CSV failu
    # result = []
    label_dictionary = dict()
    with open('resources/spreadsheet_skos.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            # skill_numeric_id = row[0]+'.'+row[1]+'.'+row[2]+'.'+row[3]+'.'+row[4]
            skill_numeric_id = row[0:5]
            last_non_zero = 0
            if row[4] != 0:
                last_non_zero = 4
            elif row[3] != 0:
                last_non_zero = 3
            elif row[2] != 0:
                last_non_zero = 2
            elif row[1] != 0:
                last_non_zero = 1
            elif row[0] != 0:
                last_non_zero = 0

            skill_id = row[5]
            skill_prefLabel = row[5]
            skill_name = row[6]
            skill_description = row[7]
            current_label = '.'.join(skill_numeric_id)
            label_dictionary[current_label] = skill_id
            parent_skill_id = copy.copy(skill_id)
            parent_skill_id[last_non_zero] = 0
            parent_label = '.'.join(parent_skill_id)

            # x = skill_id.rfind(".")
            # if x == -1:
            #     parent_skill_id = '' # Nav vecāka
            # else:
            #     parent_skill_id = skill_id[:x]
            addToRdfGraph(g,
                          skill_numeric_id,
                          skill_id,
                          skill_description,
                          skill_prefLabel,
                          skill_name,
                          parent_skill_id)
	
# skillDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, numeric_id, skillID, skillDescription, prefLabel, skill_name, parentSkill_id):
    global eliozo_ns
    skill_node = rdflib.URIRef(eliozo_ns+skillID) # RDF subjekts
    skill_numeric_id_property = rdflib.URIRef(eliozo_ns+'skillNumber') # 1 0 0 0
    skill_id_property = rdflib.URIRef(eliozo_ns+'skillID') # alg.expr
    skill_description_property = rdflib.URIRef(eliozo_ns+'skillDescription') # Fiksēts URL, kas apraksta RDF predikātu
    skill_name_property = rdflib.URIRef(eliozo_ns+'skillName')
    skill_rdf_type_property = rdflib.URIRef(RDF_NS+'type')
    skill_prefLabel_property = rdflib.URIRef(SKOS+'prefLabel')
    skill_broader_property = rdflib.URIRef(SKOS+'broader')
    skill_narrower_property = rdflib.URIRef(SKOS+'narrower')
    skill_description_object = rdflib.term.Literal(skillDescription)
    g.add((skill_node, skill_id_property, rdflib.term.Literal(skillID)))
    g.add((skill_node, skill_description_property, skill_description_object))
    g.add((skill_node, skill_name_property, rdflib.term.Literal(skill_name)))
    g.add((skill_node, skill_rdf_type_property, rdflib.URIRef(eliozo_ns+"Skill")))
    g.add((skill_node, skill_numeric_id_property, rdflib.term.Literal(numeric_id)))
    g.add((skill_node, skill_prefLabel_property, rdflib.term.Literal(prefLabel)))
    if parentSkill_id != '':
        parent_skill_node = rdflib.URIRef(eliozo_ns+parentSkill_id)
        g.add((skill_node, skill_broader_property, parent_skill_node)) # bērns iedur vecākam
        g.add((parent_skill_node, skill_narrower_property, skill_node)) # vecāks iedur bērnam
    

def produceCSVtoRDF(in_file, out_file): # Pārveido CSV failu par RDF failu

    global SKOS

    g = rdflib.Graph()

    g.bind("skos", SKOS)
    g.bind("eliozo", eliozo_ns)

    # Atver JSON failu
    f = open(in_file)

    readCSVfile(g)

    g.serialize(destination=out_file)

if __name__ == '__main__':
    getGoogleSpreadsheet() # Izsauc funkciju, kas iegūst skos dokumentu CSV faila formātā
    produceCSVtoRDF(in_file="resources/spreadsheet_skos.csv", out_file= "resources/skos.ttl")