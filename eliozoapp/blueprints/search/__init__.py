from flask import Blueprint, render_template, request, session
import os
from dotenv import load_dotenv

# Add path to weaviate_utils if needed, or assume it's in python path
# based on imports in other files, controllers seems to be a package
from controllers.weaviate_utils import WeaviateUtils

from blueprints.paging import page_links, parse_offset
from eliozo.webmd_utils import fix_image_links, mathBeautify
from eliozo_dao.search_repository import (
    SEARCH_TARGET_PROBLEMS,
    SEARCH_TARGET_SOLUTIONS,
    searchProblems
)

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

    if searchMode == 'semantic':
        # Load env vars for Weaviate
        # env_path = "/Users/kapsitis/workspace-public/worksheet-generation-with-llms/tests/.env"
        # override=True ensures we pick up the values from this file even if env has others
        #load_dotenv(env_path, override=True)

        weaviate_url = os.getenv("WEAVIATE_URL")
        weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
        openai_api_key = os.getenv("OPENAI_API_KEY")

        if not weaviate_url:
             print("Error: WEAVIATE_URL not found in .env")

        try:
            with WeaviateUtils(weaviate_url, weaviate_api_key, openai_api_key) as wu:
                limit = 10
                # Use raw keyword for semantic search
                _, response = wu.get_problems(keyword, limit)
                results = response.get('problems', [])

                lang = session.get('lang', 'lv')

                for res in results:
                    p_id = res.get('problemID', 'NA')

                    # Fallback to 'lv' if current lang text is missing, or just empty
                    p_text = res.get(f'problemText_{lang}', '')
                    if not p_text and lang != 'lv':
                         p_text = res.get('problemText_lv', '')

                    # Apply beautify
                    p_text = mathBeautify(p_text)
                    p_text = fix_image_links(p_text)

                    d = {'problemid': p_id, 'text': p_text, 'imagefile': ''}
                    problems.append(d)

        except Exception as e:
            print(f"Weaviate search failed: {e}")
            # We can choose to show an error or just return empty results

    else:
        offset = parse_offset(request.args.get('offset'))
        result = searchProblems(keyword, searchMode, searchTarget,
                                uiLang=session.get('lang', 'lv'), offset=offset)

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
        'lang': session.get('lang', 'lv'),
        'title': 'Sākumlapa',
        'clickcount': clickcount
    }
    return render_template('main_content.html', **template_context)
