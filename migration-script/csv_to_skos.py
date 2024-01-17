from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import rdflib
import requests

eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"

SKOS = "http://www.w3.org/2004/02/skos/core#"

def getGoogleSpreadsheet(): # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("resources/spreadsheet_skos.csv", "wb").write(response.content)

def readCSVfile(g): # Funkcija, kas lasa CSV failu
    result = []
    with open('resources/spreadsheet_skos.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            skill_numeric_id = row[0]+'.'+row[1]+'.'+row[2]+'.'+row[3]+'.'+row[4]
            skill_id = row[5]
            skill_prefLabel = row[5]
            skill_description = row[6]
            x = skill_id.rfind(".")
            if x == -1:
                parent_skill_id = '' # Nav vecāka
            else:
                parent_skill_id = skill_id[:x]
            addToRdfGraph(g, skill_numeric_id, skill_id, skill_description, skill_prefLabel, parent_skill_id)
	
# skillDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, numeric_id, skillID, skillDescription, prefLabel, parentSkill_id):
    global eliozo_ns
    skill_node = rdflib.URIRef(eliozo_ns+skillID) # RDF subjekts
    skill_numeric_id_property = rdflib.URIRef(eliozo_ns+'skillNumber') # 1 0 0 0
    skill_id_property = rdflib.URIRef(eliozo_ns+'skillIdentifier') # alg.expr
    skill_description_property = rdflib.URIRef(eliozo_ns+'skillDescription') # Fiksēts URL, kas apraksta RDF predikātu
    skill_prefLabel_property = rdflib.URIRef(SKOS+'prefLabel')
    skill_broader_property = rdflib.URIRef(SKOS+'broader')
    skill_narrower_property = rdflib.URIRef(SKOS+'narrower')
    skill_description_object = rdflib.term.Literal(skillDescription)
    g.add((skill_node, skill_id_property, rdflib.term.Literal(skillID)))
    g.add((skill_node, skill_description_property, skill_description_object))
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