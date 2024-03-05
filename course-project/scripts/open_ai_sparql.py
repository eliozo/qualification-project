from openai import OpenAI
import configparser
client = OpenAI()

def get_openai_client():
    configParser = configparser.RawConfigParser()
    configFilePath = 'properties.txt'
    configParser.read(configFilePath)
    client = OpenAI(
        # This is the default and can be omitted
        api_key=configParser.get('your-config', 'api_key'),
    )
    return client

# client = get_openai_client()

query = """
Consider RDF dataset with the following namespace prefixes: 
``` sparql
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
```
Consider the following training set with respective sparql queries and their description
```
{
  "description": "Find all problems on Algebraic transactions involving binomial square formula. Skills are selected by year of assignment and sorted from lowest to highest year",
  "SPARQL": "PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>\nPREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>\nPREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>\nSELECT ?sub WHERE {\n?sub eliozo:skill \"alg.tra.binom.square\" ;\n     eliozo:year ?year\n} ORDER BY ASC(?year)"
}
```
Please convert the following description to SPARQL: All problems on algebraic transactions binomial square formula for 2002.
"""

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are an assistant, that translates search queries described in English into SPARQL query. Please return just unquoted SPARQL and without explanaitons"},
    {"role": "user", "content": query }
  ]
)

print(completion.choices[0].message.content)