from flask import render_template, session
from eliozo_dao.sparql_access import SparqlAccess

def getReferences():
    # return render_template("info.html")
    lang = session.get('lang', 'lv')
    fuseki_url = 'http://127.0.0.1:9080/jena-fuseki-war-4.7.0/abc/'
    sparql_access = SparqlAccess(fuseki_url)
    sources = sparql_access.getSPARQLSources(lang)
    template_context = {
        'active': 'about_us',
        'navlinks': [
            { 'title':'About Us' },
            { 'url': 'getReferences', 'title': 'References'}
        ],
        'lang': lang,
        'sources': sources,
        'title': 'Atsauces'
    }
    return render_template('references_content.html', **template_context)


def getContactInfo():
    lang = session.get('lang', 'lv')
    template_context = {
        'active': 'about_us',
        'navlinks': [
            {'title':'About Us'},
            {'url': 'getContactInfo', 'title': 'Contact Information'}
        ],
        'lang': lang,
        'title': 'Contact Information'
    }
    return render_template('contactinfo_content.html', **template_context)