from flask import Blueprint, abort, render_template, request, send_from_directory, session
from eliozo_dao.references_repository import getSPARQLSources
from eliozo.webmd_utils import fix_image_links, mathBeautify
import os
import re
import markdown
from eliozo.webmd_utils import proc_markdown

references_bp = Blueprint('references_bp', __name__)

# eliozoapp/eliozo/content -- one directory per document, holding one Markdown
# file per language.
CONTENT_ROOT = os.path.normpath(os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', '..', 'eliozo', 'content'))

# Only letters, digits, underscore and hyphen: no '/' and no '.', so a document
# name can never escape CONTENT_ROOT.
_DOC_NAME_RE = re.compile(r'[A-Za-z0-9_-]+')

# Page titles for the documents reachable from the menu. The values must match
# the msgids used in navigation.py so that the breadcrumb is translated too.
# Documents that are not listed still render; they fall back to their directory
# name.
CONTENT_DOC_TITLES = {
    'ontology': 'Ontology',
    'search_by_keyword': 'Exact Search',
    'search_by_regex': 'Regex Search',
    'ontology_topics': 'Topics',
    'ontology_methods': 'Methods',
    'ontology_genres': 'Genres',
    'ontology_question_types': 'Question Types',
    'ontology_concepts': 'Concepts',
    'ontology_olympiads': 'Olympiads',
    'ontology_models': 'Models',
    'ontology_hints': 'Hints',
    'ontology_hint_types': 'Hint Types',
}

# The help page of each metadata type (ontology_<type>) is a subpage of the
# ontology overview in the breadcrumb.
ONTOLOGY_SUBPAGE_PREFIX = 'ontology_'

# Files a document may show besides its text, e.g. the diagram on the
# ontology page: ![...](/content/ontology/klasifikatoru_attiecibu_grafs.svg)
_CONTENT_FILE_RE = re.compile(r'[A-Za-z0-9_-]+\.(?:svg|png|jpg|jpeg|gif)')


def find_content_file(docname, lang):
    """Path of ``content/<docname>/content_<lang>.md``, or None.

    English is the fallback when the requested language is missing.
    """
    if not docname or not _DOC_NAME_RE.fullmatch(docname):
        return None
    doc_dir = os.path.join(CONTENT_ROOT, docname)
    for name in (f'content_{lang}.md', 'content_en.md'):
        path = os.path.join(doc_dir, name)
        if os.path.isfile(path):
            return path
    return None


def render_content_file(path):
    """Markdown file -> HTML, with the same LaTeX handling as problem texts."""
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    html_content = proc_markdown(text)
    return mathBeautify(html_content)

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
    # Kept as its own URL because it is linked from elsewhere; the document
    # itself is loaded by the generic content loader.
    return getContentPage('ontology')


@references_bp.route('/content/<docname>', methods=['GET'])
def getContentPage(docname):
    """Render any Markdown document under eliozo/content/<docname>/.

    With ``?fragment=1`` only the rendered HTML is returned, without the page
    chrome -- that is what the context sensitive help pop-up on the search page
    loads.
    """
    lang = session.get('lang', 'lv')
    file_path = find_content_file(docname, lang)
    if file_path is None:
        abort(404)

    html_content = render_content_file(file_path)
    if request.args.get('fragment'):
        return html_content

    title = CONTENT_DOC_TITLES.get(docname, docname.replace('_', ' ').title())
    navlinks = [{'title': 'About Us'}]
    if docname.startswith(ONTOLOGY_SUBPAGE_PREFIX):
        navlinks.append({'url': 'references_bp.getOntology', 'title': 'Ontology'})
    navlinks.append({'url': 'references_bp.getContentPage',
                     'params': {'docname': docname}, 'title': title})
    template_context = {
        'active': 'about_us',
        'navlinks': navlinks,
        'lang': lang,
        'title': title,
        'content_html': html_content
    }
    return render_template('md_content.html', **template_context)


@references_bp.route('/content/<docname>/<filename>', methods=['GET'])
def getContentFile(docname, filename):
    """An image stored next to the Markdown files of a document."""
    if not _DOC_NAME_RE.fullmatch(docname) or not _CONTENT_FILE_RE.fullmatch(filename):
        abort(404)
    return send_from_directory(os.path.join(CONTENT_ROOT, docname), filename)
