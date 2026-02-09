
# import os
# import time

# def expand_markdown_includes(text, base_dir):
#     """
#     Replaces {!(.*)!} with the content of the file at base_dir/match
#     """
#     pattern = re.compile(r'\{!(.*?)!\}')
    
#     def repl(match):
#         rel_path = match.group(1).strip()
#         full_path = os.path.join(base_dir, rel_path)
#         try:
#             with open(full_path, 'r', encoding='utf-8') as f:
#                 return f.read()
#         except Exception as e:
#             return f"Error including {rel_path}: {str(e)}"

#     return pattern.sub(repl, text)

# def get_cached_book_content(subdir, problembase_root):
#     """
#     Checks cache or processes markdown.
#     """
#     if not problembase_root:
#         return "ERROR: PROBLEMBASE_ROOT environment variable not set."
    
#     source_dir = os.path.join(problembase_root, subdir)
#     source_file = os.path.join(source_dir, 'content_lv.md')
    
#     # Ensure static books dir exists
#     # We use current_app.root_path to find the static folder relative to the app
#     static_folder = current_app.static_folder
#     if not static_folder:
#          # Fallback if static_folder is not set
#          static_folder = os.path.join(current_app.root_path, 'static')

#     books_static_dir = os.path.join(static_folder, 'books')
#     os.makedirs(books_static_dir, exist_ok=True)
    
#     cache_file = os.path.join(books_static_dir, f'{subdir}.html')
    
#     needs_update = True
#     if os.path.exists(cache_file):
#         if os.path.exists(source_file):
#             src_mtime = os.path.getmtime(source_file)
#             cache_mtime = os.path.getmtime(cache_file)
#             if cache_mtime >= src_mtime:
#                 needs_update = False
    
#     if needs_update:
#         if not os.path.exists(source_file):
#              return f"ERROR: Content file not found at {source_file}"
        
#         try:
#             with open(source_file, 'r', encoding='utf-8') as f:
#                 text = f.read()
            
#             # 1. Expand includes
#             text = expand_markdown_includes(text, source_dir) 
            
#             # 2. Process markdown to HTML
#             html_content = proc_markdown(text)
            
#             # 3. Fix images and MathJax
#             html_content = fix_image_links(html_content)
#             html_content = mathBeautify(html_content)
            
#             with open(cache_file, 'w', encoding='utf-8') as f:
#                 f.write(html_content)
                
#         except Exception as e:
#             return f"ERROR processing book: {str(e)}"

#     # Read from cache
#     try:
#         with open(cache_file, 'r', encoding='utf-8') as f:
#             return f.read()
#     except Exception as e:
#         return f"ERROR reading cache: {str(e)}"
