from flask import Blueprint, abort, render_template, request, send_from_directory, session
from eliozo_dao.references_repository import getSPARQLSources
from eliozo.webmd_utils import fix_image_links, mathBeautify
import os
import re
import markdown
from eliozo.webmd_utils import proc_markdown
from eliozo.content_docs import (CONTENT_ROOT, DOC_NAME_RE, ONTOLOGY_DOC, ONTOLOGY_SUBPAGES,
                                 content_doc_title, find_content_file)

references_bp = Blueprint('references_bp', __name__)

# Page titles for the documents reachable from the menu. The values must match
# the msgids used in navigation.py so that the breadcrumb is translated too.
# The ontology documents use their own first heading instead; other documents
# that are not listed fall back to their directory name.
CONTENT_DOC_TITLES = {
    'search_by_keyword': 'Exact Search',
    'search_by_regex': 'Regex Search',
    'search_by_meaning': 'Semantic Search',
}

# Help documents of the plain search modes, under "Info > Plain Search".
PLAIN_SEARCH_DOCS = ('search_by_keyword', 'search_by_regex', 'search_by_meaning')

# The top-level menu item all these pages belong to (msgid in navigation.py).
INFO_MENU_TITLE = 'Info'

# Files a document may show besides its text, e.g. the diagram on the
# ontology page: ![...](/content/ontology/klasifikatoru_attiecibu_grafs.svg)
_CONTENT_FILE_RE = re.compile(r'[A-Za-z0-9_-]+\.(?:svg|png|jpg|jpeg|gif)')


def _doc_title(docname, lang):
    if docname == ONTOLOGY_DOC or docname in ONTOLOGY_SUBPAGES:
        title = content_doc_title(docname, lang)
        if title:
            return title
    return CONTENT_DOC_TITLES.get(docname, docname.replace('_', ' ').title())


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
            { 'title': INFO_MENU_TITLE },
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
            {'title': INFO_MENU_TITLE},
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

    title = _doc_title(docname, lang)
    navlinks = [{'title': INFO_MENU_TITLE}]
    if docname in PLAIN_SEARCH_DOCS:
        navlinks.append({'title': 'Plain Search'})
    if docname in ONTOLOGY_SUBPAGES:
        navlinks.append({'url': 'references_bp.getOntology', 'title': _doc_title(ONTOLOGY_DOC, lang)})
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
    if not DOC_NAME_RE.fullmatch(docname) or not _CONTENT_FILE_RE.fullmatch(filename):
        abort(404)
    return send_from_directory(os.path.join(CONTENT_ROOT, docname), filename)
