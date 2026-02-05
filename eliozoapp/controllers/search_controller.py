import sys
import os
from dotenv import load_dotenv
from flask import render_template, request, session, json

# Add path to weaviate_utils
# Using the path provided by the user
# sys.path.append("/Users/kapsitis/workspace-public/worksheet-generation-with-llms/scripts")
from controllers.weaviate_utils import WeaviateUtils

from eliozo.webmd_utils import fix_image_links, mathBeautify
from eliozo.search_helpers import (
    replace_non_ascii_with_unicode_escape, 
    getProblemsByKeywordSPARQL, 
    getProblemsByRegexSPARQL
)

def search_problems():
    keyword = request.args.get('keyword')
    if 'clickcount' in session: 
        clickcount = session['clickcount']
    else:
        clickcount = 0
    print(f"clickcount = {clickcount}")
    
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
        
        # Note: WeaviateUtils expects "WEAVIATE_URL", but .env usually has it. 
        # Check what the .env usage expects. The user just said "The .env file... is located under..."
        # WeaviateUtils constructor takes (weaviate_url, weaviate_api_key, openai_api_key).
        # We assume the keys in .env are WEAVIATE_URL, WEAVIATE_API_KEY, OPENAI_API_KEY or similar.
        # Let's try to fetch them. If different names, we might fail. 
        # But typically they are standard. 
        
        weaviate_url = os.getenv("WEAVIATE_URL")
        weaviate_api_key = os.getenv("WEAVIATE_API_KEY")
        openai_api_key = os.getenv("OPENAI_API_KEY")

        if not weaviate_url:
             print("Error: WEAVIATE_URL not found in .env")
        
        try:
            # WeaviateUtils uses 'Problem' collection by default in get_problems?
            # get_problems calls near_search("Problem", ...)
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
