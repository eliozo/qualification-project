import re
import markdown
import os
import time

from flask import current_app, url_for

# def fix_image_links(arg):
#     img_regex1 = r'<img\s+(alt="?[^"]*"?)\s+src="([^"/]*)" />\{ width=([^"]*) \}'
#     img_replace1 = r'<img \1 style="width:\3" src="https://www.dudajevagatve.lv/static/eliozo/images/\2"/>'
#     img_regex2 = r'<img\s+(alt="?[^"]*"?)\s+src="([^"/]*)"\s*/>'
#     img_replace2 = r'<img \1 src="https://www.dudajevagatve.lv/static/eliozo/images/\2"/>'
#     arg = re.sub(img_regex1, img_replace1, arg)
#     arg = re.sub(img_regex2, img_replace2, arg)
#     return arg

def fix_image_links(arg):
    USE_REMOTE_STATIC = current_app.config.get('USE_REMOTE_STATIC', False)
    STATIC_PREFIX = ('/static/eliozo/images/' 
                     if USE_REMOTE_STATIC 
                     else url_for('static', filename='eliozo/images/'))

    def repl_width(match):
        alt, fname, width = match.groups()
        return f'<img {alt} style="width:{width}" src="{STATIC_PREFIX}{fname}"/>'

    def repl_simple(match):
        alt, fname = match.groups()
        return f'<img {alt} src="{STATIC_PREFIX}{fname}"/>'

    import re
    pattern1 = re.compile(r'<img\s+(alt="?[^"]*"?)\s+src="([^"/]*)" />\{ width=([^"]*) \}')
    pattern2 = re.compile(r'<img\s+(alt="?[^"]*"?)\s+src="([^"/]*)"\s*/>')

    arg = pattern1.sub(repl_width, arg)
    arg = pattern2.sub(repl_simple, arg)
    return arg


def mathBeautify(a): # Izskaistina formulas ar MathJax Javascript bibliotēku
    b0 = re.sub(r"\$\$([^\$]+)\$\$", r"<p><span class='math display'>\[\1\]</span></p>", a) # Aizstāj vairākrindu formulas $$..$$
    b = re.sub(r"\$([^\$]+)\$", r"<span class='math inline'>\(\1\)</span>", b0) # Aizstāj inline formulas $...$ (Svarīga secība, kā aizstāj)
    return b

def extract_latex(text):
    # Find all the LaTeX patterns and replace them with placeholders
    inline_latex = re.findall(r'\$[^\$]+\$', text)
    display_latex = re.findall(r'\$\$[^\$]+\$\$', text)

    placeholders = {}
    idx = 0
    for latex in inline_latex + display_latex:
        placeholder = f"LaTeXPlaceholder({idx})"
        placeholders[placeholder] = latex
        text = text.replace(latex, placeholder, 1)
        idx += 1

    return text, placeholders

def replace_placeholders(text, placeholders):
    # Replace the placeholders with the original LaTeX content
    for placeholder, latex in placeholders.items():
        text = text.replace(placeholder, latex)
    return text

def proc_markdown(text):
    text_with_placeholders, latex_placeholders = extract_latex(text)
    problemTextHtml = markdown.markdown(text_with_placeholders, extensions=['tables']).strip()
    problemTextHtml = replace_placeholders(problemTextHtml, latex_placeholders)
    return problemTextHtml


def expand_markdown_includes(text, base_dir):
    """
    Replaces {!(.*)!} with the content of the file at base_dir/match
    """
    pattern = re.compile(r'\{!(.*?)!\}')
    
    def repl(match):
        rel_path = match.group(1).strip()
        full_path = os.path.join(base_dir, rel_path)
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            return f"Error including {rel_path}: {str(e)}"

    return pattern.sub(repl, text)

def get_cached_book_content(subdir, problembase_root):
    """
    Checks cache or processes markdown.
    """
    if not problembase_root:
        return "ERROR: PROBLEMBASE_ROOT environment variable not set."
    
    source_dir = os.path.join(problembase_root, subdir)
    source_file = os.path.join(source_dir, 'content_lv.md')
    
    # Ensure static books dir exists
    # We use current_app.root_path to find the static folder relative to the app
    static_folder = current_app.static_folder
    if not static_folder:
         # Fallback if static_folder is not set
         static_folder = os.path.join(current_app.root_path, 'static')
    
    # Ensure we look in 'eliozo/static' structure if that is how it is organized
    # Based on app structure: eliozoapp/eliozo/static/eliozo/images
    # The user suggested: "eliozoapp/eliozo/static/books"
    
    # If static_folder points to eliozoapp/eliozo/static
    books_static_dir = os.path.join(static_folder, 'books')
    
    if not os.path.exists(books_static_dir):
        try:
            os.makedirs(books_static_dir, exist_ok=True)
        except OSError:
            # Fallback for permission errors or path issues?
            pass
    
    cache_file = os.path.join(books_static_dir, f'{subdir}.html')
    
    needs_update = True
    if os.path.exists(cache_file):
        if os.path.exists(source_file):
            src_mtime = os.path.getmtime(source_file)
            cache_mtime = os.path.getmtime(cache_file)
            if cache_mtime >= src_mtime:
                needs_update = False
    
    if needs_update:
        if not os.path.exists(source_file):
             return f"ERROR: Content file not found at {source_file}"
        
        try:
            with open(source_file, 'r', encoding='utf-8') as f:
                text = f.read()
            
            # 1. Expand includes
            text = expand_markdown_includes(text, source_dir) 
            
            # 2. Process markdown to HTML
            html_content = proc_markdown(text)
            
            # 3. Fix images and MathJax
            html_content = fix_image_links(html_content)
            html_content = mathBeautify(html_content)
            
            with open(cache_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
                return html_content # Return directly to avoid re-reading
                
        except Exception as e:
            return f"ERROR processing book: {str(e)}"

    # Read from cache
    try:
        with open(cache_file, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"ERROR reading cache: {str(e)}"

