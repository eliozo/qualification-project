from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import rdflib
import requests

eozol_ns = "http://www.dudajevagatve.lv/eozol#"

SKOS_NS = "http://www.w3.org/2004/02/skos/core#"

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"

def getGoogleSpreadsheet():  # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("spreadsheet_skos.csv", "wb").write(response.content)


def readCSVfile(g):  # Funkcija, kas lasa CSV failu
    result = []
    with open('spreadsheet_skos.csv', 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line_count += 1
            if line_count == 1:
                continue
            skill_numeric_id = row[0] + '.' + row[1] + '.' + row[2] + '.' + row[3] + '.' + row[4]
            skill_id = row[5]
            skill_prefLabel = row[5]
            skill_description = row[6]
            x = skill_id.rfind(".")
            if x == -1:
                parent_skill_id = ''  # Nav vecāka
            else:
                parent_skill_id = skill_id[:x]
            addToRdfGraph(g, skill_numeric_id, skill_id, skill_description, skill_prefLabel, parent_skill_id)


# skillDescription ir string mainīgais, kurā glabājas RDF objekta vērtība
def addToRdfGraph(g, problem_id, video_id, video_youtube_link, video_title, video_length, bookmarks):
    global eozol_ns
    global SKOS_NS
    global RDF_NS
    problem_node = rdflib.URIRef(eozol_ns + problem_id)
    problem_video_property = rdflib.URIRef(eozol_ns + 'video')
    # video_resource = rdflib.URIRef(eozol_ns + video_id)
    video_resource = rdflib.BNode()

    rdf_type_property = rdflib.URIRef(RDF_NS + "type")
    rdf_type_value = rdflib.URIRef(eozol_ns + "Video")

    video_youtube_property = rdflib.URIRef(eozol_ns + "videoYoutube")
    video_youtube_value = rdflib.term.Literal(video_youtube_link)

    video_title_property = rdflib.URIRef(eozol_ns + "videoTitle")
    video_title_value = rdflib.term.Literal(video_title)

    video_length_property = rdflib.URIRef(eozol_ns + "videoLength")
    video_length_value = rdflib.term.Literal(video_length)


    g.add((problem_node, problem_video_property, video_resource))
    g.add((video_resource, rdf_type_property, rdf_type_value))
    g.add((video_resource, video_youtube_property, video_youtube_value))
    g.add((video_resource, video_title_property, video_title_value))
    g.add((video_resource, video_length_property, video_length_value))

    video_bookmark_property = rdflib.URIRef(eozol_ns + "videoBookmarks")

    video_bookmarks = rdflib.BNode()
    g.add((video_resource, video_bookmark_property, video_bookmarks))

    bookmarks_type_property = rdflib.URIRef(RDF_NS + "Seq")
    g.add((video_bookmarks, rdf_type_property, bookmarks_type_property))

    count = 1
    for (tstamp, bmtext) in bookmarks:
        seq_property = rdflib.URIRef(RDF_NS + "_{}".format(count))
        current_bookmark = rdflib.BNode()
        g.add((video_bookmarks, seq_property, current_bookmark))
        current_bookmark_tstamp_property = rdflib.URIRef(eozol_ns + "tstamp")
        g.add((current_bookmark, current_bookmark_tstamp_property, rdflib.term.Literal(tstamp)))
        current_bookmark_text_property = rdflib.URIRef(eozol_ns + "bmtext")
        g.add((current_bookmark, current_bookmark_text_property, rdflib.term.Literal(bmtext)))
        count += 1


def produceCSVtoRDF(in_file, out_file):  # Pārveido CSV failu par RDF failu

    global SKOS_NS
    global eozol_ns

    g = rdflib.Graph()

    g.bind("skos", SKOS_NS)
    g.bind("eozol", eozol_ns)

    # Atver JSON failu
    # f = open(in_file)

    # readCSVfile(g)


    problem_id = "LV.AO.2011.5.1"
    video_id = "LV.AO.2011.5.1.video"
    video_youtube_link = "https://www.youtube.com/watch?v=tWx-UGFeuSA"
    video_title = "AMO2011, 5.klases 1.uzdevums"
    video_length = "475"



    bookmarks = [("0:05", "Uzdevuma saprašana: Piemērā abi reizinātāji ir īsti divciparu skaitļi."),
                 ("0:45", "Uzdevuma saprašana: Kādēļ pilnā pārlase neder?"),
                 ("1:18", "Uzdevuma saprašana: Izmantojam vienādības labo pusi, lai samazinātu meklējumu telpu."),
                 ("2:00", "Risinājums: Skaitļa 111 izteikšana ar reizinājumu. Metode: Dalīšana pirmreizinātājos."),
                 ("2:55", "Risinājums: Izsakām visus EEE skaitļus kā reizinājumus. Metode: Gadījumu pārlase."),
                 ("3:40", "Risinājums: Kādēļ kreisajā pusē jābūt 37 vai 74? Metode: Dalāmība veselu skaitļu vienādojumā."),
                 ("5:43", "Risinājums: Nederīgo reizinājumu atmešana. Metode: Izslēgšanas metode."),
                 ("7:08", "Atskats: Atbildes formulējums; reizinātāju mainīšana vietām atbilžu skaitu formāli palielina.")]


    addToRdfGraph(g, problem_id, video_id, video_youtube_link, video_title, video_length, bookmarks)

    g.serialize(destination=out_file)


if __name__ == '__main__':
    # getGoogleSpreadsheet()  # Izsauc funkciju, kas iegūst skos dokumentu CSV faila formātā
    produceCSVtoRDF(in_file="spreadsheet_skos.csv", out_file="youtube.ttl")