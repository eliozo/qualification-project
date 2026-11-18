from flask import url_for, session, request
from flask_babel import _

from .content_docs import ONTOLOGY_SUBPAGES, content_doc_title


def _advanced_search_menu(lang):
    """'Advanced Search': the ontology overview (classes and properties for
    writing SPARQL queries) with its child documents as a nested menu; the
    item itself opens the overview."""
    return {
        'label': _('Advanced Search'),
        'endpoint': 'references_bp.getOntology',
        'children': [
            {'label': content_doc_title(doc, lang) or doc,
             'endpoint': 'references_bp.getContentPage', 'url_params': {'docname': doc}}
            for doc in ONTOLOGY_SUBPAGES
        ],
    }


def _plain_search_menu():
    """'Plain Search': only a navigation node (no page of its own) with the
    help documents of the search modes of the main page ("/"), in the order
    of its radio buttons."""
    def doc(label, docname):
        return {'label': label, 'endpoint': 'references_bp.getContentPage',
                'url_params': {'docname': docname}}
    return {
        'label': _('Plain Search'),
        'children': [
            doc(_('Exact Search'), 'search_by_keyword'),
            doc(_('Regex Search'), 'search_by_regex'),
            doc(_('Semantic Search'), 'search_by_meaning'),
        ],
    }


def _process(items, current_path):
    """Resolve the URLs of visible items, recursively; mark the current page and its ancestors."""
    result = []
    for item in items:
        if not item.get('condition', True):
            continue
        if 'endpoint' in item:
            item['url'] = url_for(item['endpoint'], **item.get('url_params', {}))
        else:
            item['url'] = '#'  # Placeholder for dropdowns without direct link
        item['current'] = item['url'] == current_path
        if 'children' in item:
            item['children'] = _process(item['children'], current_path)
            # Open a nested menu when the current page is in it
            item['expanded'] = any(c['current'] or c.get('expanded') for c in item['children'])
        result.append(item)
    return result

def get_navigation():
    """
    Returns the navigation structure for the application.
    Each item is a dictionary with:
    - label: Display text (localized)
    - endpoint: Flask endpoint name (optional)
    - url_params: Parameters for url_for (optional)
    - active_key: Key to match against 'active' variable in template
    - children: List of sub-items (optional); a child may have children of its own
      (a nested menu, e.g. Info > Advanced Search > Question Types)
    - condition: Boolean to determine visibility (optional, default True)
    """
    
    # Check clickcount for Worksheets visibility
    clickcount = session.get('clickcount', 0)
    show_worksheets = clickcount >= 7

    nav_items = [
        {
            'label': _('Home'),
            'endpoint': 'search_bp.search_problems',
            'active_key': 'main'
        },
        {
            'label': _('Filters'),
            'endpoint': 'filter.getFilter',
            'active_key': 'filter'
        },
        {
            'label': _('Archive'),
            'active_key': 'archive',
            'children': [
                {'label': _('Olympiads'), 'endpoint': 'problems.getOlympiads'},
                {'label': _('Video'), 'endpoint': 'problems.getVideo'},
            ]
        },        
        {
            'label': _('Order'),
            'active_key': 'order_by',
            'children': [
                {'label': _('by Topic'), 'endpoint': 'indexes.getTopics'},
                {'label': _('by Method'), 'endpoint': 'indexes.getMethods'},
                {'label': _('by Genre'), 'endpoint': 'indexes.getGenres'},
                {'label': _('by Concept'), 'endpoint': 'indexes.getConcepts'},
                {'label': _('Topics Table'), 'endpoint': 'indexes.getTopicsTable'},
            ]
        },
        {
            'label': _('Reports'),
            'active_key': 'statistics',
            'children': [
                {'label': _('Olympiad Curriculum'), 'endpoint': 'curriculum_bp.getCurriculum'},
                {'label': _('Problem Count'), 'endpoint': 'stats_bp.getProblemCounts'},
                {'label': _('Property Usage'), 'endpoint': 'stats_bp.getPropertyCounts'},
                {'label': _('Result Summary'), 'endpoint': 'stats_bp.getResults'},
            ]
        },
        {
            'label': _('Worksheets'),
            'active_key': 'worksheets',
            'condition': show_worksheets,
            'children': [
                {'label': _('Worksheets'), 'endpoint': 'worksheets.getWorksheets'},
            ]
        },
        {
            # References, the authors, and help on searching (plain search
            # modes and the ontology for SPARQL queries)
            'label': _('Info'),
            'active_key': 'about_us',
            'children': [
                {'label': _('References'), 'endpoint': 'references_bp.getReferences'},
                {'label': _('Contact Information'), 'endpoint': 'references_bp.getContactInfo'},
                _plain_search_menu(),
                _advanced_search_menu(session.get('lang', 'lv')),
            ]
        }
    ]

    # Add login/logout based on session
    if 'user' in session:
        username = session['user'].get('name', 'User')
        nav_items[5]['children'].append({'label': f"Welcome, {username}", 'endpoint': 'dashboard'})
        nav_items[5]['children'].append({'label': _('Logout'), 'endpoint': 'logout'})
    else:
        nav_items[5]['children'].append({'label': _('Login'), 'endpoint': 'login'})

    return _process(nav_items, request.path)
