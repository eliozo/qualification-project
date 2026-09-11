from flask import Blueprint, abort, render_template, request, session
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
}


def find_content_file(docname, lang):
    """Path of the best Markdown file for ``docname`` in ``lang``, or None.

    Both naming conventions in use are accepted -- ``content_lv.md`` (new
    documents) and ``<docname>_lv.md`` (the ontology) -- and English is the
    fallback when the requested language is missing.
    """
    if not docname or not _DOC_NAME_RE.fullmatch(docname):
        return None
    doc_dir = os.path.join(CONTENT_ROOT, docname)
    candidates = [f'content_{lang}.md', f'{docname}_{lang}.md',
                  'content_en.md', f'{docname}_en.md']
    for name in candidates:
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
    lang = session.get('lang', 'lv')
    file_path = find_content_file('ontology', lang)
    html_content = render_content_file(file_path) if file_path else ""

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
    template_context = {
        'active': 'about_us',
        'navlinks': [
            {'title': 'About Us'},
            {'url': 'references_bp.getContentPage',
             'params': {'docname': docname}, 'title': title}
        ],
        'lang': lang,
        'title': title,
        'content_html': html_content
    }
    return render_template('md_content.html', **template_context)
