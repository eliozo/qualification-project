# from mistletoe import Document, HTMLRenderer
import mistletoe
import mistletoe.ast_renderer
import requests
import csv
from json_reader import *

file_path = "out.json"

def getGoogleSpreadsheet():
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vT1Il_-qJURh8sZHRN1oJSwok4kRUjcA7VCOhDfg1PnTUC14k4skRRl3NrUDEbd1vELQq_ALwEU9Ltx/pub?output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("spreadsheet.csv", "wb").write(response.content)

def readCSVfile():
    result = []
    with open('spreadsheet.csv', 'r',  encoding='utf-8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                row_1 = row[1][45:]
                result.append((row_1, row[3]))
                print(f'\t {row_1}')
                line_count += 1
        print(f'Processed {line_count} lines.')
    return result

def convertToJSON(URL_suffix):
    my_path = 'C:/Users/eliz_/Documents/math/'+URL_suffix[0]+'/content.md'
    print(my_path)
    with open(my_path, 'r', encoding='utf-8') as fin:
        with mistletoe.ast_renderer.ASTRenderer() as renderer:     # or: `with HTMLRenderer(AnotherToken1, AnotherToken2) as renderer:`
            doc = mistletoe.Document(fin)              # parse the lines into AST
            rendered = renderer.render(doc)  # render the AST
            # internal lists of tokens to be parsed are automatically reset when exiting this `with` block
            # print("URL Suffix: '{}' ".format(URL_suffix[1]))
            out_file = open(URL_suffix[1]+'-'+file_path, "w", encoding='utf-8')
            out_file.write(rendered)
            out_file.close()
    produceRDF(URL_suffix[1]+'-'+file_path, URL_suffix[1]+'-'+'tbl.ttl')
    

if __name__ == '__main__':
    # Nolasīt visus URL suffixus no Google Spreadsheet
    getGoogleSpreadsheet()
    results = readCSVfile() # 4 apakšdirektorijas ar uzdevumiem AO, VO utt.
    for result in results:
        convertToJSON(result)
    # Kopē failus uz savu build direktoriju
    # Pārveidot par JSON
    # Pārveidot par RDF 