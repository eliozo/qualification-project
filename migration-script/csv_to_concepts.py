from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import rdflib
import requests
import copy as cp

eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"
RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
SKOS = "http://www.w3.org/2004/02/skos/core#"


def getGoogleSpreadsheet(fname):  # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSsIUjRXRU6L_MGgEmgUZlfwvygclZun964ilvH-l6F3TZ9w0I2MDce9VXqJgd4p2GZxF7vJ6OY5jcT/pub?output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open(fname, "wb").write(response.content)


# skillDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, conceptID, termLV, descLV):
    rdf_type_property = rdflib.URIRef(RDF_NS + 'type')
    topic_node = rdflib.URIRef(eliozo_ns + "TRM-" + conceptID)
    g.add((topic_node, rdf_type_property, rdflib.URIRef(eliozo_ns + "Concept")))
    termEN = conceptID.replace("-", " ")
    termEN_property = rdflib.URIRef(eliozo_ns + 'termEN')
    termLV_property = rdflib.URIRef(eliozo_ns + 'termLV')
    descLV_property = rdflib.URIRef(eliozo_ns + 'descLV')
    conceptID_property = rdflib.URIRef(eliozo_ns + 'conceptID')
    g.add((topic_node, termEN_property, rdflib.term.Literal(termEN, lang=u'en')))
    g.add((topic_node, termLV_property, rdflib.term.Literal(termLV, lang=u'lv')))
    g.add((topic_node, conceptID_property, rdflib.term.Literal(conceptID, lang=u'en')))
    if descLV and descLV != "" and descLV != "NA":
        g.add((topic_node, descLV_property, rdflib.term.Literal(descLV, lang=u'lv')))

def produceCSVtoRDF(in_file, out_file):
    global SKOS
    g = rdflib.Graph()
    g.bind("skos", SKOS)
    g.bind("eliozo", eliozo_ns)
    line_count = 0
    with open(in_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            elif row[0] == '':
                print(f'WARNING: empty concept on line {line_count}')
                continue
            else:
                print(f'"{row[0]}" --> "{row[1]}"')
                addToRdfGraph(g, row[0], row[1], row[2])
    g.serialize(destination=out_file)

if __name__ == '__main__':
    fname = "resources/spreadsheet_concepts.csv"
    getGoogleSpreadsheet(fname)
    produceCSVtoRDF(in_file=fname, out_file="resources/concepts.ttl")