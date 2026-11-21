"""The Advanced search page: a GET form, so that the browser's Back button returns to the results."""

from unittest import mock

import pytest

QUERY = 'SELECT ?problemID WHERE { ?p ?x ?problemID }'
ROW = {'problemid': 'LV.AMO.2011.5.1', 'section': None, 'subsection': None}


@pytest.fixture
def client():
    import eliozo
    return eliozo.create_app({'TESTING': True}).test_client()


def test_empty_form_runs_nothing(client):
    with mock.patch('blueprints.advanced_search.run_query') as run:
        html = client.get('/advanced_search').get_data(as_text=True)
    run.assert_not_called()
    assert 'method="get"' in html and 'class="btn btn-default new-query"' in html


@pytest.mark.parametrize('method', ['get', 'post'])   # long queries are POSTed
def test_query_runs_from_url_or_form(client, method):
    with mock.patch('blueprints.advanced_search.run_query', return_value=([ROW], False)) as run:
        if method == 'get':
            response = client.get('/advanced_search', query_string={'query': QUERY, 'limit': '5'})
        else:
            response = client.post('/advanced_search', data={'query': QUERY, 'limit': '5'})
    run.assert_called_once_with(QUERY, 5)
    assert '/problem/LV.AMO.2011.5.1' in response.get_data(as_text=True) or \
        'LV.AMO.2011.5.1' in response.get_data(as_text=True)


def test_query_label_runs_the_preset_and_takes_precedence(client):
    from blueprints.advanced_search import load_presets, preset_by_label
    menu, queries = load_presets('lv')
    pigeonhole = preset_by_label(menu, queries, 'pigeonhole')
    assert pigeonhole and 'MTH_PigeonholePrincipleBasic' in pigeonhole
    with mock.patch('blueprints.advanced_search.run_query', return_value=([ROW], False)) as run:
        html = client.get('/advanced_search',
                          query_string={'queryLabel': 'pigeonhole', 'query': QUERY}).get_data(as_text=True)
    run.assert_called_once_with(pigeonhole, 100)
    assert 'http://localhost/advanced_search?queryLabel=pigeonhole' in html   # the canned link
    assert 'MTH_PigeonholePrincipleBasic' in html                              # query in the text field


def test_unknown_query_label(client):
    with mock.patch('blueprints.advanced_search.run_query') as run:
        html = client.get('/advanced_search?queryLabel=no-such-preset').get_data(as_text=True)
    run.assert_not_called()
    assert 'no-such-preset' in html and 'alert-danger' in html


def _preset_items(items):
    """All query items of a preset file, including those in submenus."""
    for item in items:
        if 'items' in item:
            yield from _preset_items(item['items'])
        else:
            yield item


def _all_preset_items():
    import glob, os, yaml
    from blueprints.advanced_search import PRESETS_DIR
    for path in sorted(glob.glob(os.path.join(PRESETS_DIR, '*.yaml'))):
        with open(path, encoding='utf-8') as f:
            yield from _preset_items(yaml.safe_load(f)['items'])


def test_all_presets_have_unique_labels():
    from blueprints.advanced_search import PRESET_LABEL_RE
    labels = [item.get('label') for item in _all_preset_items() if 'query' in item]
    assert all(l and PRESET_LABEL_RE.fullmatch(l) for l in labels), labels
    assert len(labels) == len(set(labels))


def test_all_presets_are_accepted():
    # Parsed and run on an empty store only: results depend on the real problem base.
    from pyoxigraph import Store
    from eliozo_dao.advanced_search_repository import check_query, collect_rows
    store = Store()
    for item in _all_preset_items():
        check_query(item['query'])
        collect_rows(store, item['query'], 10)
