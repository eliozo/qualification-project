from flask import Blueprint, render_template, request, session, url_for, json
import os
from eliozo.webmd_utils import mathBeautify, fix_image_links, get_cached_book_content
from eliozo_dao.problem_repository import (
    getSPARQLOlympiads,
    getSPARQLOlympiadTimeIDs,
    getSPARQLOlympiadTimeIDsGrades,
    getSPARQLOlympiadProblemsByEvent,
    getSPARQLOlympiadProblemsByEventAndGrade,
    getSPARQLProblem,
    getSPARQLProblemSolutions,
    getSPARQLVideoBookmarks,
    getAllSPARQLVideos
)

problems_bp = Blueprint('problems', __name__)

@problems_bp.route('/olympiads', methods=['GET', 'POST'])
def getOlympiads():
    lang = session.get('lang', 'lv')
    olympiads = json.loads(getSPARQLOlympiads(lang))
    olympiadData = []
    for rr in olympiads['results']['bindings']:
        olympiadName = rr['olympiadName']['value']
        olympiadDescription = rr['olympiadDescription']['value']
        olympiadCode = rr['olympiadCode']['value']

        country = ''
        if 'olympiadCountry' in rr:
            country = rr['olympiadCountry']['value']

        if olympiadCode not in ['AMO', 'NOL', 'SOL', 'VOL', 'IMOSHL']:
            continue

        olympiadEvents = []
        eventData = json.loads(getSPARQLOlympiadTimeIDs(country, olympiadCode))
        for event in eventData['results']['bindings']:
            timeID = event['problemTimeID']['value']
            isComplete = True
            olympiadEvents.append((timeID, isComplete))


        olympiadData.append({'olympiadName': olympiadName,
                                'olympiadDescription': olympiadDescription,
                                'olympiadCountry':country,
                                'olympiadCode': olympiadCode,
                                'olympiadEvents': olympiadEvents})

    template_context = {
        'links': olympiadData,
        'active': 'archive',
        'navlinks': [
            {'url':'problems.getOlympiads', 'title':'Olympiads'}
        ],
        'title': 'Arhīvs'
    }

    return render_template('archive_content.html', **template_context)

@problems_bp.route('/olympiad', methods=['GET', 'POST'])
def getOlympiad():
    country_id = request.args.get('country_id')
    olympiad_id= request.args.get('olympiad_id')
    olympiads = json.loads(getSPARQLOlympiadTimeIDsGrades(country_id, olympiad_id))

    all_events = []
    all_grades = dict()

    current_event = "NA"

    for item in olympiads['results']['bindings']:
        timeID = item['problemTimeID']['value']
        if timeID != current_event:
            all_events.append(timeID) # Pievienojam jaunu gadu sarakstam all_years
            current_event = timeID # Atceramies pēdējo pievienoto vērtību, lai neiespraustu atkārtoti
            all_grades[current_event] = ['NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA', 'NA'] # Sagatavojamies pievienot visas klases
        grade = int(item['grade']['value'])
        all_grades[current_event][grade-5] = item['grade']['value'] # 0. 5.klase, 1. 6.klase utt.

    template_context = {
        'all_events': all_events,
        'all_grades': all_grades,
        'country_id': country_id,
        'olympiad_id': olympiad_id,
        'active': 'archive',
        'title': 'Olimpiāde'
    }
    return render_template('olympiad_content.html', **template_context)

@problems_bp.route('/grade', methods=['GET', 'POST'])
def getGrades():
    lang = session.get('lang', 'lv')
    event = request.args.get('event')
    country = request.args.get('country')
    grade = request.args.get('grade')
    olympiad= request.args.get('olympiad')
    if grade == '-1':
        link = json.loads(getSPARQLOlympiadProblemsByEvent(event, country, olympiad, lang))
    else:
        link = json.loads(getSPARQLOlympiadProblemsByEventAndGrade(event, country, grade, olympiad, lang))

    problems_map = {}
    
    for item in link['results']['bindings']:
        problem_id_value = item['problemid']['value']
        problem_number_value = item['problem_number']['value']
        if grade == -1:
            problem_grade_value = item['problem_grade']['value']
        else:
            problem_grade_value = grade
        
        problem_text_value = item['text']['value']
        problem_text_value = fix_image_links(problem_text_value)
        problem_text_value = mathBeautify(problem_text_value)
        
        problem_lang = item['text'].get('xml:lang', 'unk')

        if problem_id_value not in problems_map:
            problems_map[problem_id_value] = {
                'problemid': problem_id_value,
                'problem_number': problem_number_value,
                'problem_grade': problem_grade_value,
                'translations': {}
            }
        
        problems_map[problem_id_value]['translations'][problem_lang] = problem_text_value

    problems = list(problems_map.values())
    
    try:
            problems.sort(key=lambda x: (int(x['problem_grade']), int(x['problem_number'])))
    except ValueError:
            problems.sort(key=lambda x: (x['problem_grade'], x['problem_number']))

    for p in problems:
        available_langs = sorted(list(p['translations'].keys()))
        if lang in p['translations']:
            p['text'] = p['translations'][lang]
            p['current_lang'] = lang
        elif 'lv' in p['translations']:
            p['text'] = p['translations']['lv']
            p['current_lang'] = 'lv'
        elif 'en' in p['translations']:
            p['text'] = p['translations']['en']
            p['current_lang'] = 'en'
        else:
            first_lang = available_langs[0]
            p['text'] = p['translations'][first_lang]
            p['current_lang'] = first_lang
        
        p['available_langs'] = available_langs


    template_context = {
        'problems': problems,
        'event': event,
        'country': country,
        'grade': grade,
        'olympiad': olympiad,
        'active': 'archive',
        'navlinks': [
            {
                'url': 'problems.getOlympiads', 
                'title': 'Olympiads'
            }, 
            {
                'url': 'problems.getGrades', 
                'params': {
                    'event': event, 
                    'country': country, 
                    'grade': grade, 
                    'olympiad': olympiad
                },
                'title': f'{country}.{olympiad}.{event}'
            }
        ],
        'title': f'{country}.{olympiad}.{event}'
    }

    return render_template('grade_content.html', **template_context)

@problems_bp.route('/problem', methods=['GET','POST'])
def getProblem():
    lang = session.get('lang', 'lv')
    problemid = request.args.get('problemid')
    
    solnData = json.loads(getSPARQLProblemSolutions(problemid, lang))
    hasSolution = False
    if 'results' in solnData and 'bindings' in solnData['results']:
            for item in solnData['results']['bindings']:
                if 'solutionTextHtml' in item:
                    hasSolution = True
                    break

    data = json.loads(getSPARQLProblem(problemid, lang))
    
    problem_translations = {}
    
    first_binding = None
    if 'results' in data and 'bindings' in data['results'] and len(data['results']['bindings']) > 0:
        first_binding = data['results']['bindings'][0]
        for item in data['results']['bindings']:
            if 'problemTextHtml' in item:
                p_text = item['problemTextHtml']['value']
                p_lang = item['problemTextHtml'].get('xml:lang', 'unk')
                problem_translations[p_lang] = mathBeautify(fix_image_links(p_text))

    problemTextHtml = ""
    available_langs = sorted(list(problem_translations.keys()))
    current_lang = lang

    if lang in problem_translations:
        problemTextHtml = problem_translations[lang]
        current_lang = lang
    elif 'lv' in problem_translations:
        problemTextHtml = problem_translations['lv']
        current_lang = 'lv'
    elif 'en' in problem_translations:
        problemTextHtml = problem_translations['en']
        current_lang = 'en'
    elif len(available_langs) > 0:
        current_lang = available_langs[0]
        problemTextHtml = problem_translations[current_lang]
    
    problem = {
        'problemid': problemid,
        'translations': problem_translations,
        'available_langs': available_langs,
        'current_lang': current_lang
    }

    if 'video' in first_binding:
        hasVideo = first_binding['video']['value'] != ''
    else:
        hasVideo = False

    bookmarks = []
    video_title = "NA"
    youtubeID = "NA"

    if hasVideo:
        video_data = json.loads(getSPARQLVideoBookmarks(problemid))
        for item in video_data['results']['bindings']:
            video_title = item['videoTitle']['value']
            youtubeID = item['youtubeID']['value']
            if 'tstamp' in item:
                minutes = int(item['tstamp']['value']) // 60
                if minutes < 10:
                    minutes = '0' + str(minutes)
                seconds = int(item['tstamp']['value']) % 60
                if seconds < 10:
                    seconds = '0' + str(seconds)
                bookmarks.append({'tstamp': item['tstamp']['value'], 'bmtext': item['bmtext']['value'], 'minutes': minutes, 'sec': seconds}) 

    metaitems = []
    problemYear = "NA"
    country = "NA"
    olympiad = "NA"
    problemBook = "NA"
    problemBookSection = "NA"
    problemGrade = "NA"
    problem_number = "NA"
    methodIdentifier = "NA"
    topicIdentifier = "NA"
    concepts = "NA"
    questionType = "NA"
    domain = "NA"

    metaitems.append({'key':'problemID','value': problemid})

    if first_binding:
        if 'problemYear' in first_binding:
            problemYear = first_binding['problemYear']['value']
        if 'country' in first_binding:
            country = first_binding['country']['value']
        if 'olympiad' in first_binding:
            olympiad = first_binding['olympiad']['value']
        if 'problemBook' in first_binding:
            problemBook = first_binding['problemBook']['value']
        if 'problemBookSection' in first_binding:
            problemBookSection = first_binding['problemBookSection']['value']
        if 'problemGrade' in first_binding:
            problemGrade = first_binding['problemGrade']['value']
        if 'problem_number' in first_binding:
            problem_number = first_binding['problem_number']['value']
        if 'topicIdentifier' in first_binding:
            topicIdentifier = first_binding['topicIdentifier']['value']
        if 'methodIdentifier' in first_binding:
            methodIdentifier = first_binding['methodIdentifier']['value']
        if 'concepts' in first_binding:
            concepts = first_binding['concepts']['value']
        if 'questionType' in first_binding:
            questionType = first_binding['questionType']['value']
        if 'domain' in first_binding:
            domain = first_binding['domain']['value']

    if problemYear != 'NA':
        metaitems.append({'key':'year', 'value': problemYear})
        if country != 'NA':
            metaitems.append({'key':'country', 'value': country})
        if olympiad != 'NA':
            metaitems.append({'key': 'olympiad', 'value': olympiad})
        if problemGrade != 'NA':
            metaitems.append({'key': 'grade', 'value': problemGrade})
    else:
        if problemBook != 'NA':
            metaitems.append({'key': 'book', 'value': problemBook})
        if problemBookSection != 'NA':
            metaitems.append({'key': 'section', 'value': problemBookSection})

    all_topics = []
    if problem_number != 'NA':
        metaitems.append({'key': 'num', 'value': problem_number})
    if methodIdentifier != 'NA':
        metaitems.append({'key': 'method', 'value': methodIdentifier})
    if topicIdentifier != 'NA':
        metaitems.append({'key': 'topic', 'value': topicIdentifier})
        all_topics.append(topicIdentifier)
    if concepts != 'NA':
        metaitems.append({'key': 'concepts', 'value': concepts.replace('http://www.dudajevagatve.lv/eliozo#TRM-','')})
    if questionType != 'NA':
        metaitems.append({'key': 'questionType', 'value': questionType})
    if domain in ['Alg', 'Comb', 'Geom', 'NT']:
        all_domains = {"Alg":"Algebra", "Comb":"Kombinatorika", "Geom":"Ģeometrija", "NT":"Skaitļu teorija"}
        metaitems.append({'key': 'domain', 'value': all_domains[domain]})

    unique_sorted_topics = list(sorted(set(all_topics)))

    template_context = {
        'problemid': problemid,
        'problem': problem, 
        'data': data['results']['bindings'], 
        'topics': unique_sorted_topics,
        'problemTextHtml': problemTextHtml, 
        'hasVideo': hasVideo,
        'video_title': video_title,
        'bookmarks': bookmarks,
        'youtubeID': youtubeID,
        'hasSolution': hasSolution,
        'active': 'archive',
        'title': 'Uzdevums',
        'metaitems': metaitems
    }
    return render_template('problem_content.html', **template_context)


@problems_bp.route('/problem_solution', methods=['GET','POST'])
def getProblemSolution():
    problemid = request.args.get('problemid')
    lang = session.get('lang', 'lv')
    data = json.loads(getSPARQLProblemSolutions(problemid, lang))

    problem_translations = {}
    solutions_map = {} 
    
    for item in data['results']['bindings']:
        # Problem Text
        if 'problemTextHtml' in item:
            p_text = item['problemTextHtml']['value']
            p_lang = item['problemTextHtml'].get('xml:lang', 'unk')
            if p_lang not in problem_translations:
                problem_translations[p_lang] = mathBeautify(fix_image_links(p_text))
        
        # Solution Text
        if 'solutionTextHtml' in item:
            s_text = item['solutionTextHtml']['value']
            s_lang = item['solutionTextHtml'].get('xml:lang', 'unk')
            s_id = "default"
            if 'solutionID' in item:
                s_id = item['solutionID']['value']

            if s_id not in solutions_map:
                solutions_map[s_id] = {}
            solutions_map[s_id][s_lang] = mathBeautify(fix_image_links(s_text))

    problemTextHtml = ""
    available_langs = sorted(list(problem_translations.keys()))
    current_lang = lang

    if lang in problem_translations:
        problemTextHtml = problem_translations[lang]
        current_lang = lang
    elif 'lv' in problem_translations:
        problemTextHtml = problem_translations['lv']
        current_lang = 'lv'
    elif 'en' in problem_translations:
        problemTextHtml = problem_translations['en']
        current_lang = 'en'
    elif len(available_langs) > 0:
        current_lang = available_langs[0]
        problemTextHtml = problem_translations[current_lang]
    
    problem = {
        'problemid': problemid,
        'translations': problem_translations,
        'available_langs': available_langs,
        'current_lang': current_lang
    }
    
    solutions = []
    for s_id in sorted(solutions_map.keys()):
        s_trans = solutions_map[s_id]
        s_avail = sorted(list(s_trans.keys()))
        s_curr = lang
        s_text = ""
        if lang in s_trans:
            s_text = s_trans[lang]
            s_curr = lang
        elif 'lv' in s_trans:
            s_text = s_trans['lv']
            s_curr = 'lv'
        elif 'en' in s_trans:
            s_text = s_trans['en']
            s_curr = 'en'
        elif len(s_avail) > 0:
            s_curr = s_avail[0]
            s_text = s_trans[s_curr]
            
        solutions.append({
            'id': s_id,
            'translations': s_trans,
            'available_langs': s_avail,
            'current_lang': s_curr,
            'text': s_text
        })

    template_context = {
        'problemid': problemid,
        'data': data['results']['bindings'],
        'problem': problem,
        'problemTextHtml': problemTextHtml,
        'solutions': solutions,
        'active': 'archive',
        'title': 'Uzdevums'
    }
    return render_template('problem_solution_content.html', **template_context)

@problems_bp.route("/video")
def getVideo():
    data = json.loads(getAllSPARQLVideos())

    all_problemids = []

    for item in data['results']['bindings']:
        problemID = item['problemid']['value']
        text = item['text']['value']
        text = text.replace("$$", "$")
        text = text[:80]
        # text = mathBeautify(text)
        textHtml = item['textHtml']['value']
        all_problemids.append({'problemID': problemID, 'text': text, 'textHtml': textHtml})

    template_context = {
        'all_problemids' : all_problemids,
        'active': 'statistics',
        'navlinks': [
            {'url':'problems.getVideo', 'title':'Video'}
        ],
        'title': 'Video'
    }

    return render_template('video_content.html', **template_context)


@problems_bp.route('/book_full', methods=['GET', 'POST'])
def getBookFull():
    subdir = request.args.get('subdir')
    
    problembase_root = os.getenv('PROBLEMBASE_ROOT')
    
    content = get_cached_book_content(subdir, problembase_root)
    
    template_context = {
        'content': content,
        'subdir': subdir,
        'active': 'archive',
        'title': 'Grāmata'
    }
    return render_template('book_full.html', **template_context)

