import re
import markdown
from collections import defaultdict

import rdflib
from rdflib.namespace import RDF, FOAF, SKOS, XSD

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"
ELIOZO = rdflib.Namespace("http://www.dudajevagatve.lv/eliozo#")


# RDF methods

def add_new_problem(g, title):
    problem_node = rdflib.URIRef(eliozo_ns+title)
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((problem_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Problem")))
    return problem_node

# for example, key='country', value='LV'
def add_problem_literal_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    g.add((problem_node, problem_property, rdflib.term.Literal(value)))


def add_problem_literal_prop_lang(g, problem_node, key, value, lang):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    g.add((problem_node, problem_property, rdflib.term.Literal(value, lang=lang)))


# for example, key='grade', value=10
def add_problem_integer_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    g.add((problem_node, problem_property, rdflib.term.Literal(value, datatype=XSD.integer)))


def add_problem_topiclike_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    value_resource = rdflib.URIRef(eliozo_ns + value)
    g.add((problem_node, problem_property, value_resource))

def addSolutionToRdfProblem(g, title, i, solution_text, theLang):
    problem_node = rdflib.URIRef(eliozo_ns + title)  # subjekts
    solution_node = rdflib.URIRef(eliozo_ns + f"SOLN.{title}.SUB{i}")
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((solution_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Solution")))
    add_problem_literal_prop_lang(g, solution_node, 'solutionText', solution_text, theLang)
    add_problem_integer_prop(g, solution_node, 'solutionNum', i)
    add_problem_literal_prop_lang(g, solution_node, 'solutionTextHtml',
                                  markdown.markdown(solution_text, extensions=['tables']), theLang)
    problem_problemsolution_property = rdflib.URIRef(eliozo_ns + 'problemSolution')
    g.add((problem_node, problem_problemsolution_property, solution_node))


def addImageToRDFGraph(g, title, image_src, image_width):
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns + title) # subjekts
    image_node = rdflib.URIRef(eliozo_ns + "IMG." + image_src)
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((image_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Image")))
    add_problem_literal_prop(g, image_node, 'imageSrc', image_src)
    add_problem_literal_prop(g, image_node, 'imageWidth', image_width)
    problem_problemimage_property = rdflib.URIRef(eliozo_ns+'problemImage')
    g.add((problem_node, problem_problemimage_property, image_node))


def extract_problem(text):
    problem_text = []
    lines = text.split('\n')
    for line in lines:
        if line.startswith('# '):
            continue
        elif re.fullmatch(r'^\s*<small>\s*', line) or re.fullmatch(r'## .*', line):
            break
        else:
            problem_text.append(line)
    return '\n'.join(problem_text)



def extract_solutions(title, text):
    # Drop the starting portion
    f1 = text.find('</small>')
    f2 = text.find('<text num=')
    f3 = text.find('## Atrisin')
    if f1 >= 0:
        text = text[f1 + len('</small>'):]
    elif f2 >= 0:
        text = text[f2:]
    elif f3 >= 0:
        text = text[f3:]

    pattern1 = r'<text\s+num="[0-9]+"\s+lang="lv">'
    regex1 = re.compile(pattern1)
    match1 = regex1.search(text)

    if not match1:
        solutions = []
        current_solution = []
        lines = text.split('\n')
        for line in lines:
            if re.fullmatch(r'## Atrisin.*', line):
                # append the previous solution
                if current_solution != []:
                    solutions.append({'lv': '\n'.join(current_solution)})
                current_solution = [line]
            elif current_solution != []:
                # before seeing the first title, we do not append anything
                current_solution.append(line)
        # Append the last solution, when input ends
        if current_solution != []:
            solutions.append({'lv': '\n'.join(current_solution)})
        return solutions

    else:
        pattern = r'<text\s+num="([0-9]+)"\s+lang="([a-z]+)">\s*(.*?)\s*</text>'
        # Compile the regex pattern
        regex = re.compile(pattern, re.DOTALL)

        # Find all matching text blocks
        matches = regex.findall(text)

        # Initialize variables to store the results
        result = []
        current_num = None
        current_dict = defaultdict(str)

        # Process each match
        for match in matches:
            num, lang, content = match

            # Check if we've encountered a new "num" value
            if num != current_num:
                # If there is an existing dictionary, add it to the result list
                if current_dict:
                    result.append(dict(current_dict))

                # Start a new dictionary for the new "num" value
                current_dict = defaultdict(str)
                current_num = num

            # Add the content to the current dictionary
            current_dict[lang] = content.strip()

        # Don't forget to add the last dictionary to the result list
        if current_dict:
            result.append(dict(current_dict))

        return result


def extract_metadata(text):
    metadata = dict()
    lines = text.split('\n')
    meta_opened = False
    for line in lines:
        if re.fullmatch(r'\s*<small>\s*', line):
            meta_opened = True
        elif re.fullmatch(r'\s*</small>\s*', line):
            meta_opened = False
            break
        elif meta_opened:
            if line.startswith('* ['):
                continue
            key_val = line.split(":")
            if len(key_val) == 2:
                key = key_val[0]
                if key.startswith('* '):
                    key = key[2:]
                values = key_val[1].split(",")
                if key in metadata:
                    metadata[key].extend([i.strip() for i in values])
                else:
                    metadata[key] = [i.strip() for i in values]
    return metadata


def extract_images(text):
    images = []
    lines = text.split('\n')
    image_regex = re.compile(r"^!\[.*\]\((.*)\)(\{\s*width=(\S*)\s*\})?")  # LV.AO.2000.7.1
    for line in lines:
        line = line.strip()
        match_id = image_regex.match(line)
        if match_id:
            image_id = match_id.group(1)
            width = ''
            if match_id.group(3):
                width = match_id.group(3)
            images.append((image_id, width))
    return images


# Read problems one by one from Markdown file "filepath"
def extract_sections_from_md(filepath):
    section_titles = []
    current_section = None
    sections = []
    title = "NA"

    heading_re = re.compile(r'^#\s+<lo-sample/>\s+(.*)')

    with open(filepath, 'r') as file:
        for line in file:
            m = heading_re.match(line)
            if m:
                new_title = m.group(1)
                # append the previous (title, current_section)
                if current_section is not None:
                    sections.append((title, current_section))
                title = new_title
                current_section = line
            elif current_section is not None:
                # before seeing the first title, we do not append anything
                current_section += line
    # Append the last (title, current_section)
    if current_section:
        sections.append((title, current_section))
    return sections


def remove_translation_tags(text):
    lv_tag = '<text lang="lv">'
    if text.find(lv_tag) == -1:
        pattern = re.compile(r'<text lang=.*?>.*?</text>', re.DOTALL)
        return {'lv': re.sub(pattern, '', text)}
    else:
        result = {}
        pattern = r'<text lang="(?P<lang>\w+)">\s*(?P<content>.*?)\s*</text>'
        matches = re.finditer(pattern, text, re.DOTALL)
        for match in matches:
            lang = match.group('lang')
            content = match.group('content').strip()  # Strip any leading/trailing whitespace
            result[lang] = content
        return result


def get_suffix(arg):
    if not isinstance(arg, str):
        raise ValueError("Input should be a string")
    last_dot_index = arg.rfind('.')
    if last_dot_index == -1:
        return arg
    return arg[:last_dot_index]


# [('Contest','Konkurss'), ('Book','Grāmata'), ('RegionalOrOpen', 'Reģionu vai atklātā'),
# ('National', 'Nacionālā'), ('TeamSelection', 'Papildsacensības'), ('International', 'Starptautiska')] %}
# Return olympiadType - a single string value
def get_olympiad_type(title):
    result = 'Contest'
    title_list = title.split(".")
    prefix2 = ".".join(title_list[0:2])
    if prefix2 in ['EE.LVS', 'EE.LVT', 'EE.PK', 'EE.PKTEST', 'LT.RAJ', 'LT.VUMIF', 'LV.SOL', 'LV.NOL', 'LV.AMO']:
        result = 'RegionalOrOpen'
    elif prefix2 in ['EE.LO', 'LT.LMMO', 'LT.LKMMO', 'LV.VOL']:
        result = 'National'
    elif prefix2 in ['EE.TST', 'LT.TST', 'LV.TST']:
        result = 'TeamSelection'
    elif prefix2.startswith('IMO_SHL'):
        result = 'International'
    elif prefix2.startswith('BBK2012'):
        result = 'Book'
    return result

def get_suggested_grade(title):
    title_list = title.split(".")
    suffix2 = title_list[-2]
    if suffix2 in ['5', '6', '7', '8', '9', '10', '11', '12']:
        return [int(suffix2)]
    if title.startswith('BBK2012'):
        return [9,10,11,12]
    if title.startswith('IMO_SHL'):
        return [10,11,12]
    if title.startswith('EE.TST') or title.startswith('LT.TST') or title.startswith('LV.TST'):
        return [10,11,12]
    if title.startswith('LT.LKMMO'):
        return [9,10,11,12]
    if suffix2.find('_'):
        return [int(x) for x in suffix2.split('_')]
    else:
        print(f'UNDEFINED suggestedGrade for {title}')
        return []


def md_to_rdf(md_file_path, ttl_file_path):
    sections = extract_sections_from_md(md_file_path)

    g = rdflib.Graph()
    g.bind("foaf", FOAF)
    g.bind("skos", SKOS)
    g.bind("eliozo", ELIOZO)

    olympiad_problem_id = re.compile(r"(EE|LV|LT)\.(\w+)\.(\d{4}[A-Z]?)\.([0-9_]+)\.(\d+)") # LV.AO.2000.7.1
    book_problem_id = re.compile(r"([A-Z0-9]+)\.(.*)\.(\d+)")  # BBK2012.P1.1 or BBK2012.P1.E2.1 or similar
    inter_problem_id = re.compile(r"(\w+)\.(\d{4}[A-Z]?)\.([A-Z])?(\d+)")   # IMO_SHL.2022.A2

    for i, (title,section) in enumerate(sections):
        title = title.strip()
        suffix = get_suffix(title)
        suggestGrade = get_suggested_grade(title)
        olympiadType = get_olympiad_type(title)
        problem_node = add_new_problem(g, title)
        match_id = olympiad_problem_id.match(title)
        book_match_id = book_problem_id.match(title)
        inter_match_id = inter_problem_id.match(title)


        if match_id:
            country = match_id.group(1)
            olympiad = match_id.group(2)
            timeID = match_id.group(3)
            if len(timeID) > 4:
                year = int(timeID[0:4])
            else:
                year = int(timeID)
            rawGrade = match_id.group(4)
            grade_underscore = rawGrade.find("_")
            if grade_underscore == -1:
                grade = int(rawGrade)
            else:
                grade = int(rawGrade[0:grade_underscore])
            problem_number = match_id.group(5)
            add_problem_literal_prop(g, problem_node, 'country', country)
            add_problem_literal_prop(g, problem_node, 'olympiadCode', olympiad)
            add_problem_literal_prop(g, problem_node, 'olympiad', country + '.' + olympiad)
            add_problem_literal_prop(g, problem_node, 'suffix', suffix)
            add_problem_integer_prop(g, problem_node, 'problemYear', year)
            add_problem_literal_prop(g, problem_node, 'problemTimeID', timeID)
            add_problem_integer_prop(g, problem_node, 'problemGrade', grade)
            add_problem_integer_prop(g, problem_node, 'problem_number', problem_number)
            add_problem_literal_prop(g, problem_node, 'problemID', title)

        elif book_match_id:
            book_name = book_match_id.group(1)
            section_name = book_match_id.group(2)
            problem_number = book_match_id.group(3)
            add_problem_literal_prop(g, problem_node, 'problemBook', book_name)
            add_problem_literal_prop(g, problem_node, 'problemBookSection', section_name)
            add_problem_literal_prop(g, problem_node, 'suffix', suffix)
            add_problem_integer_prop(g, problem_node, 'problem_number', problem_number)
            add_problem_literal_prop(g, problem_node, 'problemID', title)

        elif inter_match_id:
            olympiad = inter_match_id.group(1)
            timeID = inter_match_id.group(2)
            if len(timeID) > 4:
                year = int(timeID[0:4])
            else:
                year = int(timeID)
            grade = 12
            problem_type = inter_match_id.group(3)
            problem_number = inter_match_id.group(4)
            if problem_type:
                suffix = suffix + "." + problem_type

            add_problem_literal_prop(g, problem_node, 'olympiad', olympiad)
            add_problem_literal_prop(g, problem_node, 'olympiadCode', olympiad)
            add_problem_literal_prop(g, problem_node, 'country', '')
            add_problem_integer_prop(g, problem_node, 'problemYear', year)
            add_problem_literal_prop(g, problem_node, 'problemTimeID', timeID)
            add_problem_literal_prop(g, problem_node, 'suffix', suffix)
            add_problem_integer_prop(g, problem_node, 'problem_number', problem_number)
            add_problem_integer_prop(g, problem_node, 'problemGrade', grade)
            add_problem_literal_prop(g, problem_node, 'problemID', title)

        else:
            print(f"***** WARNING: ***** Invalid problemID: {title}")

        # Get everything above <small>...</small> metadata block
        problem_text_md = extract_problem(section).strip()
        # return a dictionary of all problem translations
        # (Latvian text can be without <text lang="lv">)
        problem_text_dict = remove_translation_tags(problem_text_md)

        # img_list = extract_images(problem_text_md)
        # for (img_src, img_width) in img_list:
        #     addImageToRDFGraph(g, title, img_src, img_width)

        for theLang, problem_text_md in problem_text_dict.items():
            problem_text_html = markdown.markdown(problem_text_md, extensions=['tables']).strip()

            add_problem_literal_prop_lang(g, problem_node, 'problemText', problem_text_md, theLang)
            add_problem_literal_prop_lang(g, problem_node, 'problemTextHtml', problem_text_html, theLang)

        add_problem_literal_prop(g, problem_node, 'olympiadType', olympiadType)
        for sug_grade in suggestGrade:
            add_problem_integer_prop(g, problem_node, 'suggestedGrade', sug_grade)

        meta_dict = extract_metadata(section)
        for k, vvv in meta_dict.items():
            for vv in vvv:
                if k == 'topic':
                    add_problem_topiclike_prop(g, problem_node, 'topic', vv)
                elif k == 'concepts':
                    add_problem_topiclike_prop(g, problem_node, 'concepts', "TRM-"+vv)
                else:
                    add_problem_literal_prop(g, problem_node, k, vv)

        solutions = extract_solutions(title,section)
        for i, soln_text_dict in enumerate(solutions):
            for theLang, soln_text in soln_text_dict.items():
                soln_text = soln_text.strip()
                addSolutionToRdfProblem(g, title, i, soln_text, theLang)
                img_list = extract_images(soln_text)
                for (img_src, img_width) in img_list:
                    addImageToRDFGraph(g, title, img_src, img_width)
    g.serialize(destination=ttl_file_path)


if __name__ == '__main__':
    md_to_rdf('resources/LV-AMO-lv-amo-2023.md', 'resources/temp.ttl')

