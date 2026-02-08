from flask import Blueprint, render_template, session
from eliozo_dao.references_repository import getSPARQLSources
from eliozo.webmd_utils import fix_image_links, mathBeautify
import os
import markdown
from eliozo.webmd_utils import proc_markdown

references_bp = Blueprint('references_bp', __name__)

@references_bp.route('/references', methods=['GET'])
def getReferences():
    # return render_template("info.html")
    lang = session.get('lang', 'lv')
    sources = getSPARQLSources(lang)
    template_context = {
        'active': 'about_us',
        'navlinks': [
            { 'title':'About Us' },
            { 'url': 'references_bp.getReferences', 'title': 'References'}
        ],
        'lang': lang,
        'sources': sources,
        'title': 'Atsauces'
    }
    return render_template('references_content.html', **template_context)


@references_bp.route('/contact_info', methods=['GET'])
def getContactInfo():
    lang = session.get('lang', 'lv')
    template_context = {
        'active': 'about_us',
        'navlinks': [
            {'title':'About Us'},
            {'url': 'references_bp.getContactInfo', 'title': 'Contact Information'}
        ],
        'lang': lang,
        'title': 'Contact Information'
    }
    return render_template('contactinfo_content.html', **template_context)


@references_bp.route('/ontology', methods=['GET'])
def getOntology():
    lang = session.get('lang', 'lv')
    
    # Define path to markdown files
    # Assumes structure: eliozoapp/eliozo/content/ontology/ontology_{lang}.md
    # We need to find base_dir relative to this blueprint file
    # This might need adjustment depending on where this file is located relative to content
    # Current location: eliozoapp/blueprints/references/__init__.py
    # Content location: eliozoapp/eliozo/content/ontology
    
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Go up two levels to eliozoapp, then down to eliozo/content/ontology
    content_dir = os.path.join(base_dir, '..', '..', 'eliozo', 'content', 'ontology')
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
            {'url': 'references_bp.getOntology', 'title': 'Ontology'}
        ],
        'lang': lang,
        'title': 'Ontology',
        'ontology_html': html_content
    }
    return render_template('ontology_content.html', **template_context)
