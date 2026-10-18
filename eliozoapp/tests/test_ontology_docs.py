"""Tests for the ontology documentation under ``eliozo/content/ontology*``.

Every document must exist in all three languages, render, link only to pages
that exist, and contain SPARQL examples that the advanced search accepts.
The examples are only parsed here (on the small fixture store), not checked for
results: the real problem base changes with every import.
"""

import glob
import os
import re

import pytest
from pyoxigraph import Store

from eliozo_dao.advanced_search_repository import check_query, collect_rows

CONTENT_ROOT = os.path.join(os.path.dirname(__file__), '..', 'eliozo', 'content')
LANGS = ('en', 'lv', 'lt')
DOCS = sorted(os.path.basename(d) for d in glob.glob(os.path.join(CONTENT_ROOT, 'ontology*'))
              if os.path.isdir(d))
LINK_RE = re.compile(r'\]\((/[^)\s]*)\)')


def _text(doc, lang):
    with open(os.path.join(CONTENT_ROOT, doc, 'content_%s.md' % lang), encoding='utf-8') as f:
        return f.read()


def _sparql_examples(text):
    """The indented code blocks that contain a SELECT query."""
    blocks, current = [], []
    for line in text.split('\n') + ['end']:
        if line.startswith('    '):
            current.append(line[4:])
        elif line.strip():
            if current:
                blocks.append('\n'.join(current))
            current = []
    return [b for b in blocks if 'SELECT' in b]


@pytest.fixture
def client():
    import eliozo
    return eliozo.create_app({'TESTING': True}).test_client()


def _set_lang(client, lang):
    with client.session_transaction() as s:
        s['lang'] = lang


def test_all_metadata_types_are_documented():
    assert DOCS == ['ontology', 'ontology_concepts', 'ontology_genres', 'ontology_hint_types',
                    'ontology_hints', 'ontology_methods', 'ontology_models', 'ontology_olympiads',
                    'ontology_question_types', 'ontology_topics']


@pytest.mark.parametrize('doc', DOCS)
@pytest.mark.parametrize('lang', LANGS)
def test_document_exists_and_has_no_stray_dollars(doc, lang):
    # A "$" would be taken as the start of a LaTeX formula by mathBeautify.
    assert '$' not in _text(doc, lang)


@pytest.mark.parametrize('doc', DOCS)
@pytest.mark.parametrize('lang', LANGS)
def test_sparql_examples_are_accepted(doc, lang):
    store = Store()
    for query in _sparql_examples(_text(doc, lang)):
        check_query(query)
        collect_rows(store, query, 10)


def test_languages_have_the_same_examples():
    # Translations change the comments and subtitles, not the query structure.
    for doc in DOCS:
        counts = {lang: len(_sparql_examples(_text(doc, lang))) for lang in LANGS}
        assert len(set(counts.values())) == 1, (doc, counts)


@pytest.mark.parametrize('lang', LANGS)
def test_pages_render_and_links_resolve(client, lang):
    _set_lang(client, lang)
    links = set()
    for doc in DOCS:
        response = client.get('/content/%s' % doc)
        assert response.status_code == 200
        links.update(LINK_RE.findall(_text(doc, lang)))
    # Documents and images are fetched; the browse pages (/topics, ...) need
    # the real problem base, so for them it is enough that the route exists.
    urls = client.application.url_map.bind('localhost')
    for link in sorted(links):
        if link.startswith('/content/'):
            assert client.get(link).status_code == 200, link
        else:
            urls.match(link.split('?')[0])


def test_subpage_breadcrumb_goes_through_ontology(client):
    html = client.get('/content/ontology_topics').get_data(as_text=True)
    assert 'href="/ontology"' in html


def test_ontology_page_shows_the_diagram(client):
    html = client.get('/ontology').get_data(as_text=True)
    assert 'src="/content/ontology/klasifikatoru_attiecibu_grafs.svg"' in html
    response = client.get('/content/ontology/klasifikatoru_attiecibu_grafs.svg')
    assert response.status_code == 200
    assert response.mimetype == 'image/svg+xml'


@pytest.mark.parametrize('path', [
    '/content/ontology/content_en.md',
    '/content/ontology/missing.svg',
    '/content/ontology/..%2F..%2F__init__.py',
    '/content/no_such_doc/klasifikatoru_attiecibu_grafs.svg',
])
def test_content_file_route_serves_only_existing_images(client, path):
    assert client.get(path).status_code == 404


def test_advanced_search_links_to_ontology(client):
    html = client.get('/advanced_search').get_data(as_text=True)
    assert 'class="ontology-help" href="/ontology"' in html
    assert 'blue_question_mark.png' in html
