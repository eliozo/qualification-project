"""The nested About Us > Ontology > ... menu, on every page."""

import re

import pytest


@pytest.fixture
def client():
    import eliozo
    return eliozo.create_app({'TESTING': True}).test_client()


def _set_lang(client, lang):
    with client.session_transaction() as s:
        s['lang'] = lang


def _submenu(html):
    m = re.search(r'<li class="nav-submenu[^"]*">(.*?)</ul>\s*</li>', html, re.S)
    assert m, 'no nested menu'
    return m.group(0)


def test_ontology_menu_lists_the_overview_and_its_subpages(client):
    _set_lang(client, 'lv')
    html = client.get('/content/search_by_keyword').get_data(as_text=True)
    menu = _submenu(html)
    links = re.findall(r'<a href="([^"]+)">\s*([^<]+?)\s*</a>', menu)
    assert links[0] == ('/ontology', 'Ontoloģija')
    assert ('/content/ontology_question_types', 'Jautājumu tipi') in links
    assert len(links) == 10
    assert re.search(r'<ul class="nav-submenu-list"[^>]*\bhidden\b', menu)   # folded elsewhere


def test_ontology_menu_is_unfolded_on_a_subpage(client):
    _set_lang(client, 'en')
    html = client.get('/content/ontology_question_types').get_data(as_text=True)
    menu = _submenu(html)
    assert 'aria-expanded="true"' in menu
    assert not re.search(r'<ul class="nav-submenu-list"[^>]*\bhidden\b', menu)
    assert re.search(r'<li class="current">\s*<a href="/content/ontology_question_types">Question types</a>', menu)
    # Breadcrumb: About Us > Ontology > Question types
    assert re.search(r'<b>Question types</b>', html)
