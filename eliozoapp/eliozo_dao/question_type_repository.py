import json
import re

from . import sparql_query

# Language-tagged texts of an eliozo:Question (see questionTypes2.csv)
_TEXT_PROPERTIES = {
    'questionName': 'name',
    'questionCanonical': 'canonical',
    'questionDescription': 'description',
    'questionRequiredParts': 'requiredParts',
}


def getSPARQLQuestionTypes():
    queryTemplate = """
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?id ?L1 ?L2 ?parent ?property ?value WHERE {
        ?q a eliozo:Question ;
           eliozo:questionID ?id ;
           eliozo:sorter_L1 ?L1 ;
           eliozo:sorter_L2 ?L2 .
        OPTIONAL { ?q skos:broader/eliozo:questionID ?parent . }
        OPTIONAL {
            VALUES ?property { eliozo:questionName eliozo:questionCanonical
                               eliozo:questionDescription eliozo:questionRequiredParts }
            ?q ?property ?value .
        }
    } ORDER BY ?L1 ?L2
    """
    return sparql_query(queryTemplate)


def getQuestionTypes(lang):
    """The question types in vocabulary order: {id: {'id', 'parent', 'isGroup', 'name',
    'canonical', 'description', 'requiredParts'}}, texts in *lang* ('lv'; others get
    English), falling back to any other language."""
    preferred = ['lv', 'en'] if lang == 'lv' else ['en', 'lv']
    types, texts = {}, {}
    for row in json.loads(getSPARQLQuestionTypes())['results']['bindings']:
        qid = row['id']['value']
        types.setdefault(qid, {
            'id': qid,
            'parent': row.get('parent', {}).get('value'),
            'isGroup': row['L2']['value'] == '0',
        })
        if 'value' in row:
            key = _TEXT_PROPERTIES[row['property']['value'].rsplit('#', 1)[-1]]
            texts.setdefault((qid, key), {})[row['value'].get('xml:lang', '')] = row['value']['value']
    for qid, info in types.items():
        for key in _TEXT_PROPERTIES.values():
            by_lang = texts.get((qid, key), {})
            info[key] = next((by_lang[l] for l in preferred if l in by_lang), next(iter(by_lang.values()), ''))
        info['name'] = info['name'] or qid
    # Descriptions refer to other types by ID ("... izvēlas QTY_FindAll"): show their names instead
    for info in types.values():
        for key in ('description', 'requiredParts'):
            info[key] = re.sub(r'\b(?:QTY|RSP)_\w+',
                               lambda m: f'"{types[m.group(0)]["name"]}"' if m.group(0) in types else m.group(0),
                               info[key])
    return types


def questionTypeName(question_types, qid):
    """Display name of a question type; the raw ID only for values missing from the vocabulary."""
    return question_types[qid]['name'] if qid in question_types else qid
