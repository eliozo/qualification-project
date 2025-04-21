import copy

from rdflib import Graph, Namespace, URIRef, Literal, RDF, XSD
# from rdflib.namespace import RDF, FOAF, SKOS, XSD
import csv
import rdflib
import requests

eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
SKOS = "http://www.w3.org/2004/02/skos/core#"

def getGoogleSpreadsheet(URL, FILE): # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
    # URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?output=csv'
    # URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv'
    response = requests.get(URL)
    open(FILE, "wb").write(response.content)

def readCSVfile(in_file, g, class_name):
    num_count = 5 if class_name == 'topic' else 2
    label_nums = [4,3,2,1,0] if class_name == 'topic' else [1,0]
    num_zeroes = '0.0.0.0.0' if class_name == 'topic' else '0.0'


    # result = []
    label_dictionary = dict()
    with open(in_file, 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            topic_numeric_id = [int(i) for i in row[0:num_count]]
            last_non_zero = 0

            for nnum in label_nums: 
                if topic_numeric_id[nnum] != 0:
                    last_non_zero = nnum
                    break

            # if topic_numeric_id[4] != 0:
            #     last_non_zero = 4
            # elif topic_numeric_id[3] != 0:
            #     last_non_zero = 3
            # elif topic_numeric_id[2] != 0:
            #     last_non_zero = 2
            # elif topic_numeric_id[1] != 0:
            #     last_non_zero = 1
            # elif topic_numeric_id[0] != 0:
            #     last_non_zero = 0

            topic_id = row[num_count + 0]
            topic_prefLabel = row[num_count + 0]
            topic_name = row[num_count + 1]
            topic_description = row[num_count + 2]
            current_label = '.'.join([str(i) for i in topic_numeric_id])
            label_dictionary[current_label] = topic_id
            parent_topic_id = copy.copy(topic_numeric_id)
            # print(f'parent_topic_id = {parent_topic_id}, last_non_zero = {last_non_zero}')
            parent_topic_id[last_non_zero] = 0
            parent_id_str = '.'.join([str(i) for i in parent_topic_id])
            if parent_id_str == num_zeroes:
                parent_label = ''
            else:
                # print(f'current_label = {current_label}, parent_id_str = {parent_id_str}, topic_id = {topic_id}, last_non_zero = {last_non_zero}')
                parent_label = label_dictionary[parent_id_str]

            addToRdfGraph(g,
                          class_name,
                          current_label,
                          topic_id,
                          topic_description,
                          topic_prefLabel,
                          topic_name,
                          parent_label)
	
# topicDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, class_name, numeric_id, topicID, topicDescription, prefLabel, topicName, parentTopicID):
    
    propNames = {
        'topic': {
            'number': 'topicNumber', 
            'id': 'topicID', 
            'description': 'topicDescription',
            'name': 'topicName',
            'class': 'Topic'
        }, 
        'method': {
            'number': 'methodNumber', 
            'id': 'methodID', 
            'description': 'methodDescription',
            'name': 'methodName',
            'class': 'Method'
        }, 
        'domain': {
            'number': 'domainNumber', 
            'id': 'domainID', 
            'description': 'domainDescription',
            'name': 'domainName',
            'class': 'Domain'
        }, 
    }

    topicNode = rdflib.URIRef(eliozo_ns+topicID) # RDF subjekts
    topic_numeric_id_property = rdflib.URIRef(eliozo_ns + propNames[class_name]['number']) # 1 0 0 0
    topic_sorter_l1_property = rdflib.URIRef(eliozo_ns + 'sorter_L1')
    topic_sorter_l2_property = rdflib.URIRef(eliozo_ns + 'sorter_L2')
    topic_sorter_l3_property = rdflib.URIRef(eliozo_ns + 'sorter_L3')
    topic_sorter_l4_property = rdflib.URIRef(eliozo_ns + 'sorter_L4')
    topic_sorter_l5_property = rdflib.URIRef(eliozo_ns + 'sorter_L5')

    topic_id_property = rdflib.URIRef(eliozo_ns + propNames[class_name]['id']) # alg.expr
    topic_description_property = rdflib.URIRef(eliozo_ns + propNames[class_name]['description']) # Fiksēts URL, kas apraksta RDF predikātu
    topic_name_property = rdflib.URIRef(eliozo_ns + propNames[class_name]['name'])
    topic_rdf_type_property = rdflib.URIRef(RDF_NS+'type')
    topic_prefLabel_property = rdflib.URIRef(SKOS+'prefLabel')
    topic_broader_property = rdflib.URIRef(SKOS+'broader')
    topic_narrower_property = rdflib.URIRef(SKOS+'narrower')
    topic_description_object = rdflib.term.Literal(topicDescription)
    g.add((topicNode, topic_id_property, rdflib.term.Literal(topicID)))
    g.add((topicNode, topic_description_property, topic_description_object))
    g.add((topicNode, topic_name_property, rdflib.term.Literal(topicName)))
    g.add((topicNode, topic_rdf_type_property, rdflib.URIRef(eliozo_ns+propNames[class_name]['class'])))
    g.add((topicNode, topic_numeric_id_property, rdflib.term.Literal(numeric_id)))
    # Add levels L1, L2 (possibly also L3-L5) as integers
    sorters = [int(num) for num in numeric_id.split(".")]
    g.add((topicNode, topic_sorter_l1_property, rdflib.term.Literal(sorters[0], datatype=XSD.integer)))
    g.add((topicNode, topic_sorter_l2_property, rdflib.term.Literal(sorters[1], datatype=XSD.integer)))
    if class_name == 'topic':
        g.add((topicNode, topic_sorter_l3_property, rdflib.term.Literal(sorters[2], datatype=XSD.integer)))
        g.add((topicNode, topic_sorter_l4_property, rdflib.term.Literal(sorters[3], datatype=XSD.integer)))
        g.add((topicNode, topic_sorter_l5_property, rdflib.term.Literal(sorters[4], datatype=XSD.integer)))
    g.add((topicNode, topic_prefLabel_property, rdflib.term.Literal(prefLabel)))
    if parentTopicID != '':
        parent_topic_node = rdflib.URIRef(eliozo_ns+parentTopicID)
        g.add((topicNode, topic_broader_property, parent_topic_node)) # bērns iedur vecākam
        g.add((parent_topic_node, topic_narrower_property, topicNode)) # vecāks iedur bērnam
    

def produceCSVtoRDF(in_file, out_file, class_name): # Pārveido CSV failu par RDF failu
    global SKOS
    g = rdflib.Graph()
    g.bind("skos", SKOS)
    g.bind("eliozo", eliozo_ns)
    f = open(in_file)
    readCSVfile(in_file, g, class_name)
    g.serialize(destination=out_file)

if __name__ == '__main__':
    TOPIC_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=462395741&single=true&output=csv'
    TOPIC_FILE = 'resources/spreadsheet_topic_skos.csv'
    TOPIC_OUT = 'resources/skos_topic.ttl'

    METHOD_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1894093694&single=true&output=csv'
    METHOD_FILE = 'resources/spreadsheet_method_skos.csv'
    METHOD_OUT = 'resources/skos_method.ttl'

    SUBDOMAIN_URL = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?gid=1943031484&single=true&output=csv'
    SUBDOMAIN_FILE = 'resources/spreadsheet_subdomain_skos.csv'
    SUBDOMAIN_OUT = 'resources/skos_subdomain.ttl'

    getGoogleSpreadsheet(TOPIC_URL, TOPIC_FILE) 
    produceCSVtoRDF(in_file=TOPIC_FILE, out_file=TOPIC_OUT, class_name='topic')

    getGoogleSpreadsheet(METHOD_URL, METHOD_FILE) 
    produceCSVtoRDF(in_file=METHOD_FILE, out_file=METHOD_OUT, class_name='method')

    getGoogleSpreadsheet(SUBDOMAIN_URL, SUBDOMAIN_FILE) 
    produceCSVtoRDF(in_file=SUBDOMAIN_FILE, out_file=SUBDOMAIN_OUT, class_name='domain')
