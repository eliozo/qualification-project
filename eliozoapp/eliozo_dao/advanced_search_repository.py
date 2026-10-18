"""Advanced search: run a user-written SPARQL SELECT query and list problem IDs.

The query comes straight from a web form, so it is treated as untrusted:

1. ``check_query`` rejects it before it reaches the store when it is empty,
   too long, not a SELECT query, or uses SERVICE (which would make the server
   send HTTP requests to any address in the query).
2. ``run_query`` executes it in a separate Python process that opens the
   store read-only and is killed after ``QUERY_TIMEOUT_SECONDS``, so a query
   that never ends (a cartesian product, say) cannot hang a web worker.
   The process returns at most ``limit`` result rows, and ``limit`` itself is
   capped at ``MAX_LIMIT``.

Naming convention for the query's result variables (case-insensitive):

    ?problemID    required; the problem IDs to show, e.g. "LV.AMO.2011.5.1"
    ?section      optional; problems are listed under one subtitle per value
    ?subsection   optional; a second level of subtitles inside a section

Rows are kept in the query's own order (ORDER BY), and sections appear in
the order of their first row.

The worker process is this module run as ``python -m``; it reads the query
as JSON from stdin and writes the result as JSON to stdout.
"""

import json
import os
import re
import subprocess
import sys

DEFAULT_LIMIT = 20
MAX_LIMIT = 100
MAX_QUERY_LENGTH = 20000
QUERY_TIMEOUT_SECONDS = 10

PROBLEM_ID_VARIABLE = 'problemid'
SECTION_VARIABLE = 'section'
SUBSECTION_VARIABLE = 'subsection'

_APP_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), '..'))

# Comments, string literals and IRIs are skipped when looking for keywords,
# so "# no SERVICE here" or "service" inside a string do not count. Prefixed
# names (eliozo:method) and variables (?select) are matched as whole tokens
# for the same reason.
_TOKEN_PATTERN = re.compile(r'''
      (?P<comment>\#[^\n]*)
    | (?P<string>"""(?:[^"\\]|\\.|"(?!""))*"""|'\'\'(?:[^'\\]|\\.|'(?!''))*'\'\'
                |"(?:[^"\\\n]|\\.)*"|'(?:[^'\\\n]|\\.)*')
    | (?P<iri><[^<>"{}|^`\\\s]*>)
    | (?P<variable>[?$]\w+)
    | (?P<prefixed>[A-Za-z_][\w.-]*:[\w.:%-]*|:[\w.:%-]*)
    | (?P<word>[A-Za-z_]\w*)
''', re.VERBOSE)

_QUERY_FORMS = {'SELECT', 'ASK', 'CONSTRUCT', 'DESCRIBE'}
_UPDATE_KEYWORDS = {'INSERT', 'DELETE', 'LOAD', 'CLEAR', 'DROP', 'CREATE',
                    'ADD', 'MOVE', 'COPY', 'WITH'}

_SYNTAX_ERROR_PATTERN = re.compile(r'^error at (\d+):(\d+): (.*)$', re.DOTALL)


class QueryError(Exception):
    """A query that is refused or fails. ``kind`` tells which message to show.

    kind: 'empty', 'too_long', 'not_select', 'update', 'service', 'syntax',
          'no_problem_id', 'timeout', 'failed'
    For 'syntax' errors ``line`` and ``column`` (1-based) locate the error and
    ``line_text`` is that line of the query.
    """

    def __init__(self, kind, message='', line=None, column=None, line_text=None):
        super().__init__(message or kind)
        self.kind = kind
        self.message = message
        self.line = line
        self.column = column
        self.line_text = line_text


def parse_limit(value):
    """The result limit from a form field: an integer between 1 and MAX_LIMIT.

    Returns None when ``value`` is not a positive integer; values above the
    cap are lowered to MAX_LIMIT.
    """
    if value is None or str(value).strip() == '':
        return DEFAULT_LIMIT
    text = str(value).strip()
    if not text.isdigit() or int(text) < 1:
        return None
    return min(int(text), MAX_LIMIT)


def keywords(query):
    """The upper-cased bare words of ``query``, outside comments, strings and IRIs."""
    return [m.group('word').upper() for m in _TOKEN_PATTERN.finditer(query)
            if m.lastgroup == 'word']


def check_query(query):
    """Raise QueryError when ``query`` must not be run; return None otherwise."""
    if query is None or not query.strip():
        raise QueryError('empty')
    if len(query) > MAX_QUERY_LENGTH:
        raise QueryError('too_long')
    words = keywords(query)
    if 'SERVICE' in words:
        raise QueryError('service')
    first = next((w for w in words if w in _QUERY_FORMS or w in _UPDATE_KEYWORDS), None)
    if first in _UPDATE_KEYWORDS:
        raise QueryError('update')
    if first != 'SELECT':
        raise QueryError('not_select')


def _term_text(term):
    """A result value as plain text; IRIs are shortened to their local name."""
    if term is None:
        return None
    if type(term).__name__ == 'NamedNode':
        return term.value.rsplit('#', 1)[-1].rsplit('/', 1)[-1]
    return term.value or None


def collect_rows(store, query, limit):
    """Run ``query`` on ``store``; return (rows, truncated).

    Each row is a dict with 'problemid', 'section' and 'subsection' (the
    latter two None when the query does not select them). Rows without a
    problem ID and repeated rows are skipped; at most ``limit`` rows are
    returned and ``truncated`` tells whether the query had more.
    Raises QueryError for syntax errors and queries without ?problemID.
    """
    try:
        solutions = store.query(query)
    except SyntaxError as e:
        raise _syntax_error(query, str(e))
    if not hasattr(solutions, 'variables'):
        raise QueryError('not_select')

    names = {v.value.lower(): v.value for v in solutions.variables}
    if PROBLEM_ID_VARIABLE not in names:
        raise QueryError('no_problem_id')
    problemVar = names[PROBLEM_ID_VARIABLE]
    sectionVar = names.get(SECTION_VARIABLE)
    subsectionVar = names.get(SUBSECTION_VARIABLE)

    rows = []
    seen = set()
    for solution in solutions:
        problemid = _term_text(solution[problemVar])
        if not problemid:
            continue
        section = _term_text(solution[sectionVar]) if sectionVar else None
        subsection = _term_text(solution[subsectionVar]) if subsectionVar else None
        key = (section, subsection, problemid)
        if key in seen:
            continue
        if len(rows) == limit:
            return rows, True
        seen.add(key)
        rows.append({'problemid': problemid, 'section': section, 'subsection': subsection})
    return rows, False


def _syntax_error(query, message):
    match = _SYNTAX_ERROR_PATTERN.match(message)
    if not match:
        return QueryError('syntax', message)
    line, column = int(match.group(1)), int(match.group(2))
    lines = query.split('\n')
    lineText = lines[line - 1].rstrip('\r') if 0 < line <= len(lines) else ''
    return QueryError('syntax', match.group(3), line=line, column=column, line_text=lineText)


def _python_executable():
    """The Python interpreter for the worker process.

    Under uWSGI ``sys.executable`` is the uwsgi binary, so the interpreter of
    the app's environment (``sys.prefix``) is looked up instead.
    """
    if os.path.basename(sys.executable or '').lower().startswith('python'):
        return sys.executable
    for name in (os.path.join('bin', 'python3'), os.path.join('bin', 'python'),
                 os.path.join('Scripts', 'python.exe'), 'python.exe'):
        candidate = os.path.join(sys.prefix, name)
        if os.path.isfile(candidate):
            return candidate
    return sys.executable


def run_query(query, limit, db_path=None, timeout=QUERY_TIMEOUT_SECONDS):
    """Check ``query`` and run it in a worker process; return (rows, truncated).

    See ``collect_rows`` for the rows. Raises QueryError.
    """
    check_query(query)
    limit = max(1, min(int(limit), MAX_LIMIT))
    if db_path is None:
        from . import OXIGRAPH_DB_PATH
        db_path = OXIGRAPH_DB_PATH
    request = json.dumps({'query': query, 'limit': limit, 'db_path': db_path})
    try:
        completed = subprocess.run(
            [_python_executable(), '-m', 'eliozo_dao.advanced_search_repository'],
            input=request, capture_output=True, text=True, encoding='utf-8',
            cwd=_APP_ROOT, timeout=timeout)
    except subprocess.TimeoutExpired:
        raise QueryError('timeout')
    try:
        reply = json.loads(completed.stdout)
    except ValueError:
        # The worker crashed; its last stderr line is usually the exception.
        lastLines = completed.stderr.strip().splitlines()[-1:]
        raise QueryError('failed', lastLines[0] if lastLines else '')
    if 'error' in reply:
        e = reply['error']
        raise QueryError(e['kind'], e.get('message', ''), e.get('line'), e.get('column'),
                         e.get('line_text'))
    return reply['rows'], reply['truncated']


def group_rows(rows):
    """Rows grouped for display: a list of sections in first-seen order.

    Each section is {'title': ..., 'subsections': [{'title': ..., 'problemids': [...]}]}.
    Titles are None for rows without ?section / ?subsection; when no row has
    a section the result is one untitled section.
    """
    sections = []
    byTitle = {}
    for row in rows:
        section = byTitle.get(row['section'])
        if section is None:
            section = {'title': row['section'], 'subsections': [], '_byTitle': {}}
            byTitle[row['section']] = section
            sections.append(section)
        sub = section['_byTitle'].get(row['subsection'])
        if sub is None:
            sub = {'title': row['subsection'], 'problemids': []}
            section['_byTitle'][row['subsection']] = sub
            section['subsections'].append(sub)
        sub['problemids'].append(row['problemid'])
    for section in sections:
        del section['_byTitle']
    return sections


def _worker():
    """Entry point of the worker process: JSON request on stdin, reply on stdout."""
    from pyoxigraph import Store

    request = json.loads(sys.stdin.read())
    try:
        store = Store.read_only(request['db_path'])
        rows, truncated = collect_rows(store, request['query'], request['limit'])
        reply = {'rows': rows, 'truncated': truncated}
    except QueryError as e:
        reply = {'error': {'kind': e.kind, 'message': e.message, 'line': e.line,
                           'column': e.column, 'line_text': e.line_text}}
    except Exception as e:  # evaluation errors, e.g. an invalid regex
        reply = {'error': {'kind': 'failed', 'message': str(e)}}
    sys.stdout.write(json.dumps(reply))


if __name__ == '__main__':
    _worker()
