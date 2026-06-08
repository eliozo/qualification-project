import json

from . import sparql_query


def getSPARQLSources(lang):
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
    response = sparql_query(queryTemplate.format(language=lang))
    items = json.loads(response)
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
