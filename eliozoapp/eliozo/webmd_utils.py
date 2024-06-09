import re

def fix_image_links(arg):
    img_regex1 = r'<img\s+(alt="?[^"]*"?)\s+src="([^"/]*)" />\{ width=([^"]*) \}'
    img_replace1 = r'<img \1 style="width:\3" src="https://www.dudajevagatve.lv/static/eliozo/images/\2"/>'
    img_regex2 = r'<img\s+(alt="?[^"]*"?)\s+src="([^"/]*)"\s*/>'
    img_replace2 = r'<img \1 src="https://www.dudajevagatve.lv/static/eliozo/images/\2"/>'
    arg = re.sub(img_regex1, img_replace1, arg)
    arg = re.sub(img_regex2, img_replace2, arg)
    return arg
