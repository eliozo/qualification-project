# https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Cbs-66PXXr45JreveYV5pa3rojZO1MNWn9Fce_P3ggNtXBOjFKFYym41tM3bGQ1fhUnin0g5_ihs/pub?gid=0&single=true&output=csv

from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import rdflib
import requests
import copy as cp

eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
SKOS = "http://www.w3.org/2004/02/skos/core#"

def getGoogleSpreadsheet(): # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Cbs-66PXXr45JreveYV5pa3rojZO1MNWn9Fce_P3ggNtXBOjFKFYym41tM3bGQ1fhUnin0g5_ihs/pub?gid=0&single=true&output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("resources/spreadsheet_topics.csv", "wb").write(response.content)

def readCSVfile(g, topicDictionary, depthDictionary, allIDs, allAttributes): # Funkcija, kas lasa CSV failu
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    result = []
    line_count = 0
    with open('resources/spreadsheet_topics.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            elif row[0] == '':
                print(f'WARNING: empty topicID in line {line_count}')
                continue
            else:
                topicID = row[0]
                parentTopicId = row[1]
                # parentDepth = int(row[1])
                siblingNum = int(row[2])
                myTitle = row[3].strip()
                myDescription = row[4].strip()
                myURL = row[6].strip()
                if topicID in topicDictionary: 
                    print(f'ERROR: topicID not unique on line {line_count}')
                else:
                    topicDictionary[topicID] = []
                if not parentTopicId in topicDictionary: 
                    print(f'ERROR: parent undefined on line {line_count}')
                
                
                topicDictionary[parentTopicId].append(topicID)
                if siblingNum != len(topicDictionary[parentTopicId]): 
                    expectedSiblingNum = len(topicDictionary[parentTopicId])
                    print(f'WARNING: wrong sibling number {siblingNum} (expected {expectedSiblingNum}) on line {line_count}')
                depthDictionary[topicID] = cp.copy(depthDictionary[parentTopicId])
                depthDictionary[topicID].append(letters[siblingNum-1])
                tempValue = depthDictionary[topicID]
                # print(f'depthDictionary[{topicID}] = {tempValue}')
                # if parentDepth != len(depthDictionary[topicID]) - 1: 
                #     print(f'WARNING: wrong depth on line {line_count}')
                sortingLabel = ".".join(depthDictionary[topicID])
                allIDs[sortingLabel] = topicID
                allAttributes[topicID] = {'parentID': parentTopicId, 'title': myTitle, 'descr': myDescription, 'url': myURL}


            # skill_numeric_id = row[0]+'.'+row[1]+'.'+row[2]+'.'+row[3]+'.'+row[4]
            # skill_id = row[5]
            # skill_prefLabel = row[5]
            # skill_description = row[6]
            # x = skill_id.rfind(".")
            # if x == -1:
            #     parent_skill_id = '' # Nav vecāka
            # else:
            #     parent_skill_id = skill_id[:x]
            # addToRdfGraph(g, skill_numeric_id, skill_id, skill_description, skill_prefLabel, parent_skill_id)
    print(f'line_count = {line_count}')

# skillDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, topicID, sorter, topicTitle, topicDescription, topicUrl, parentTopicID):
    global eliozo_ns
    topic_node = rdflib.URIRef(eliozo_ns+topicID) # RDF subjekts
    topic_id_property = rdflib.URIRef(eliozo_ns+'topicID') # 'proofsByEstimateAndExample'
    topic_sorter_property = rdflib.URIRef(eliozo_ns+'sorter') # 'G.L'
    topic_description_property = rdflib.URIRef(eliozo_ns+'topicDescription') # Fiksēts URL, kas apraksta RDF predikātu
    topic_title_property = rdflib.URIRef(eliozo_ns+'topicTitle') # ''
    topic_url_property = rdflib.URIRef(SKOS+'topicUrl')
    topic_rdf_type_property = rdflib.URIRef(RDF_NS+'type')
    skill_broader_property = rdflib.URIRef(SKOS+'broader')
    skill_narrower_property = rdflib.URIRef(SKOS+'narrower')

    g.add((topic_node, topic_id_property, rdflib.term.Literal(topicID)))
    g.add((topic_node, topic_sorter_property, rdflib.term.Literal(sorter)))
    g.add((topic_node, topic_title_property, rdflib.term.Literal(topicTitle)))
    g.add((topic_node, topic_description_property, rdflib.term.Literal(topicDescription)))
    g.add((topic_node, topic_rdf_type_property, rdflib.URIRef(eliozo_ns+"Topic")))
    g.add((topic_node, topic_url_property, rdflib.term.Literal(topicUrl)))
    # g.add((topic_node, skill_prefLabel_property, rdflib.term.Literal(prefLabel)))
    if parentTopicID != '' and parentTopicID != 'TOP':
        parent_topic_node = rdflib.URIRef(eliozo_ns+parentTopicID)
        g.add((topic_node, skill_broader_property, parent_topic_node)) # bērns iedur vecākam
        g.add((parent_topic_node, skill_narrower_property, topic_node)) # vecāks iedur bērnam
    

def produceCSVtoRDF(in_file, out_file): # Pārveido CSV failu par RDF failu

    global SKOS

    g = rdflib.Graph()

    g.bind("skos", SKOS)
    g.bind("eliozo", eliozo_ns)

    # Atver JSON failu
    f = open(in_file)

    topicDictionary = dict()
    topicDictionary['TOP'] = []

    depthDictionary = dict()
    depthDictionary['TOP'] = []

    allIDs = dict()

    allAttributes = dict()
    readCSVfile(g, topicDictionary, depthDictionary, allIDs, allAttributes)

    allSortingLabels = list(allIDs.keys())
    allSortingLabels.sort()
    for kk in allSortingLabels:
        topicID = allIDs[kk]
        
        parentTopicID = allAttributes[topicID]['parentID']
        title = allAttributes[topicID]['title']
        description = allAttributes[topicID]['descr']
        url = allAttributes[topicID]['url']

        # subtopics = topicDictionary[topicID]
        # print(f'map {topicID} to ({kk}, {parentTopicID}): {subtopics}')
        addToRdfGraph(g, topicID, kk, title, description, url, parentTopicID)
        # print(f'{topicID}: {kk}')

    g.serialize(destination=out_file)

if __name__ == '__main__':
    getGoogleSpreadsheet() # Izsauc funkciju, kas iegūst skos dokumentu CSV faila formātā
    produceCSVtoRDF(in_file="resources/spreadsheet_topics.csv", out_file= "resources/topics.ttl")