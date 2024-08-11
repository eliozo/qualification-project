import re
import markdown

def fix_image_links(arg):
    img_regex1 = r'<img\s+(alt="?[^"]*"?)\s+src="([^"/]*)" />\{ width=([^"]*) \}'
    img_replace1 = r'<img \1 style="width:\3" src="https://www.dudajevagatve.lv/static/eliozo/images/\2"/>'
    img_regex2 = r'<img\s+(alt="?[^"]*"?)\s+src="([^"/]*)"\s*/>'
    img_replace2 = r'<img \1 src="https://www.dudajevagatve.lv/static/eliozo/images/\2"/>'
    arg = re.sub(img_regex1, img_replace1, arg)
    arg = re.sub(img_regex2, img_replace2, arg)
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

