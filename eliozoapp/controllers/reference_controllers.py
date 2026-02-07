from flask import render_template, session
from eliozo_dao.sparql_access import SparqlAccess
from eliozo.webmd_utils import fix_image_links, mathBeautify

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


def getOntology():
    lang = session.get('lang', 'lv')
    import os
    import markdown
    from eliozo.webmd_utils import proc_markdown

    # Define path to markdown files
    # Assumes structure: eliozoapp/eliozo/content/ontology/ontology_{lang}.md
    base_dir = os.path.dirname(os.path.abspath(__file__))
    content_dir = os.path.join(base_dir, '..', 'eliozo', 'content', 'ontology')
    file_path = os.path.join(content_dir, f'ontology_{lang}.md')

    # Fallback to English if file doesn't exist
    if not os.path.exists(file_path):
        file_path = os.path.join(content_dir, 'ontology_en.md')
    
    html_content = ""
    if os.path.exists(file_path):
         with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            html_content = proc_markdown(text)
            html_content = mathBeautify(html_content)

    template_context = {
        'active': 'about_us',
        'navlinks': [
            {'title':'About Us'},
            {'url': 'getOntology', 'title': 'Ontology'}
        ],
        'lang': lang,
        'title': 'Ontology',
        'ontology_html': html_content
    }
    return render_template('ontology_content.html', **template_context)