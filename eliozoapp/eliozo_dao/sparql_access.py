import json
import requests

class SparqlAccess:
    fuseki_url = 'NA'

    def __init__(self, fuseki_url): 
        self.fuseki_url = fuseki_url

    def get_message(self): 
        return f'Hello {self.fuseki_url}'

    def getSPARQLSources(self, lang): 
        queryTemplate = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
        PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
        SELECT DISTINCT ?srcLabel ?srcName ?srcDescription ?srcUrl WHERE {{ 
        ?src eliozo:sourceLabel ?srcLabel ;
            eliozo:sourceName ?srcName ;
            eliozo:sourceDescription ?srcDescription ; 
            eliozo:sourceUrl ?srcUrl .
        FILTER (lang(?srcName) = "{language}")
        FILTER (lang(?srcDescription) = "{language}")  
        }} ORDER BY ?srcLabel ?srcName
        """
        actual_query = queryTemplate.format(language=lang)
        myobj = {'query':  actual_query}
        head = {'Content-Type': 'application/x-www-form-urlencoded'}
        x = requests.post(self.fuseki_url, myobj, head)

        items = json.loads(x.text)
        itemData = []
        for rr in items['results']['bindings']:
            srcLabel = rr['srcLabel']['value']
            srcName = rr['srcName']['value']
            srcDescription = rr['srcDescription']['value']
            srcUrl = rr['srcUrl']['value']
            itemData.append({'label': srcLabel, 
                             'name': srcName, 
                             'description': srcDescription, 
                             'url': srcUrl})
        return itemData
    
