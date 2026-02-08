import requests
from . import FUSEKI_URL

def replace_non_ascii_with_unicode_escape(text):
    non_ascii_characters = {'ā': '\\u0101', 'č': '\\u010D', 'ē': '\\u0113', 'ģ': '\\u0123', 'ī': '\\u012B',
                        'ķ': '\\u0137', 'ļ': '\\u013C', 'ņ': '\\u0146', 'š': '\\u0161', 'ū': '\\u016B',
                        'ž': '\\u017E'}
    replaced_text = ''
    for char in text:
        if char in non_ascii_characters:
            replaced_text += non_ascii_characters[char]
        else:
            replaced_text += char
    return replaced_text

def getProblemsByKeywordSPARQL(thePattern, isCaseSensitive):
    if not isCaseSensitive:
        escapedPattern = thePattern.lower()
        isLcase = 'lcase'
    else:
        escapedPattern = thePattern
        isLcase = ''

    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problem ?problemid ?text ?textHtml ?grade
WHERE {{
    ?problem eliozo:problemID ?problemid ;
    eliozo:problemText ?text ;
    eliozo:problemTextHtml ?textHtml .
    OPTIONAL {{
        ?problem eliozo:problemGrade ?grade .
    }}
    FILTER (contains({lcase}(?text), "{pattern}"))
}} ORDER BY ?grade ?problemid
LIMIT 10
"""
    escapedPattern = escapedPattern.replace('"', '\\"')

    query = queryTemplate.format(pattern=escapedPattern, lcase=isLcase)
    myobj = {'query': query}
    # print(f"***** query in getProblemsByKeywordSPARQL('{thePattern}')")
    # print(query)
    # print("===== END =====")

    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)

    return x.text

def getProblemsByRegexSPARQL(thePattern, isCaseSensitive):
    # so far no escaping pattern
    if not isCaseSensitive:
        escapedPattern = thePattern.lower()
        isLcase = 'lcase'
    else:
        escapedPattern = thePattern
        isLcase = ''

    url = FUSEKI_URL
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problem ?problemid ?text ?textHtml ?grade
WHERE {{
    ?problem eliozo:problemID ?problemid ;
    eliozo:problemText ?text ;
    eliozo:problemTextHtml ?textHtml ;
    OPTIONAL {{
        ?problem eliozo:problemGrade ?grade .
    }}
    FILTER (regex({lcase}(?text), "{pattern}"))
}} ORDER BY ?grade ?problemid
LIMIT 10
"""
    escapedPattern = escapedPattern.replace('"', '\\"')
    escapedPattern = escapedPattern.replace('\\', '\\\\')

    query = queryTemplate.format(pattern=escapedPattern, lcase=isLcase)
    myobj = {'query': query}
    # print(f"***** query in getProblemsByRegexSPARQL('{thePattern}')")
    # print(query)
    # print("===== END =====")

    head = {'Content-Type': 'application/x-www-form-urlencoded'}
    x = requests.post(url, myobj, head)

    return x.text
