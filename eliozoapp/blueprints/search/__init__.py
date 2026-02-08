from flask import Blueprint, render_template, request, session, json
import os
from dotenv import load_dotenv

# Add path to weaviate_utils if needed, or assume it's in python path
# based on imports in other files, controllers seems to be a package
from controllers.weaviate_utils import WeaviateUtils

from eliozo.webmd_utils import fix_image_links, mathBeautify
from eliozo_dao.search_repository import (
    replace_non_ascii_with_unicode_escape, 
    getProblemsByKeywordSPARQL, 
    getProblemsByRegexSPARQL
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
    
    if keyword is None or keyword == "":
        template_context = {
            'active': 'main',
            'searchMode': 'exact'
        }
        return render_template('main_content.html',  **template_context)
    
    new_keyword = replace_non_ascii_with_unicode_escape(keyword)
    searchMode = request.args.get('searchMode')
    
    problems = []

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
        isRegex = (searchMode == 'regex')

        if not isRegex:
            link = json.loads(getProblemsByKeywordSPARQL(new_keyword, False))
        else:
            link = json.loads(getProblemsByRegexSPARQL(new_keyword, False))
        
        if 'results' in link and 'bindings' in link['results']:
            for item in link['results']['bindings']:
                problem_id_value = item['problemid']['value']
                problem_imagefile = ''
                problem_text_value = mathBeautify(item['textHtml']['value'])
                problem_text_value = fix_image_links(problem_text_value)
                d = {'problemid': problem_id_value, 'text': problem_text_value, 'imagefile': problem_imagefile}
                problems.append(d)

    template_context = {
        'problems': problems,
        'keyword' : keyword,
        'active': 'main',
        'searchMode': searchMode,
        'lang': session.get('lang', 'lv'),
        'title': 'Sākumlapa', 
        'clickcount': clickcount
    }
    return render_template('main_content.html', **template_context)
