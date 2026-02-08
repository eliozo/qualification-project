from flask import url_for, session
from flask_babel import _

def get_navigation():
    """
    Returns the navigation structure for the application.
    Each item is a dictionary with:
    - label: Display text (localized)
    - endpoint: Flask endpoint name (optional)
    - url_params: Parameters for url_for (optional)
    - active_key: Key to match against 'active' variable in template
    - children: List of sub-items (optional)
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
            'endpoint': 'getFilter',
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
            'endpoint': 'getWorksheets',
            'active_key': 'worksheets',
            'condition': show_worksheets
        },
        {
            'label': _('About Us'),
            'active_key': 'about_us',
            'children': [
                {'label': _('References'), 'endpoint': 'references_bp.getReferences'},
                {'label': _('Contact Information'), 'endpoint': 'references_bp.getContactInfo'},
                {'label': _('Ontology'), 'endpoint': 'references_bp.getOntology'},
            ]
        }
    ]

    # Process items to generate URLs and filter by condition
    final_nav = []
    for item in nav_items:
        if item.get('condition', True):
            # Process main item
            if 'endpoint' in item:
                item['url'] = url_for(item['endpoint'], **item.get('url_params', {}))
            else:
                item['url'] = '#' # Placeholder for dropdowns without direct link

            # Process children
            if 'children' in item:
                final_children = []
                for child in item['children']:
                    if child.get('condition', True):
                        if 'endpoint' in child:
                            child['url'] = url_for(child['endpoint'], **child.get('url_params', {}))
                        final_children.append(child)
                item['children'] = final_children
            
            final_nav.append(item)

    return final_nav
