from flask import Blueprint, render_template, request, session, url_for, json
import os
import re
from eliozo.webmd_utils import mathBeautify, fix_image_links, get_cached_book_content
from eliozo_dao.problem_listing import UNTAGGED, chooseTranslation, collectTranslation
from eliozo_dao.question_type_repository import getQuestionTypes, questionTypeName
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
            all_grades[current_event] = [] # Šī gada klases (jebkuras no 1 līdz 12)
        grade = int(item['grade']['value'])
        if grade not in all_grades[current_event]:
            all_grades[current_event].append(grade)

    for grades in all_grades.values():
        grades.sort()

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
        if grade == '-1':
            problem_grade_value = item.get('problem_grade', {}).get('value')
        else:
            problem_grade_value = grade

        problem_text_value = item['text']['value']
        problem_text_value = fix_image_links(problem_text_value)
        problem_text_value = mathBeautify(problem_text_value)

        problem_lang = item['text'].get('xml:lang', UNTAGGED)

        if problem_id_value not in problems_map:
            problems_map[problem_id_value] = {
                'problemid': problem_id_value,
                'problem_number': problem_number_value,
                'problem_grade': problem_grade_value,
                'translations': {}
            }

        collectTranslation(problems_map[problem_id_value]['translations'], problem_lang, problem_text_value)

    problems = list(problems_map.values())

    # Sort by grade (problems without a numeric grade go last), then by problem id
    # with numeric parts compared as numbers (so "9.2" comes before "9.10").
    def problem_sort_key(p):
        try:
            grade_key = (0, int(p['problem_grade']))
        except (TypeError, ValueError):
            grade_key = (1, 0)
        id_key = [(0, int(part), '') if part.isdigit() else (1, 0, part)
                  for part in re.split(r'(\d+)', p['problemid'])]
        return (grade_key, id_key)

    problems.sort(key=problem_sort_key)

    for p in problems:
        p['current_lang'] = chooseTranslation(p['translations'], lang)
        p['text'] = p['translations'].get(p['current_lang'], '')
        p['available_langs'] = sorted(list(p['translations'].keys()))


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
                p_lang = item['problemTextHtml'].get('xml:lang', UNTAGGED)
                collectTranslation(problem_translations, p_lang, mathBeautify(fix_image_links(p_text)))

    available_langs = sorted(list(problem_translations.keys()))
    # A "lang" URL parameter (the notes on search results link with one) picks
    # the translation shown first; otherwise the shared precedence rules do.
    current_lang = chooseTranslation(problem_translations, lang, request.args.get('lang'))
    problemTextHtml = problem_translations.get(current_lang, "")

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
    # All the question types of the problem (and of its sub-parts), by their names
    question_type_ids = list(dict.fromkeys(b['questionType']['value'] for b in data['results']['bindings']
                                           if 'questionType' in b)) if first_binding else []
    if question_type_ids:
        question_types = getQuestionTypes(session.get('lang', 'lv'))
        metaitems.append({'key': 'questionType',
                          'value': ', '.join(questionTypeName(question_types, q) for q in question_type_ids)})
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


# Solution headings by language, for solutions whose text has no heading of its own.
SOLUTION_TITLES = {'lv': 'Atrisinājums', 'en': 'Solution', 'lt': 'Sprendimas', 'et': 'Lahendus'}

SOLUTION_HEADING_RE = re.compile(r'^\s*<h2[^>]*>(.*?)</h2>\s*', re.DOTALL)


def splitSolutionHeading(html):
    """Split '<h2>Atrisinājums-2</h2>...' into ('Atrisinājums', '...'); (None, html) without a heading."""
    m = SOLUTION_HEADING_RE.match(html)
    if not m:
        return None, html
    title = re.sub(r'[\s.]*-?\s*\d*\s*$', '', m.group(1).strip())
    return (title or None), html[m.end():]


def solutionNumber(solution_id):
    """N from 'SOLN.LV.AMO.2022B.12.4.SUB<N>', so that SUB10 sorts after SUB2."""
    m = re.search(r'(\d+)$', solution_id)
    return int(m.group(1)) if m else 0


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
            p_lang = item['problemTextHtml'].get('xml:lang', UNTAGGED)
            collectTranslation(problem_translations, p_lang, mathBeautify(fix_image_links(p_text)))

        # Solution Text
        if 'solutionTextHtml' in item:
            s_text = item['solutionTextHtml']['value']
            s_lang = item['solutionTextHtml'].get('xml:lang', UNTAGGED)
            s_id = "default"
            if 'solutionID' in item:
                s_id = item['solutionID']['value']

            s_title, s_text = splitSolutionHeading(s_text)
            soln = solutions_map.setdefault(s_id, {'translations': {}, 'titles': {}})
            collectTranslation(soln['translations'], s_lang, mathBeautify(fix_image_links(s_text)))
            soln['titles'].setdefault(s_lang, s_title or SOLUTION_TITLES.get(s_lang, SOLUTION_TITLES['en']))

    # A "lang" URL parameter (the notes on search results link with one) picks
    # the translation shown first; otherwise the shared precedence rules do.
    requested_lang = request.args.get('lang')

    available_langs = sorted(list(problem_translations.keys()))
    current_lang = chooseTranslation(problem_translations, lang, requested_lang)
    problemTextHtml = problem_translations.get(current_lang, "")

    problem = {
        'problemid': problemid,
        'translations': problem_translations,
        'available_langs': available_langs,
        'current_lang': current_lang
    }

    solutions = []
    s_ids = [s_id for s_id in solutions_map if solutions_map[s_id]['translations']]
    s_ids.sort(key=lambda s_id: (solutionNumber(s_id), s_id))
    for num, s_id in enumerate(s_ids, start=1):
        s_trans = solutions_map[s_id]['translations']
        # A solution starts in the problem's language (if it has that translation)
        if current_lang in s_trans:
            s_curr = current_lang
        else:
            s_curr = chooseTranslation(s_trans, lang, requested_lang)
        # "Atrisinājums-2" when there are several solutions, plain "Atrisinājums" for the only one
        titles = {l: (f'{t}-{num}' if len(s_ids) > 1 else t)
                  for l, t in solutions_map[s_id]['titles'].items()}
        solutions.append({
            'id': s_id,
            'num': num,
            'titles': titles,
            'translations': s_trans,
            'available_langs': sorted(list(s_trans.keys())),
            'current_lang': s_curr,
            'text': s_trans[s_curr]
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
    page = request.args.get('page', 1, type=int)
    per_page = 48  # Number of thumbnails per page

    data = json.loads(getAllSPARQLVideos())

    all_problemids = []

    for item in data['results']['bindings']:
        problemID = item['problemid']['value']
        text = item['text']['value']
        text = text.replace("$$", "$")
        # text = mathBeautify(text)  # Commented out in original
        textHtml = item['textHtml']['value']
        youtubeID = item.get('youtubeID', {}).get('value', '')

        if youtubeID:
            all_problemids.append({
                'problemID': problemID,
                'text': text,
                'textHtml': textHtml,
                'youtubeID': youtubeID
            })

    # Pagination logic
    total_videos = len(all_problemids)
    total_pages = (total_videos + per_page - 1) // per_page

    # Ensure page is within valid range
    if page < 1: page = 1
    if page > total_pages and total_pages > 0: page = total_pages

    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page

    paginated_videos = all_problemids[start_idx:end_idx]

    template_context = {
        'all_problemids' : paginated_videos,
        'page': page,
        'total_pages': total_pages,
        'active': 'archive',
        'navlinks': [
            {'url':'problems.getVideo', 'title':'Video'}
        ],
        'title': 'Video Galerija'
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

