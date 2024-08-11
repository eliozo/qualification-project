import mistletoe
import mistletoe.ast_renderer
import requests
import csv
from json_reader import *
from mdchunk_reader import *
from csv_to_skos import *

# file_path = "out.json"

def getGoogleSpreadsheet():  # Funkcija, kas iegūst Google Spreadsheet dokumentu ar olimpiāžu uzdevumu datiem
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("resources/spreadsheet.csv", "wb").write(response.content)

# Atgriežam sarakstu, kurā ir pārīši row_1, row[3]
def readCSVfile():  # Funkcija, kas lasa CSV failu
    result = []
    with open('resources/spreadsheet.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                result.append((row[1], row[2], row[4]))
                line_count += 1
        print(f'Processed {line_count} lines.')
    return result

def getMarkdownFile(URL, content_file_name, file_suffix): # Funkcija, kas iegūst Markdown failu no GitHub repozitorija
    # print(f'URL = {URL}')
    URL = URL.replace('github.com','raw.githubusercontent.com')
    URL = URL + '/' + content_file_name + '.md'
    URL = URL.replace('/tree', '')
    print(f'Getting markdown: {URL}')
    response = requests.get(URL)
    open('resources/'+file_suffix+'-'+content_file_name + '.md', "wb").write(response.content)

def convertToJSON(URL_suffix):  # Pārveido Markdown failu par JSON failu
    # my_path = 'C:/Users/eliz_/Documents/math/'+URL_suffix[0]+'/content.md'
    my_path = 'resources/'+URL_suffix[2]+'-'+ URL_suffix[1] + '.md'
    print(my_path)
    with open(my_path, 'r', encoding='utf-8') as fin:
        with mistletoe.ast_renderer.ASTRenderer() as renderer:
            doc = mistletoe.Document(fin)
            rendered = renderer.render(doc)
            out_file = open('resources/'+URL_suffix[2]+'-'+URL_suffix[1] + '.json', "w", encoding='utf-8')
            out_file.write(rendered)
            out_file.close()
    # Izsauc funkciju no json_reader.py, kas pārveido olimpiāžu uzd datus no JSON par RDF
    produceRDF('resources/'+URL_suffix[2]+'-'+URL_suffix[1], 'resources/'+URL_suffix[2]+'-'+URL_suffix[1]+'.ttl')


if __name__ == '__main__':
    # Nolasa apstrādājamo olimpiāžu sarakstu no Google Docs izklājlapas
    getGoogleSpreadsheet()
    # Pārīši [('https://github.com/kapsitis/math/tree/master/src/site/problembase/numtheory-lv-ao', 'LV-AO')] utml.
    results = readCSVfile()

    # Testēšanai tikai viens pārītis:
    # results = [('https://github.com/kapsitis/math/tree/master/src/site/problembase/imo-shl-2022', 'content', 'IMO-SHL-2022')]
    # results = [('https://github.com/maramanaa/nms-uzdevumi/tree/main/lv-amo-2011', 'content', 'LV-AMO-2011')]

    for result in results:
        # print("****{}, {}, {}".format(result[0], result[1], result[2]))
        getMarkdownFile(result[0].strip(), result[1].strip(), result[2].strip())
        md_path = 'resources/' + result[2] + '-' + result[1].strip() + '.md'
        ttl_path = 'resources/' + result[2] + '-' + result[1].strip() + '.ttl'
        md_to_rdf(md_path, ttl_path)


        # convertToJSON(result)
