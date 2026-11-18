"""The nested Info > Plain Search / Advanced Search > ... menus, on every page."""

import re

import pytest


@pytest.fixture
def client():
    import eliozo
    return eliozo.create_app({'TESTING': True}).test_client()


def _set_lang(client, lang):
    with client.session_transaction() as s:
        s['lang'] = lang


def _submenus(html):
    return re.findall(r'<li class="nav-submenu[^"]*">.*?</ul>\s*</li>', html, re.S)


def _submenu(html):
    """The Advanced Search (ontology) nested menu."""
    menus = [m for m in _submenus(html) if '/ontology"' in m]
    assert menus, 'no nested menu'
    return menus[0]


def _links(menu):
    return re.findall(r'<a href="([^"]+)">\s*([^<]+?)\s*</a>', menu)


def test_ontology_menu_lists_the_overview_and_its_subpages(client):
    _set_lang(client, 'lv')
    html = client.get('/content/search_by_keyword').get_data(as_text=True)
    menu = _submenu(html)
    links = _links(menu)
    assert links[0] == ('/ontology', 'Paplašinātā meklēšana')
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
    # Breadcrumb: Info > Ontology > Question types
    assert re.search(r'<b>Question types</b>', html)


def test_plain_search_menu_is_a_node_with_the_three_search_modes(client):
    _set_lang(client, 'en')
    html = client.get('/content/search_by_meaning').get_data(as_text=True)
    menu = [m for m in _submenus(html) if 'Plain Search' in m]
    assert len(menu) == 1
    menu = menu[0]
    # No page of its own: the label is the toggle button, not a link
    assert re.search(r'<button[^>]*nav-submenu-label[^>]*>\s*Plain Search', menu)
    assert _links(menu) == [('/content/search_by_keyword', 'Exact Search'),
                            ('/content/search_by_regex', 'Regex Search'),
                            ('/content/search_by_meaning', 'Semantic Search')]
    assert 'aria-expanded="true"' in menu      # unfolded on its own page
    assert re.search(r'Info\s*&gt;\s*Plain Search\s*&gt;', html)    # breadcrumb
    assert '<b>Semantic Search</b>' in html


def test_main_page_radio_labels(client):
    _set_lang(client, 'en')
    html = client.get('/').get_data(as_text=True)
    for label in ('Exact', 'Regex', 'Semantic'):
        assert re.search(r'name="searchMode"[^>]*>\s*%s\s*</label>' % label, html)
