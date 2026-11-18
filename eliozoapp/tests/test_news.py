"""The news list on the main page (eliozo/data/news.yaml)."""

import datetime
import re

import pytest

from eliozo.news import load_news, news_page, parse_news


@pytest.fixture
def client():
    import eliozo
    return eliozo.create_app({'TESTING': True}).test_client()


def _items(n):
    """n items, one per day, given oldest first."""
    start = datetime.date(2026, 1, 1)
    return parse_news([{'date': start + datetime.timedelta(days=i), 'text': 'item %d' % i}
                       for i in range(n)])


def test_the_news_file_is_valid():
    items = load_news()
    assert items, 'eliozo/data/news.yaml has no valid entries'
    assert all(a['date'] >= b['date'] for a, b in zip(items, items[1:]))


def test_markdown_line_and_languages():
    [item] = parse_news([{'date': '2026-11-18',
                          'text': {'lv': 'Skat. [šeit](/advanced_search?queryLabel=weighing)',
                                   'en': 'See *here*'}}])
    assert item['html']['lv'] == 'Skat. <a href="/advanced_search?queryLabel=weighing">šeit</a>'
    page = news_page(0, 'lt', [item])            # no Lithuanian text: Latvian
    assert page['items'][0]['html'] == item['html']['lv']
    assert news_page(0, 'en', [item])['items'][0]['html'] == 'See <em>here</em>'


def test_invalid_entries_are_skipped():
    items = parse_news([{'date': 'yesterday', 'text': 'x'}, {'text': 'no date'},
                        {'date': '2026-01-02'}, 'junk', {'date': '2026-01-01', 'text': 'ok'}])
    assert [i['date'].isoformat() for i in items] == ['2026-01-01']


def test_paging_newest_first():
    items = _items(23)
    first = news_page(0, 'lv', items)
    assert len(first['items']) == 10
    assert first['items'][0]['date'] == '2026-01-23'
    assert (first['newer'], first['older']) == (None, 10)
    middle = news_page(10, 'lv', items)
    assert middle['items'][0]['date'] == '2026-01-13'
    assert (middle['newer'], middle['older']) == (0, 20)
    last = news_page(20, 'lv', items)
    assert [i['date'] for i in last['items']] == ['2026-01-03', '2026-01-02', '2026-01-01']
    assert (last['newer'], last['older']) == (10, None)
    assert news_page(999, 'lv', items)['items'] == last['items']   # past the end
    assert news_page(0, 'lv', _items(10))['older'] is None


def test_main_page_shows_the_news(client):
    html = client.get('/').get_data(as_text=True)
    assert '<dl class="news-list">' in html
    assert re.search(r'<time datetime="2026-11-18">2026-11-18</time>', html)
    assert 'href="/advanced_search?queryLabel=weighing"' in html


def test_search_results_page_has_no_news(client):
    html = client.get('/?keyword=trijst%C5%ABr&searchMode=exact').get_data(as_text=True)
    assert 'news-list' not in html
