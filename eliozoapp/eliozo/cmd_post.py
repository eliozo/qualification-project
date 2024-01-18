import requests

url = 'http://localhost:9080/jena-fuseki-war-4.7.0/abc/'
myobj = {'query': 'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\n'+
'PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\n'+
'PREFIX skos: <http://www.w3.org/2004/02/skos/core#>\n'+
'PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\n'+
'SELECT * WHERE { ?sub eliozo:skill ?obj . ?obj skos:prefLabel ?label . } LIMIT 10\n'
}

head = {'Content-Type' : 'application/x-www-form-urlencoded'}

x = requests.post(url, myobj, head)

print(x.text)