import json
import re
# from rdflib import Graph, URIRef, Literal, Namespace, BNode
import rdflib
from rdflib.namespace import RDF, FOAF, SKOS, XSD

RDF_NS = "http://www.w3.org/1999/02/22-rdf-syntax-ns#"
eliozo_ns = "http://www.dudajevagatve.lv/eliozo#"

def addToRdfGraph(g, title, text, country, olympiad, year, grade, problem_number): # Funkcija, kas pievieno RDF datus grafam
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns+title)
    problem_country_property = rdflib.URIRef(eliozo_ns+'country')
    problem_olympiadcode_property = rdflib.URIRef(eliozo_ns + 'olympiadCode')
    problem_olympiad_property = rdflib.URIRef(eliozo_ns + 'olympiad')
    problem_year_property = rdflib.URIRef(eliozo_ns+'problemYear')
    problem_grade_property = rdflib.URIRef(eliozo_ns+'problemGrade')
    problem_number_property = rdflib.URIRef(eliozo_ns+'problem_number')
    problem_rdf_property = rdflib.URIRef(RDF_NS+'type')
    problem_id = rdflib.URIRef(eliozo_ns+'problemID')
    g.add((problem_node, problem_country_property, rdflib.term.Literal(country)))
    g.add((problem_node, problem_olympiadcode_property, rdflib.term.Literal(olympiad)))
    g.add((problem_node, problem_olympiad_property, rdflib.URIRef(eliozo_ns + country + '.' + olympiad)))
    g.add((problem_node, problem_year_property, rdflib.term.Literal(year)))
    g.add((problem_node, problem_grade_property, rdflib.term.Literal(grade, datatype=XSD.integer)))
    g.add((problem_node, problem_number_property, rdflib.term.Literal(problem_number)))
    g.add((problem_node, problem_id, rdflib.term.Literal(title)))
    g.add((problem_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Problem")))

# current_problem_id = "NA"

def addTextToRdfProblem(g, title, text):
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns + title)
    problem_text_property = rdflib.URIRef(eliozo_ns + 'problemText')
    problem_text = rdflib.term.Literal(text, lang=u'lv')
    g.add((problem_node, problem_text_property, problem_text))

def addNoteToRdfProblem(g, title, note_text):
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns + title)
    problem_note_property = rdflib.URIRef(eliozo_ns + 'problemNote')
    problem_note = rdflib.term.Literal(note_text, lang=u'lv')
    g.add((problem_node, problem_note_property, problem_note))


def addSkillToRdfGraph(g, title, skill): # Funkcija, kas pievieno RDF prasmes datus grafam 
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns+title) # subjekts
    problem_skill_property = rdflib.URIRef(eliozo_ns+'hasSkill') # property vienmēr eliozo:hasSkill, predikāts
    problem_skill_object = rdflib.URIRef(eliozo_ns+skill) # konkrētā prasme, īpašība var atkāroties, objekts
    g.add((problem_node, problem_skill_property, problem_skill_object))

def addTopicToRdfGraph(g, title, topic): # Funkcija, kas pievieno RDF tēmu uzdevumam 
    global eliozo_ns
    # print(f'Adding topic {topic}')
    problem_node = rdflib.URIRef(eliozo_ns+title) # subjekts
    problem_topic_property = rdflib.URIRef(eliozo_ns+'hasTopic') # property vienmēr eliozo:hasTopic, predikāts
    problem_topic_object = rdflib.URIRef(eliozo_ns+topic) # konkrētā tēma, objekts
    g.add((problem_node, problem_topic_property, problem_topic_object))

def addAnswerToRdfGraph(g, title, answer): # Funkcija, kas pievieno RDF tēmu uzdevumam
    global eliozo_ns
    # print(f'Adding answer {answer}')
    problem_node = rdflib.URIRef(eliozo_ns+title) # subjekts
    problem_answer_property = rdflib.URIRef(eliozo_ns+'problemHasAnswer')
    problem_answer_object = rdflib.term.Literal(answer)
    g.add((problem_node, problem_answer_property, problem_answer_object))

def addSuggestedGradeToRdfGraph(g, title, grade):
    global eliozo_ns
    # print(f'Adding grade {grade}')
    problem_node = rdflib.URIRef(eliozo_ns+title) # subjekts
    problem_suggestedgrade_property = rdflib.URIRef(eliozo_ns+'problemSuggestedGrade')
    problem_suggestedgrade_object = rdflib.term.Literal(grade, datatype=XSD.integer)
    g.add((problem_node, problem_suggestedgrade_property, problem_suggestedgrade_object))


def addImageToRDFGraph(g, title, image_src, image_width):
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns + title) # subjekts
    image_node = rdflib.URIRef(eliozo_ns + "IMG." + title)
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((image_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Image")))
    problem_imagesrc_property = rdflib.URIRef(eliozo_ns+'imageSrc')
    problem_imagewidth_property = rdflib.URIRef(eliozo_ns+'imageWidth')
    problem_imagesrc_object = rdflib.term.Literal(image_src)
    g.add((image_node, problem_imagesrc_property, problem_imagesrc_object))
    problem_imagewidth_object = rdflib.term.Literal(image_width, datatype=XSD.integer)
    g.add((image_node, problem_imagewidth_property, problem_imagewidth_object))
    problem_problemimage_property = rdflib.URIRef(eliozo_ns+'problemImage')
    g.add((problem_node, problem_problemimage_property, image_node))

def addImageToRDFSolution(g, current_problem_id, image_src, image_width):
    print(f"Solution image: {image_src}, width={image_width}")

def addSolutionToRdfProblem(g, title, solution_text):
    global eliozo_ns
    problem_node = rdflib.URIRef(eliozo_ns + title)  # subjekts
    solution_node = rdflib.URIRef(eliozo_ns + "SOLN." + title)
    problem_rdf_property = rdflib.URIRef(RDF_NS + 'type')
    g.add((solution_node, problem_rdf_property, rdflib.URIRef(eliozo_ns + "Solution")))
    problem_solutiontext_property = rdflib.URIRef(eliozo_ns + 'solutionText')
    problem_solutiontext_object = rdflib.term.Literal(solution_text)
    g.add((solution_node, problem_solutiontext_property, problem_solutiontext_object))
    problem_problemsolution_property = rdflib.URIRef(eliozo_ns + 'problemSolution')
    g.add((problem_node, problem_problemsolution_property, solution_node))



def JsonToGraph(data):
    ELIOZO = rdflib.Namespace("http://www.dudajevagatve.lv/eliozo#")

    g = rdflib.Graph()

    g.bind("foaf", FOAF)
    g.bind("skos", SKOS)
    g.bind("eliozo", ELIOZO)

    items = data['children']

    state = 0

    problem_title = 'undefined'
    image_width_pattern = re.compile(r'\{\s+width\s*=\s*(\d+)px\s+\}')

    current_problem_id = "NA"
    problem_text = ""
    solution_text = ""

    for item in items:
        if item['type'] == 'Heading':
            if solution_text != "":
                addSolutionToRdfProblem(g, current_problem_id, solution_text)
            problem_title = item['children'][0]['content']
            print(f'problem_title = {problem_title}')
            if problem_title.startswith('<lo-sample/>'):
                # Read the first paragraph of a problem
                state = 1
                problem_title = problem_title[13:]
                current_problem_id = problem_title
                problem_text = ""
                solution_text = ""
            elif problem_title.startswith('Atrisinājums'):
                state = 4
            # print('State 0-to-1')
        elif state == 1 and item['type'] == 'Paragraph':
            country = "NA"
            olympiad = "NA"
            year = "NA"
            grade = "NA"
            problem_number = "NA"
            problem_id = re.compile(r"([A-Z]{2})\.(\w+)\.(\d+)\.(\d+)([A-Za-z_]+\w*)?\.(\d+)") # LV.AO.2000.7.1
            match_id = problem_id.match(problem_title)
            if (match_id):
                country = match_id.group(1)
                olympiad = match_id.group(2)
                year = match_id.group(3)
                grade = match_id.group(4)
                problem_number = match_id.group(6)
            if grade == "NA":
                grade = 0
            problem_text = ""
            for line in item['children']:
                if line['type'] == 'RawText':
                    problem_text = problem_text+line['content']
                elif line['type'] == 'LineBreak':
                    problem_text = problem_text+'\n'
            addToRdfGraph(g, problem_title, problem_text, country, olympiad, year, grade, problem_number)
            # print('State 1-to-2')
            state = 2  # continue reading problem


        elif state == 2 and item['type'] == 'Paragraph' and ('content' in item['children'][0].keys()) and item['children'][0]['content'] == '<small>':
            addTextToRdfProblem(g, current_problem_id, problem_text)
            # print("State 2-to-3 (read <small>")
            state = 3

        elif state == 2 and item['type'] == 'Paragraph' and item['children'][0]['type'] == 'Image':
            #print("Problem Image ----")
            image_src = item['children'][0]['src']
            image_width = 0
            if len(item['children']) > 1:
                match = image_width_pattern.search(item['children'][1]['content'])
                if match:
                    image_width = match.group(1)
            addImageToRDFGraph(g, current_problem_id, image_src, image_width)
            # print('State 2-to-2 (read img)')
            state = 2

        elif state == 2 and item['type'] == 'Paragraph' and item['children'][0]['type'] == 'Emphasis':
            note_text = item['children'][0]['children'][0]['content']
            # print('State 2-to-2 (read note)')
            # print(f'Problem text = {problem_text}')
            addNoteToRdfProblem(g, current_problem_id, note_text)
            state = 2


        elif state == 2 and item['type'] == 'Paragraph':
            #print("Problem Continues... ----")
            #print(f'Problem text = {problem_text}')
            problem_text = problem_text + '\n\n'
            for line in item['children']:
                if line['type'] == 'RawText':
                    problem_text = problem_text+line['content']
                elif line['type'] == 'LineBreak':
                    problem_text = problem_text+'\n'
            print('State 2-to-2 (read more)')
            state = 2


        elif state == 3 and item['type'] == 'Paragraph' and ('content' in item['children'][0].keys()) and item['children'][0]['content'] == '</small>':
            # Wait for solution or for another problem; ignore everything.
            # print("State 3-to-0 (read </small>)")
            state = 0

        elif state == 3 and item['type'] == 'List':
            skill_items = item['children']
            for skill_item in skill_items:
                if skill_item['type'] == 'ListItem':
                    skill_item_sub = skill_item['children'][0]['children'][0]
                    if skill_item_sub['type'] == 'Link':
                        skill = skill_item_sub['children'][0]['content']
                        print(f'skill = {skill}')
                        addSkillToRdfGraph(g, current_problem_id, skill)

                    elif skill_item_sub['type'] == 'RawText':
                        topicStr = skill_item_sub['content']
                        if topicStr.startswith('Topic:'):
                            topic = topicStr[6:]
                            addTopicToRdfGraph(g, current_problem_id, topic)
                        elif topicStr.startswith('Answer:'):
                            answer = topicStr[7:]
                            addAnswerToRdfGraph(g, current_problem_id, answer)
                        elif topicStr.startswith('Grade:'):
                            grades = topicStr[6:]
                            gradesList = grades.split(",")
                            for grade in gradesList:
                                addSuggestedGradeToRdfGraph(g, current_problem_id, grade)
            # print("State 3-to-3 (process small-list)")
            state = 3

        elif state == 4 and item['type'] == 'Paragraph' and item['children'][0]['type'] == 'Image':
            image_src = item['children'][0]['src']
            image_width = 0
            if len(item['children']) > 1:
                match = image_width_pattern.search(item['children'][1]['content'])
                if match:
                    image_width = match.group(1)
            solution_text = solution_text + "\n\n"
            solution_text = solution_text + f'<img src="http://www.dudajevagatve.lv/static/eliozo/images/{image_src}" width="{image_width}px"/>'
            addImageToRDFSolution(g, current_problem_id, image_src, image_width)
            state = 4

        elif state == 4 and item['type'] == 'Paragraph':
            if solution_text != "":
                solution_text = solution_text + "\n\n"
            solution_text = solution_text + "<p>"
            for line in item['children']:
                if line['type'] == 'RawText':
                    solution_text = solution_text+line['content']
                elif line['type'] == 'LineBreak':
                    solution_text = solution_text+'\n'
            solution_text = solution_text + "</p>"
            state = 4

        elif state == 4:
            # ignore trailing garbage after the solution (wait for another heading)
            addSolutionToRdfProblem(g, current_problem_id, solution_text)
            state = 0

        else:
            # continue ignoring the input, if something is not recognized
            state = 0
    return g


def produceRDF(in_file, out_file): # Funkcija, kas pārveido JSON failu par RDF
    ELIOZO = rdflib.Namespace("http://www.dudajevagatve.lv/eliozo#")

    g = rdflib.Graph()

    g.bind("foaf", FOAF)
    g.bind("skos", SKOS)
    g.bind("eliozo", ELIOZO)

    f = open(in_file) # Atver JSON failu
    
    data = json.load(f) # Atgriež JSON objektu kā vārdnīcu

    items = data['children']

    state = 0

    problem_title = 'undefined'
    image_width_pattern = re.compile(r'\{\s+width\s*=\s*(\d+)px\s+\}')

    current_problem_id = "NA"
    problem_text = ""
    solution_text = ""

    for item in items:
        if item['type'] == 'Heading':
            if solution_text != "":
                addSolutionToRdfProblem(g, current_problem_id, solution_text)
            problem_title = item['children'][0]['content']
            print(f'problem_title = {problem_title}')
            if problem_title.startswith('<lo-sample/>'):
                # Read the first paragraph of a problem
                state = 1
                problem_title = problem_title[13:]
                current_problem_id = problem_title
                problem_text = ""
                solution_text = ""
            elif problem_title.startswith('Atrisinājums'):
                state = 4
            # print('State 0-to-1')
        elif state == 1 and item['type'] == 'Paragraph':
            country = "NA"
            olympiad = "NA"
            year = "NA"
            grade = "NA"
            problem_number = "NA"
            problem_id = re.compile(r"([A-Z]{2})\.(\w+)\.(\d+)\.(\d+)([A-Za-z_]+\w*)?\.(\d+)") # LV.AO.2000.7.1
            match_id = problem_id.match(problem_title)
            if (match_id):
                country = match_id.group(1)
                olympiad = match_id.group(2)
                year = match_id.group(3)
                grade = match_id.group(4)
                problem_number = match_id.group(6)
            if grade == "NA":
                grade = 0
            problem_text = ""
            for line in item['children']:
                if line['type'] == 'RawText':
                    problem_text = problem_text+line['content']
                elif line['type'] == 'LineBreak':
                    problem_text = problem_text+'\n'
            addToRdfGraph(g, problem_title, problem_text, country, olympiad, year, grade, problem_number)
            # print('State 1-to-2')
            state = 2  # continue reading problem


        elif state == 2 and item['type'] == 'Paragraph' and ('content' in item['children'][0].keys()) and item['children'][0]['content'] == '<small>':
            addTextToRdfProblem(g, current_problem_id, problem_text)
            # print("State 2-to-3 (read <small>")
            state = 3

        elif state == 2 and item['type'] == 'Paragraph' and item['children'][0]['type'] == 'Image':
            #print("Problem Image ----")
            image_src = item['children'][0]['src']
            image_width = 0
            if len(item['children']) > 1:
                match = image_width_pattern.search(item['children'][1]['content'])
                if match:
                    image_width = match.group(1)
            addImageToRDFGraph(g, current_problem_id, image_src, image_width)
            # print('State 2-to-2 (read img)')
            state = 2

        elif state == 2 and item['type'] == 'Paragraph' and item['children'][0]['type'] == 'Emphasis':
            note_text = item['children'][0]['children'][0]['content']
            # print('State 2-to-2 (read note)')
            # print(f'Problem text = {problem_text}')
            addNoteToRdfProblem(g, current_problem_id, note_text)
            state = 2


        elif state == 2 and item['type'] == 'Paragraph':
            #print("Problem Continues... ----")
            #print(f'Problem text = {problem_text}')
            problem_text = problem_text + '\n\n'
            for line in item['children']:
                if line['type'] == 'RawText':
                    problem_text = problem_text+line['content']
                elif line['type'] == 'LineBreak':
                    problem_text = problem_text+'\n'
            print('State 2-to-2 (read more)')
            state = 2


        elif state == 3 and item['type'] == 'Paragraph' and ('content' in item['children'][0].keys()) and item['children'][0]['content'] == '</small>':
            # Wait for solution or for another problem; ignore everything.
            # print("State 3-to-0 (read </small>)")
            state = 0

        elif state == 3 and item['type'] == 'List':
            skill_items = item['children']
            for skill_item in skill_items:
                if skill_item['type'] == 'ListItem':
                    skill_item_sub = skill_item['children'][0]['children'][0]
                    if skill_item_sub['type'] == 'Link':
                        skill = skill_item_sub['children'][0]['content']
                        print(f'skill = {skill}')
                        addSkillToRdfGraph(g, current_problem_id, skill)

                    elif skill_item_sub['type'] == 'RawText':
                        topicStr = skill_item_sub['content']
                        if topicStr.startswith('Topic:'):
                            topic = topicStr[6:]
                            addTopicToRdfGraph(g, current_problem_id, topic)
                        elif topicStr.startswith('Answer:'):
                            answer = topicStr[7:]
                            addAnswerToRdfGraph(g, current_problem_id, answer)
                        elif topicStr.startswith('Grade:'):
                            grades = topicStr[6:]
                            gradesList = grades.split(",")
                            for grade in gradesList:
                                addSuggestedGradeToRdfGraph(g, current_problem_id, grade)
            # print("State 3-to-3 (process small-list)")
            state = 3

        elif state == 4 and item['type'] == 'Paragraph' and item['children'][0]['type'] == 'Image':
            image_src = item['children'][0]['src']
            image_width = 0
            if len(item['children']) > 1:
                match = image_width_pattern.search(item['children'][1]['content'])
                if match:
                    image_width = match.group(1)
            solution_text = solution_text + "\n\n"
            solution_text = solution_text + f'<img src="http://www.dudajevagatve.lv/static/eliozo/images/{image_src}" width="{image_width}px"/>'
            addImageToRDFSolution(g, current_problem_id, image_src, image_width)
            state = 4

        elif state == 4 and item['type'] == 'Paragraph':
            if solution_text != "":
                solution_text = solution_text + "\n\n"
            solution_text = solution_text + "<p>"
            for line in item['children']:
                if line['type'] == 'RawText':
                    solution_text = solution_text+line['content']
                elif line['type'] == 'LineBreak':
                    solution_text = solution_text+'\n'
            solution_text = solution_text + "</p>"
            state = 4

        elif state == 4:
            # ignore trailing garbage after the solution (wait for another heading)
            addSolutionToRdfProblem(g, current_problem_id, solution_text)
            state = 0

        else:
            # continue ignoring the input, if something is not recognized
            state = 0
    g.serialize(destination=out_file)