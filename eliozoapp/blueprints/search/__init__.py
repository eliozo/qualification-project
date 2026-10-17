import logging

from flask import Blueprint, render_template, request, session

from blueprints.paging import page_links, parse_offset
from eliozo.webmd_utils import fix_image_links, mathBeautify
from eliozo_dao.search_repository import (
    SEARCH_MODE_SEMANTIC,
    SEARCH_TARGET_PROBLEMS,
    SEARCH_TARGET_SOLUTIONS,
    searchProblems,
    semanticSearchProblems,
)

logger = logging.getLogger(__name__)

search_bp = Blueprint('search_bp', __name__)

@search_bp.route('/', methods=['GET', 'POST'])
def search_problems():
    keyword = request.args.get('keyword')
    if 'clickcount' in session:
        clickcount = session['clickcount']
    else:
        clickcount = 0
    # print(f"clickcount = {clickcount}")

    searchTarget = request.args.get('searchTarget', SEARCH_TARGET_PROBLEMS)
    if searchTarget != SEARCH_TARGET_SOLUTIONS:
        searchTarget = SEARCH_TARGET_PROBLEMS

    if keyword is None or keyword == "":
        template_context = {
            'active': 'main',
            'searchMode': 'exact',
            'searchTarget': searchTarget
        }
        return render_template('main_content.html',  **template_context)

    searchMode = request.args.get('searchMode')

    problems = []
    pageLinks = []
    searchError = None

    offset = parse_offset(request.args.get('offset'))
    uiLang = session.get('lang', 'lv')
    try:
        if searchMode == SEARCH_MODE_SEMANTIC:
            result = semanticSearchProblems(keyword, searchTarget, uiLang=uiLang, offset=offset)
        else:
            result = searchProblems(keyword, searchMode, searchTarget, uiLang=uiLang, offset=offset)
    except Exception:
        # Search by meaning needs PostgreSQL and the embedding API; show the
        # failure instead of an error page.
        if searchMode != SEARCH_MODE_SEMANTIC:
            raise
        logger.exception('Semantic search failed for %r', keyword)
        searchError = 'semantic'
        result = {'total': 0, 'problems': []}

    for item in result['problems']:
        problem_text_value = mathBeautify(item['textHtml'])
        problem_text_value = fix_image_links(problem_text_value)
        d = {'problemid': item['problemid'], 'text': problem_text_value, 'imagefile': '',
             'matchLang': item['matchLang'], 'solutionMatchLang': item['solutionMatchLang']}
        problems.append(d)

    pageLinks = page_links(result['total'], offset, 'search_bp.search_problems',
                           {'keyword': keyword, 'searchMode': searchMode,
                            'searchTarget': searchTarget})

    template_context = {
        'problems': problems,
        'page_links': pageLinks,
        'keyword' : keyword,
        'active': 'main',
        'searchMode': searchMode,
        'searchTarget': searchTarget,
        'searchError': searchError,
        'lang': session.get('lang', 'lv'),
        'title': 'Sākumlapa',
        'clickcount': clickcount
    }
    return render_template('main_content.html', **template_context)
