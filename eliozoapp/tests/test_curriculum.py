"""The /getCurriculum form: chips for olympiads and grades, year dropdowns
computed from the archive; nothing selected means all."""

import re

import pytest

CURRICULUM_TTL = """
@prefix eliozo: <http://www.dudajevagatve.lv/eliozo#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

eliozo:LV.AMO.1988.4.1 a eliozo:Problem ; eliozo:problemID "LV.AMO.1988.4.1" ;
    eliozo:olympiad "LV.AMO" ; eliozo:problemYear 1988 ; eliozo:problemGrade 4 ;
    eliozo:domain "Alg" ; eliozo:questionType "QTY_Prove" .
eliozo:LV.AMO.2011.7.1 a eliozo:Problem ; eliozo:problemID "LV.AMO.2011.7.1" ;
    eliozo:olympiad "LV.AMO" ; eliozo:problemYear 2011 ; eliozo:problemGrade 7 ;
    eliozo:domain "Comb" ; eliozo:questionType "QTY_FindAll" .
eliozo:LV.SOL.2020.9.1 a eliozo:Problem ; eliozo:problemID "LV.SOL.2020.9.1" ;
    eliozo:problemTextHtml "<p>Pierādi, ka trijstūrī ...</p>"@lv ;
    eliozo:olympiad "LV.SOL" ; eliozo:problemYear 2020 ; eliozo:problemGrade 9 ;
    eliozo:domain "Geom" ; eliozo:questionType "QTY_ProveUniversal" .
eliozo:LV.SOL.2020.9.2 a eliozo:Problem ; eliozo:problemID "LV.SOL.2020.9.2" ;
    eliozo:olympiad "LV.SOL" ; eliozo:problemYear 2020 ; eliozo:problemGrade 9 ;
    eliozo:questionType "QTY_ProveUniversal" .
eliozo:LV.SOL.2020.9.10 a eliozo:Problem ; eliozo:problemID "LV.SOL.2020.9.10" ;
    eliozo:olympiad "LV.SOL" ; eliozo:problemYear 2020 ; eliozo:problemGrade 9 ;
    eliozo:domain "Geom" ; eliozo:questionType "QTY_ProveUniversal" .
# Question types v2 (as in skos-questions.ttl made from questionTypes2.csv)
eliozo:QTY_Find a eliozo:Question ; eliozo:questionID "QTY_Find" ; eliozo:sorter_L1 1 ; eliozo:sorter_L2 0 ;
    eliozo:questionName "Atrast"@lv, "Find"@en .
eliozo:QTY_FindAll a eliozo:Question ; eliozo:questionID "QTY_FindAll" ; eliozo:sorter_L1 1 ; eliozo:sorter_L2 1 ;
    eliozo:questionName "Atrast visus atrisinājumus"@lv, "Find All Solutions"@en ;
    eliozo:questionCanonical "Atrodi visus …"@lv, "Find all …"@en ;
    eliozo:questionDescription "Atrast visus un pamatot, ka citu nav."@lv ;
    eliozo:questionRequiredParts "visas atbildes"@lv ; skos:broader eliozo:QTY_Find .
eliozo:QTY_Prove a eliozo:Question ; eliozo:questionID "QTY_Prove" ; eliozo:sorter_L1 3 ; eliozo:sorter_L2 0 ;
    eliozo:questionName "Pierādīt"@lv, "Prove"@en ; eliozo:questionCanonical "Pierādi, ka …"@lv .
eliozo:QTY_ProveUniversal a eliozo:Question ; eliozo:questionID "QTY_ProveUniversal" ;
    eliozo:sorter_L1 3 ; eliozo:sorter_L2 2 ; skos:broader eliozo:QTY_Prove ;
    eliozo:questionName "Pierādīt vispārīgu apgalvojumu"@lv, "Prove a General Statement"@en ;
    eliozo:questionCanonical "Pierādi, ka visiem …"@lv .
# Not a curriculum olympiad: its year and grade must not appear on the form
eliozo:LV.TST.1970.2.1 a eliozo:Problem ; eliozo:problemID "LV.TST.1970.2.1" ;
    eliozo:olympiad "LV.TST" ; eliozo:problemYear 1970 ; eliozo:problemGrade 2 ;
    eliozo:domain "NT" ; eliozo:questionType "Prove" .
"""


@pytest.fixture
def client(monkeypatch):
    from pyoxigraph import RdfFormat, Store

    import eliozo
    import eliozo_dao

    store = Store()
    store.load(input=CURRICULUM_TTL, format=RdfFormat.TURTLE)
    monkeypatch.setattr(eliozo_dao, "_store", store, raising=False)
    return eliozo.create_app({'TESTING': True}).test_client()


def options(html, name):
    select = re.search(r'<select name="%s".*?</select>' % name, html, re.DOTALL).group(0)
    return re.findall(r'<option value="(\d+)" (selected)?', select)


def chips(html, name):
    return re.findall(r'name="%s" id="[^"]+" value="([^"]+)"\s*(checked)?' % name, html)


def qtype_problems(html):
    """Problem IDs linked from the Question Types tab."""
    tab = re.search(r'<div id="matrix".*?</ul>', html, re.DOTALL).group(0)
    return re.findall(r'problemid=([\w.]+)', tab)


def matrix_total(html):
    return len(qtype_problems(html))


def test_default_form_shows_archive_coverage_and_queries_everything(client):
    with client.session_transaction() as session:
        session['lang'] = 'en'
    html = client.get('/getCurriculum').get_data(as_text=True)

    assert options(html, 'year_from') == [('1988', 'selected'), ('2011', ''), ('2020', '')]
    assert options(html, 'year_to') == [('1988', ''), ('2011', ''), ('2020', 'selected')]
    assert 'Archive: 1988&ndash;2020' in html
    assert chips(html, 'olympiad') == [('LV.AMO', ''), ('LV.NOL', ''), ('LV.VOL', ''), ('LV.SOL', '')]
    assert chips(html, 'grade') == [('4', ''), ('7', ''), ('9', '')]
    assert matrix_total(html) == 5


def test_selected_chips_and_years_filter_the_results(client):
    html = client.get('/getCurriculum?olympiad=LV.AMO&grade=4&grade=9').get_data(as_text=True)
    assert ('LV.AMO', 'checked') in chips(html, 'olympiad')
    assert chips(html, 'grade') == [('4', 'checked'), ('7', ''), ('9', 'checked')]
    assert qtype_problems(html) == ['LV.AMO.1988.4.1']

    html = client.get('/getCurriculum?year_from=2011&year_to=2020').get_data(as_text=True)
    assert matrix_total(html) == 4


def test_invalid_values_are_ignored(client):
    html = client.get('/getCurriculum?olympiad=LV.TST&grade=x&grade=2'
                      '&year_from=2020&year_to=1900').get_data(as_text=True)
    assert all(not checked for _, checked in chips(html, 'olympiad') + chips(html, 'grade'))
    # Years are clamped to the archive and put in order
    assert ('1988', 'selected') in options(html, 'year_from')
    assert ('2020', 'selected') in options(html, 'year_to')
    assert matrix_total(html) == 5


def visible_text(html):
    """Page text without tags and attributes, as the visitor sees it."""
    html = re.sub(r'<(script|style)\b.*?</\1>', ' ', html, flags=re.DOTALL)
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html))


def test_question_types_list_problems_by_domain(client):
    html = client.get('/getCurriculum').get_data(as_text=True)
    tab = re.search(r'<div id="matrix".*?</ul>', html, re.DOTALL).group(0)
    items = [re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', li)).strip()
             for li in re.findall(r'<li[^>]*>(.*?)</li>', tab, re.DOTALL)]
    # Vocabulary order (1.1, 3.0, 3.2); title and canonical question, description and
    # required parts in the tooltip; domains without problems left out, problems without
    # a domain listed as NA, problem IDs in natural order (9.2 before 9.10)
    assert items == [
        'Atrast visus atrisinājumus – Atrodi visus … Atrast visus un pamatot, ka citu nav. '
        'Nepieciešamās daļas: visas atbildes Comb: LV.AMO.2011.7.1',
        'Pierādīt – Pierādi, ka … Alg: LV.AMO.1988.4.1',
        'Pierādīt vispārīgu apgalvojumu – Pierādi, ka visiem … Geom: LV.SOL.2020.9.1 , LV.SOL.2020.9.10 '
        'NA: LV.SOL.2020.9.2',
    ]
    assert 'margin-left' in re.findall(r'<li[^>]*>', tab)[2]  # a subtype is indented
    assert 'QTY_' not in visible_text(tab)

    with client.session_transaction() as session:
        session['lang'] = 'en'
    tab = client.get('/getCurriculum').get_data(as_text=True)
    assert 'Find All Solutions' in tab and 'Prove a General Statement' in tab


def test_filter_by_question_type_includes_subtypes(client):
    html = client.get('/filter?questionType=QTY_Prove').get_data(as_text=True)
    found = set(re.findall(r'problemid=([\w.]+)', html))
    # a group type matches its subtypes; the legacy value "Prove" (LV.TST.1970.2.1) does not match
    assert found == {'LV.AMO.1988.4.1', 'LV.SOL.2020.9.1', 'LV.SOL.2020.9.2', 'LV.SOL.2020.9.10'}
    start = html.index('name="questionType"')
    box = visible_text(html[html.rindex('<div', 0, start):html.index('</div>', start)])
    assert 'QTY_' not in box
    assert 'Pierādīt [4]' in box and 'Pierādīt vispārīgu apgalvojumu [3]' in box

    html = client.get('/filter?questionType=QTY_ProveUniversal').get_data(as_text=True)
    assert set(re.findall(r'problemid=([\w.]+)', html)) == {'LV.SOL.2020.9.1', 'LV.SOL.2020.9.2', 'LV.SOL.2020.9.10'}

    # Unknown values (legacy or injected) are ignored
    html = client.get('/filter?questionType=Prove%22%20.%20%7D').get_data(as_text=True)
    assert 'questionType' in html


def test_problem_page_shows_question_type_names(client):
    html = client.get('/problem?problemid=LV.SOL.2020.9.1').get_data(as_text=True)
    # the metadata shown in the problem's info popup
    assert "'questionType': 'Pierādīt vispārīgu apgalvojumu'" in html
    assert 'QTY_ProveUniversal' not in html
