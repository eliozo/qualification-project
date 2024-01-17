from rdflib import Graph, Namespace, URIRef, Literal, RDF, XSD
import csv
import rdflib
import requests

eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"

SKOS_NS = "http://www.w3.org/2004/02/skos/core#"

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

def getGoogleSpreadsheet():  # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSithTBvdSFhQeovJbYVCstpt7JkDUZAKXSPOjYraqfCFW2SqNjvN5Yd_xYeIfvtSjVktmBAPo2_dDf/pub?output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("resources/youtube.csv", "wb").write(response.content)


def readCSVfile(in_file, out_file):  # Funkcija, kas lasa CSV failu
    global SKOS_NS
    global eliozo_ns

    g = rdflib.Graph()

    g.bind("skos", SKOS_NS)
    g.bind("eliozo", eliozo_ns)
    result = []
    with open(in_file, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        video_title = ''
        bookmarks = []
        problem_id = ''
        youtube_id = ''
        for row in csv_reader:
            line_count += 1
            if row[0] == '':
                addToRdfGraph(g, problem_id, youtube_id, video_title, bookmarks)
                video_title = ''
                bookmarks = []
                problem_id = ''
                youtube_id = ''
            elif row[1] == 'youtube':
                problem_id = row[0]
                youtube_id = row[2]
            elif row[1] == 'title':
                video_title = row[2]
            elif row[1] == 'bookmark':
                tstamp = row[2]
                bmtxt = row[3]
                bookmarks.append((tstamp, bmtxt))
    addToRdfGraph(g, problem_id, youtube_id, video_title, bookmarks)        
    g.serialize(destination=out_file)


# skillDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, problem_id, youtube_id, video_title, bookmarks):
    global eliozo_ns
    global SKOS_NS
    global RDF_NS
    problem_node = rdflib.URIRef(eliozo_ns + problem_id)
    problem_video_property = rdflib.URIRef(eliozo_ns + 'video')
    video_resource = rdflib.BNode()

    rdf_type_property = rdflib.URIRef(RDF_NS + "type")
    rdf_type_value = rdflib.URIRef(eliozo_ns + "Video")

    youtube_id_property = rdflib.URIRef(eliozo_ns+'youtubeID')
    youtube_id_value = rdflib.term.Literal(youtube_id)

    video_title_property = rdflib.URIRef(eliozo_ns + "videoTitle")
    video_title_value = rdflib.term.Literal(video_title)


    g.add((problem_node, problem_video_property, video_resource))
    g.add((video_resource, rdf_type_property, rdf_type_value))
    g.add((video_resource, youtube_id_property, youtube_id_value))
    g.add((video_resource, video_title_property, video_title_value))

    video_bookmark_property = rdflib.URIRef(eliozo_ns + "videoBookmarks")

    video_bookmarks = rdflib.BNode()
    g.add((video_resource, video_bookmark_property, video_bookmarks))

    bookmarks_type_property = rdflib.URIRef(RDF_NS + "Seq")
    g.add((video_bookmarks, rdf_type_property, bookmarks_type_property))

    count = 1
    for (tstamp, bmtext) in bookmarks:
        seq_property = rdflib.URIRef(RDF_NS + "_{}".format(count))
        current_bookmark = rdflib.BNode()
        g.add((video_bookmarks, seq_property, current_bookmark))
        current_bookmark_tstamp_property = rdflib.URIRef(eliozo_ns + "tstamp")
        g.add((current_bookmark, current_bookmark_tstamp_property, rdflib.term.Literal(tstamp, datatype=XSD.integer)))
        current_bookmark_text_property = rdflib.URIRef(eliozo_ns + "bmtext")
        g.add((current_bookmark, current_bookmark_text_property, rdflib.term.Literal(bmtext)))
        count += 1

if __name__ == '__main__':
    getGoogleSpreadsheet()  # Izsauc funkciju, kas iegūst skos dokumentu CSV faila formātā
    readCSVfile(in_file="resources/youtube.csv", out_file="resources/youtube.ttl")
   # produceCSVtoRDF(in_file="youtube.csv", out_file="youtube.ttl")