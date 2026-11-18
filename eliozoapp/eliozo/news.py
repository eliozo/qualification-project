"""The news list on the main page, read from eliozo/data/news.yaml.

Every entry has a ``date`` and a one-line Markdown ``text`` (or a {lv, en, lt}
mapping of such lines). The file is re-read when it changes, so a news item
can be added without restarting the application.
"""

import datetime
import logging
import os
import threading

import markdown
import yaml
from markupsafe import Markup

logger = logging.getLogger(__name__)

NEWS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'news.yaml')

# News items per page on the main page.
NEWS_PAGE_SIZE = 10

_cache = {'mtime': None, 'items': []}
_lock = threading.Lock()


def _parse_date(value):
    if isinstance(value, datetime.datetime):
        return value.date()
    if isinstance(value, datetime.date):
        return value
    return datetime.date.fromisoformat(str(value).strip())


def _render_line(text):
    """One Markdown line -> inline HTML (without the enclosing <p>)."""
    html = markdown.markdown(str(text).strip())
    if html.startswith('<p>') and html.endswith('</p>'):
        html = html[3:-4]
    return Markup(html)


def parse_news(entries):
    """YAML entries -> [{'date': date, 'html': {lang: Markup}}], newest first.

    Entries without a valid date or text are skipped (and logged), so one typo
    in the hand-edited file does not hide the whole list.
    """
    items = []
    for n, entry in enumerate(entries or [], 1):
        try:
            date = _parse_date(entry['date'])
            text = entry['text']
            texts = text if isinstance(text, dict) else {'lv': text}
            html = {lang: _render_line(t) for lang, t in texts.items() if t}
            if not html:
                raise ValueError('empty text')
        except (KeyError, TypeError, ValueError) as e:
            logger.warning('%s: skipping news entry %d (%r): %s', NEWS_FILE, n, entry, e)
            continue
        items.append({'date': date, 'html': html})
    # Stable sort: items of the same date keep their order in the file.
    items.sort(key=lambda item: item['date'], reverse=True)
    return items


def load_news(path=NEWS_FILE):
    """All news items, newest first; re-read only when the file has changed."""
    try:
        mtime = os.path.getmtime(path)
    except OSError:
        return []
    with _lock:
        if _cache['mtime'] != (path, mtime):
            try:
                with open(path, encoding='utf-8') as f:
                    entries = yaml.safe_load(f)
                _cache['items'] = parse_news(entries if isinstance(entries, list) else [])
            except (OSError, yaml.YAMLError):
                logger.exception('Cannot read %s', path)
                _cache['items'] = []
            _cache['mtime'] = (path, mtime)
        return _cache['items']


def news_page(offset, lang, items=None, page_size=NEWS_PAGE_SIZE):
    """One page of news for the main page.

    Returns ``{'items': [{'date': 'YYYY-MM-DD', 'html': Markup}], 'newer': offset
    or None, 'older': offset or None}``; ``newer``/``older`` are the offsets of
    the neighbouring pages, None at either end.
    """
    items = load_news() if items is None else items
    if offset >= len(items):
        # Past the end (e.g. an old link after items were removed): last page.
        offset = max(0, (len(items) - 1) // page_size * page_size)
    page = items[offset:offset + page_size]
    return {
        'items': [{'date': item['date'].isoformat(),
                   'html': item['html'].get(lang) or item['html'].get('lv')
                           or next(iter(item['html'].values()))}
                  for item in page],
        'newer': max(0, offset - page_size) if offset > 0 else None,
        'older': offset + page_size if offset + page_size < len(items) else None,
    }
