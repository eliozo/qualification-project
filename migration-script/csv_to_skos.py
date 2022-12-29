from rdflib import Graph, Namespace, URIRef, Literal, RDF
import csv
import json
import requests

def getGoogleSpreadsheet():
    URL_GOOGLE_SPREADSHEET = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vQvAsYeFYhuFLmLgtMiYFeQFeeO4e0DgteRXRg1zpQ2iMcWZr-mIgdyDYnh1IoKq4l5v9C-JAE1-Qcy/pub?output=csv'
    response = requests.get(URL_GOOGLE_SPREADSHEET)
    open("spreadsheet_skos.csv", "wb").write(response.content)

# def readCSVfile():
#     result = []
#     with open('spreadsheet_skos.csv', 'r',  encoding='utf-8') as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=',')
#         line_count = 0
#         for row in csv_reader:
#             if line_count == 0:
#                 print(f'Column names are {", ".join(row)}')
#                 line_count += 1
#             else:
#                 row_1 = row[1]
#                 # result.append((row_1, row[3]))
#                 print(f'\t {row_1}')
#                 line_count += 1
#         print(f'Processed {line_count} lines.')
#     return result

# Varbūt var arī iztikt bez konvertēšanas uz JSON un izmantot tikai CSV failu, lai pievienotu SKOS grafam utt?
def csvToJSON(csvFilePath, jsonFilePath):
    jsonArray = []

    # Read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # Load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # Convert each csv row into python dict
        for row in csvReader:
            # Add this python dict to json array
            jsonArray.append(row)

    # Convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)


def produceRDF(in_file, out_file):
    SKOS = Namespace("http://www.w3.org/2004/02/skos/core#")

    g = Namespace.Graph()

    g.bind("skos", SKOS)

    # Opening JSON file
    f = open(in_file)

if __name__ == '__main__':
    # Izsauc funkciju, kas iegūst skos dokumentu CSV faila formātā
    getGoogleSpreadsheet()
    # Izsauc funkciju, kas lasa CSV failu un drukā noteiktu saturu no tā
    # readCSVfile()
    # Izsauc funkciju, kas pārveido csv failu uz json formātu
    csvToJSON(csvFilePath="spreadsheet_skos.csv", jsonFilePath="skos.json")

