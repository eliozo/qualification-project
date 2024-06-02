import re
import markdown

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


def add_problem_literal_lv_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    g.add((problem_node, problem_property, rdflib.term.Literal(value, lang=u'lv')))


# for example, key='grade', value=10
def add_problem_integer_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    g.add((problem_node, problem_property, rdflib.term.Literal(value, datatype=XSD.integer)))


def add_problem_topiclike_prop(g, problem_node, key, value):
    problem_property = rdflib.URIRef(eliozo_ns + key)
    value_resource = rdflib.URIRef(eliozo_ns + value)
    g.add((problem_node, problem_property, value_resource))

def addSolutionToRdfProblem(g, title, i, solution_text):
    problem_node = rdflib.URIRef(eliozo_ns + title)  # subjekts
    solution_node = rdflib.URIRef(eliozo_ns + "SOLN." + title)
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((solution_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Solution")))
    add_problem_literal_lv_prop(g, solution_node, 'solutionText', solution_text)
    add_problem_integer_prop(g, solution_node, 'solutionNum', i)
    add_problem_literal_lv_prop(g, solution_node, 'solutionTextHtml', markdown.markdown(solution_text, extensions=['tables']))
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



def extract_solutions(text):
    solutions = []
    current_solution = []
    lines = text.split('\n')
    for line in lines:
        if re.fullmatch(r'## Atrisin.*', line):
            # append the previous solution
            if current_solution != []:
                solutions.append('\n'.join(current_solution))
            current_solution = [line]
        elif current_solution != []:
            # before seeing the first title, we do not append anything
            current_solution.append(line)
    # Append the last solution, when input ends
    if current_solution != []:
        solutions.append('\n'.join(current_solution))
    return solutions


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
    pattern = re.compile(r'<text lang=.*?>.*?</text>', re.DOTALL)
    return re.sub(pattern, '', text)

def md_to_rdf(md_file_path, ttl_file_path):
    sections = extract_sections_from_md(md_file_path)

    g = rdflib.Graph()
    g.bind("foaf", FOAF)
    g.bind("skos", SKOS)
    g.bind("eliozo", ELIOZO)

    olympiad_problem_id = re.compile(r"([A-Z]{2})\.(\w+)\.(\d+[A-Z]?)\.([0-9_]+)\.(\d+)") # LV.AO.2000.7.1
    book_problem_id = re.compile(r"([A-Z0-9]*)\.(.*)\.(\d+)")  # BBK2012.P1.1 or BBK2012.P1.E2.1 or similar

    for i, (title,section) in enumerate(sections):
        title = title.strip()
        problem_node = add_new_problem(g, title)
        match_id = olympiad_problem_id.match(title)
        if match_id:
            country = match_id.group(1)
            olympiad = match_id.group(2)
            year = match_id.group(3)
            if len(year) > 4:
                year = int(year[0:4])
            else:
                year = int(year)
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
            add_problem_integer_prop(g, problem_node, 'problemYear', year)
            add_problem_integer_prop(g, problem_node, 'problemGrade', grade)
            add_problem_integer_prop(g, problem_node, 'problem_number', problem_number)
            add_problem_literal_prop(g, problem_node, 'problemID', title)
        match_id = book_problem_id.match(title)
        if match_id:
            book_name = match_id.group(1)
            section_name = match_id.group(2)
            problem_number = match_id.group(3)
            add_problem_literal_prop(g, problem_node, 'problemBook', book_name)
            add_problem_literal_prop(g, problem_node, 'problemBookSection', section_name)
            add_problem_integer_prop(g, problem_node, 'problem_number', problem_number)
            add_problem_literal_prop(g, problem_node, 'problemID', title)

        problem_text_md = extract_problem(section).strip()
        # clean away the translations
        problem_text_md = remove_translation_tags(problem_text_md)

        img_list = extract_images(problem_text_md)
        for (img_src, img_width) in img_list:
            addImageToRDFGraph(g, title, img_src, img_width)


        problem_text_html = markdown.markdown(problem_text_md, extensions=['tables']).strip()
        add_problem_literal_lv_prop(g, problem_node, 'problemText', problem_text_md)
        add_problem_literal_lv_prop(g, problem_node, 'problemTextHtml', problem_text_html)

        meta_dict = extract_metadata(section)
        for k, vvv in meta_dict.items():
            for vv in vvv:
                if k == 'topic':
                    add_problem_topiclike_prop(g, problem_node, 'topic', vv)
                else:
                    add_problem_literal_prop(g, problem_node, k, vv)

        solutions = extract_solutions(section)
        for i, soln in enumerate(solutions):
            soln_text = soln.strip()
            addSolutionToRdfProblem(g, title, i, soln_text)
            img_list = extract_images(soln_text)
            for (img_src, img_width) in img_list:
                addImageToRDFGraph(g, title, img_src, img_width)
    g.serialize(destination=ttl_file_path)


if __name__ == '__main__':
    md_to_rdf('resources/LV-AMO-lv-amo-2023.md', 'resources/temp.ttl')

