import json
from flask import Blueprint, render_template, request, session
from eliozo.webmd_utils import fix_image_links, mathBeautify
from eliozo_dao.indexes_repository import (
    getSPARQLtopics,
    getSPARQLmethods,
    getSPARQLdomains,
    getSPARQLconcepts,
    getTopicDetails,
    getAllTopicChildren,
    getTopicProblemsSPARQL
)

indexes_bp = Blueprint('indexes', __name__)

@indexes_bp.route('/topics', methods=['GET', 'POST'])
def getTopics():
    data = json.loads(getSPARQLtopics())

    all_topics = []
    all_topic_info = dict() # Vārdnīca visai prasmju tabulai

    current_topic = "NA"

    for item in data['results']['bindings']:
        # A new topic appears
        if item['topicIdentifier']['value'] != current_topic:
            all_topics.append(item['topicIdentifier']['value']) # Pievienojam jaunu prasmi sarakstam all_topics
            current_topic = item['topicIdentifier']['value'] # Atceramies pēdējo pievienoto vērtību, lai neiespraustu atkārtoti
            current_topic_info = dict() # Vārdnīca vienai tabulas rindai
            current_topic_info['topicIdentifier'] = current_topic
            current_topic_info['topicNumber'] = item['topicNumber']['value']
            number_items = item['topicNumber']['value'].split(".")

            beautiful_description = mathBeautify(item['topicDescription']['value'])
            current_topic_info['topicDescription'] = beautiful_description
            current_topic_info['topicName'] = mathBeautify(item['topicName']['value'])
            if "problemid" in item:
                current_topic_info['problems'] = [item['problemid']['value']]
            else:
                current_topic_info['problems'] = []
            all_topic_info[current_topic] = current_topic_info # Lielajā vārdnīcā iesprauž mazo vārdnīcu
        else:
            current_topic_info['problems'].append(item['problemid']['value']) # Pievieno tikai jauno uzdevuma ID

    # domain_titles = {'1': 'Algebra', '2': 'Kombinatorika', '3': 'Ģeometrija', '4': 'Skaitļu teorija'}
    structured_topics = []
    current_LTopics = None
    current_subtopics = None
    current_subsubtopics = None
    for topic in all_topics:
        topicNumber = all_topic_info[topic]['topicNumber']
        topicId = all_topic_info[topic]['topicIdentifier']

        if topicNumber.endswith('.0.0.0.0'):
            LTopics = []
            current_LTopics = LTopics
            L1_number = topicNumber[:-len('.0.0.0.0')]
            L1_name = all_topic_info[topic]['topicName']
            L1_desc = all_topic_info[topic]['topicDescription']
            L1_prob = all_topic_info[topic]['problems']
            structured_topics.append({'number':L1_number,
                                        'topicId':topicId,
                                        'name':L1_name,
                                        'desc':L1_desc,
                                        'prob':L1_prob,
                                        'subtopics': LTopics})
        elif topicNumber.endswith('.0.0.0'):
            subtopics = []
            current_subtopics = subtopics
            L2_number = topicNumber[:-len('.0.0.0')]
            L2_label = L2_number.replace('.', '_')
            L2_name = all_topic_info[topic]['topicName']
            L2_desc = all_topic_info[topic]['topicDescription']
            L2_prob = all_topic_info[topic]['problems']
            current_LTopics.append({'number':L2_number,
                                    'topicId':topicId,
                                    'label':L2_label,
                                    'name':L2_name,
                                    'desc':L2_desc,
                                    'prob': L2_prob,
                                    'subtopics': subtopics})
        elif topicNumber.endswith('.0.0'):
            subsubtopics = []
            current_subsubtopics = subsubtopics
            L3_number = topicNumber[:-len('.0.0')]
            L3_name = all_topic_info[topic]['topicName']
            L3_desc = all_topic_info[topic]['topicDescription']
            L3_prob = all_topic_info[topic]['problems']
            current_subtopics.append({'number':L3_number,
                                        'topicId':topicId,
                                        'name':L3_name,
                                        'desc': L3_desc,
                                        'prob': L3_prob,
                                        'subtopics':subsubtopics})
        else:
            L45_number = topicNumber
            if topicNumber.endswith('.0'):
                L45_number = topicNumber[:-len('.0')]
            L45_name = all_topic_info[topic]['topicName']
            L45_desc = all_topic_info[topic]['topicDescription']
            L45_prob = all_topic_info[topic]['problems']
            current_subsubtopics.append({'number':L45_number,
                                            'topicId':topicId,
                                            'name':L45_name, 
                                            'desc': L45_desc, 
                                            'prob':L45_prob})

    template_context = {
        'all_topics': all_topics,
        'all_topic_info': all_topic_info,
        'active': 'order_by',
        'navlinks': [
            {
                'url': 'indexes.getTopics', 
                'title': 'Topics'
            }
        ],
        'title': 'Tēmas',
        'structured_topics': structured_topics
    }

    return render_template('topics_content.html', **template_context)


@indexes_bp.route('/methods', methods=['GET', 'POST'])
def getMethods():
    lang = session.get('lang', 'lv')
    data = json.loads(getSPARQLmethods())

    all_methods = []
    all_methods_info = dict()

    current_method = "NA"

    for item in data['results']['bindings']:
        if item['methodID']['value'] != current_method:
            current_method = item['methodID']['value']
            all_methods.append(current_method)

            current_method_info = dict()

            current_method_info['identifier'] = item['methodID']['value'][4:]
            current_method_info['number'] = item['methodNumber']['value']
            current_method_info['name'] = item['methodName']['value']
            current_method_info['description'] = item['methodDescription']['value']

            if "problemid" in item:
                current_method_info['problems'] = [item['problemid']['value']]
            else:
                current_method_info['problems'] = []
            all_methods_info[current_method] = current_method_info
        else:
            current_method_info['problems'].append(item['problemid']['value'])    


    template_context = {
        'active': 'order_by',
        'all_methods': all_methods, 
        'all_methods_info': all_methods_info,
        'navlinks': [
            { 'url': 'indexes.getMethods', 'title': 'Methods' }
        ],
        'title': 'Metodes'
    }
    return render_template('methods_content.html', **template_context)


@indexes_bp.route('/genres', methods=['GET', 'POST'])
def getGenres():
    lang = session.get('lang', 'lv')
    data = json.loads(getSPARQLdomains())

    all_genres = {'1':[], '2':[], '3':[], '4':[]}
    all_genres_info = dict()

    current_genre = "NA"

    for item in data['results']['bindings']:
        if item['domainNumber']['value'].endswith('0.0'):
            pass

        elif item['domainID']['value'] != current_genre:
            current_genre = item['domainID']['value']
            current_domain = item['L1']['value']
            all_genres[current_domain].append(item['domainID']['value'])

            current_genre_info = dict()
            current_genre_info['domainIdentifier'] = item['domainID']['value'][4:]
            current_genre_info['domainNumber'] = item['domainNumber']['value']
            current_genre_info['domainName'] = item['domainName']['value']
            beautiful_description = mathBeautify(item['domainDescription']['value'])
            current_genre_info['domainDescription'] = beautiful_description
            if "problemid" in item:
                current_genre_info['problems'] = [item['problemid']['value']]
            else:
                current_genre_info['problems'] = []
            all_genres_info[current_genre] = current_genre_info # Lielajā vārdnīcā iesprauž mazo vārdnīcu
        else:
            current_genre_info['problems'].append(item['problemid']['value']) # Pievieno tikai jauno uzdevuma ID


    template_context = {
        'all_genres': all_genres,
        'domain_names': {'1':'Alg', '2':'Comb', '3':'Geom', '4':'NT'},
        'domain_keys': ['1', '2', '3', '4'],
        'all_genres_info': all_genres_info,
        'active': 'order_by',
        'navlinks': [
            {
                'url': 'indexes.getGenres', 
                'title': 'Genres'
            }
        ],
        'title': 'Žanri'
    }
    return render_template('genres_content.html', **template_context)    


@indexes_bp.route('/concepts', methods=['GET','POST'])
def getConcepts():
    concepts_problems = json.loads(getSPARQLconcepts())

    concept_list = []
    current_concept = "NA"
    current_problems = []
    for item in concepts_problems['results']['bindings']:
        concept = item['concept']['value']
        if concept != current_concept:
            termLV = item['termLV']['value']
            termEN = item['termEN']['value']
            conceptID = item['conceptID']['value']
            descLV = ''
            if 'descLV' in item:
                descLV = mathBeautify(item['descLV']['value'])

            current_concept = concept
            current_problems = [item['problemID']['value']]
            concept_list.append({
                'termLV': termLV,
                'termEN': termEN,
                'conceptID': conceptID,
                'descLV': descLV,
                'problems': current_problems
            })

        else:
            current_problems.append(item['problemID']['value'])
    concept_list.append({
                'termLV': termLV,
                'termEN': termEN,
                'conceptID': conceptID,
                'descLV': descLV,
                'problems': current_problems})

    template_context = {
        'all_concepts': concept_list,
        'active': 'order_by',
        'navlinks': [
            {
                'url': 'indexes.getConcepts', 
                'title': 'Concepts'
            }
        ],
        'title': 'Jēdzieni'
    }
    return render_template('concepts_content.html', **template_context)

@indexes_bp.route('/topic_tasks', methods=['GET','POST']) # Kontrolieris, kas iegūst prasmes kopā ar uzdevumiem
def getTopic():
    topic = request.args.get('topicIdentifier')

    topic_details = json.loads(getTopicDetails(topic))
    parentNumber = topic_details['results']['bindings'][0]['topicNumber']['value']
    parentName = topic_details['results']['bindings'][0]['topicName']['value']
    parentDesc = topic_details['results']['bindings'][0]['topicDesc']['value']
    parentDesc = mathBeautify(parentDesc)

    all_topics = json.loads(getAllTopicChildren(topic))
    topic_list = []
    for topic_item in all_topics['results']['bindings']: # all_topics saraksts ar vārdnīcām
        prefLabel = topic_item['prefLabel']['value']
        topicName = topic_item['topicName']['value']
        topicName = mathBeautify(topicName)
        topicNum = topic_item['num']['value']
        dd = {'prefLabel': prefLabel, 'topicNum': topicNum, 'topicName': topicName}
        topic_list.append(dd)

    data = json.loads(getTopicProblemsSPARQL(topic))
    problem_list = []
    for data_item in data['results']['bindings']:
        problemTextHtml = data_item['text']['value']
        problemTextHtml = fix_image_links(problemTextHtml)
        problemTextHtml = mathBeautify(problemTextHtml)
        problem_list.append({'problemid': data_item['problemid']['value'], 'text': problemTextHtml})

    template_context = {
        'topic': topic,
        'parentNumber': parentNumber,
        'parentName': parentName,
        'parentDesc': parentDesc,
        'problem_list': problem_list,
        'topic_list' : topic_list,
        'active': 'order_by',
        'title': 'Tēma'
    }
    return render_template('topic_tasks_content.html', **template_context)
