"""Advanced search: a SPARQL query field, a result limit and a preset menu.

The presets come from the YAML files in ``eliozoapp/sparql_presets`` (see the
README there); they are read on every page load so that edits show up
without restarting the app.
"""

import glob
import logging
import os
import re

import yaml
from flask import Blueprint, render_template, request, session

from eliozo_dao.advanced_search_repository import (
    DEFAULT_LIMIT,
    MAX_LIMIT,
    QueryError,
    group_rows,
    parse_limit,
    run_query,
)

logger = logging.getLogger(__name__)

advanced_search_bp = Blueprint('advanced_search', __name__)

# Longer search URLs are sent as POST instead: uWSGI's default buffer for the
# request line and headers is 4096 bytes (see buffer-size in eliozo.ini).
MAX_GET_URL_LENGTH = 3500

# Preset labels, used in canned links: /advanced_search?queryLabel=pigeonhole
PRESET_LABEL_RE = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')

PRESETS_DIR = os.path.normpath(os.path.join(os.path.dirname(__file__), '..', '..', 'sparql_presets'))


def localized(title, lang):
    """A preset title: plain text, or the ``lang`` entry of a {lv, en, lt} mapping."""
    if not isinstance(title, dict):
        return str(title)
    for key in (lang, 'lv'):
        if title.get(key):
            return str(title[key])
    return str(next(iter(title.values()), ''))


def _menu_items(items, lang, queries, source):
    menu = []
    for item in items or []:
        if not isinstance(item, dict) or 'title' not in item:
            logger.warning('Skipping preset without a title in %s: %r', source, item)
            continue
        entry = {'title': localized(item['title'], lang)}
        if 'items' in item:
            entry['children'] = _menu_items(item['items'], lang, queries, source)
        elif isinstance(item.get('query'), str):
            entry['index'] = len(queries)
            queries.append(item['query'])
            label = item.get('label')
            if label is not None:
                if isinstance(label, str) and PRESET_LABEL_RE.fullmatch(label):
                    entry['label'] = label
                else:
                    logger.warning('Ignoring invalid preset label in %s: %r', source, label)
        else:
            logger.warning('Skipping preset without "query" or "items" in %s: %r', source, item)
            continue
        menu.append(entry)
    return menu


def load_presets(lang, presets_dir=PRESETS_DIR):
    """The preset menu in ``lang`` and the list of preset queries.

    Menu entries are {'title', 'children'} for submenus and {'title', 'index'}
    for queries, ``index`` pointing into the query list. A file that cannot
    be parsed is logged and left out, so a typo does not break the page.
    """
    queries = []
    menu = []
    for path in sorted(glob.glob(os.path.join(presets_dir, '*.yaml'))):
        try:
            with open(path, encoding='utf-8') as f:
                data = yaml.safe_load(f)
        except (OSError, yaml.YAMLError):
            logger.exception('Cannot read SPARQL presets from %s', path)
            continue
        if not isinstance(data, dict):
            logger.warning('Skipping %s: expected a mapping with "title" and "items"', path)
            continue
        title = data.get('title', os.path.splitext(os.path.basename(path))[0])
        menu.append({'title': localized(title, lang),
                     'children': _menu_items(data.get('items'), lang, queries, path)})
    return menu, queries


def preset_by_label(menu, queries, label):
    """The query of the preset with this label, or None. Labels are unique across
    all preset files; if one is repeated, the first one (in menu order) is used."""
    for entry in menu:
        if entry.get('label') == label:
            return queries[entry['index']]
        found = preset_by_label(entry.get('children', []), queries, label)
        if found is not None:
            return found
    return None


@advanced_search_bp.route('/advanced_search', methods=['GET', 'POST'])
def getAdvancedSearch():
    lang = session.get('lang', 'lv')
    menu, presetQueries = load_presets(lang)

    # The search is a GET form, so that results have a URL and the browser's
    # Back button returns to them without a "resubmit the form?" page. Only
    # queries too long for a URL are POSTed (the page's script decides).
    # Without a query parameter the page is the empty form.
    #
    # A canned link names a preset instead of carrying the query text:
    # /advanced_search?queryLabel=pigeonhole. The label takes precedence over
    # ?query; an unknown label shows an error and the empty form.
    form = request.form if request.method == 'POST' else request.args
    query = form.get('query', '')
    limitText = form.get('limit', str(DEFAULT_LIMIT))
    queryLabel = request.args.get('queryLabel', '').strip()

    sections = None
    truncated = False
    error = None
    limitError = False
    unknownLabel = False
    runQuery = 'query' in form
    if queryLabel:
        preset = preset_by_label(menu, presetQueries, queryLabel)
        if preset is None:
            unknownLabel = True
            query, runQuery = '', False
        else:
            query, runQuery = preset, True
    if runQuery:
        limit = parse_limit(limitText)
        if limit is None:
            limitError = True
        else:
            limitText = str(limit)
            try:
                rows, truncated = run_query(query, limit)
                sections = group_rows(rows)
            except QueryError as e:
                error = e

    template_context = {
        'active': 'main',
        'navlinks': [
            {'url':'advanced_search.getAdvancedSearch', 'title':'Advanced Search'},
        ],
        'title': 'SPARQL',
        'query': query,
        'limit': limitText,
        'maxLimit': MAX_LIMIT,
        'limitError': limitError,
        'error': error,
        'sections': sections,
        'resultCount': sum(len(sub['problemids']) for s in sections for sub in s['subsections'])
                       if sections else 0,
        'truncated': truncated,
        'presetMenu': menu,
        'presetQueries': presetQueries,
        'maxGetLength': MAX_GET_URL_LENGTH,
        'queryLabel': queryLabel if queryLabel and not unknownLabel else None,
        'unknownLabel': queryLabel if unknownLabel else None,
    }
    return render_template('advanced_search_content.html', **template_context)
