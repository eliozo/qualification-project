"""How lists of problems are presented: ranking, translation choice, paging.

Shared by the search results, the Filter page and the problem pages. The
settings block below is the single place to change that behaviour.
"""

import json
import re

from . import sparql_query


# ---------------------------------------------------------------------------
# Settings
# ---------------------------------------------------------------------------

# Problems per result page (search results and the Filter page).
PAGE_SIZE = 10

# With more result pages than this, the page bar shows the first and the last
# page and a few pages around the current one instead of every page number.
PAGE_BAR_LIMIT = 30

# Ranking of search results and Filter results, most significant criterion
# first. Each entry is (criterion, 'asc' or 'desc'). The criteria are:
#
#   'grade'      eliozo:problemGrade, 5 .. 12
#   'year'       eliozo:problemYear
#   'country'    eliozo:country: EE, LT, LV, ...
#   'olympiad'   the second segment of the problem ID: AMO in LV.AMO.2011.10.1
#   'problemid'  the whole problem ID, with its numbers compared as numbers,
#                so LV.AMO.2011.10.2 comes before LV.AMO.2011.10.10
#
# A problem without a value for a criterion (books and shortlists have no
# grade, year or country) is placed after all problems that have one, in both
# directions. Keep 'problemid' as the last entry: it makes the order total, so
# that consecutive pages never repeat or skip a problem.
SEARCH_RESULT_ORDER = [
    ('grade', 'asc'),
    ('year', 'desc'),
    ('country', 'asc'),
    ('olympiad', 'asc'),
    ('problemid', 'asc'),
]

# Which translation of a problem or a solution is shown:
#   1. the UI language, if it is one of UI_LANGUAGES and the text exists in it;
#   2. otherwise FALLBACK_LANGUAGE, if the text exists in it;
#   3. otherwise the alphabetically first language code the text exists in.
# Empty placeholder texts do not count as translations.
UI_LANGUAGES = ('en', 'lt', 'lv')
FALLBACK_LANGUAGE = 'en'

# Language key for a text without a language tag; chosen only as a last resort.
UNTAGGED = 'unk'


# ---------------------------------------------------------------------------
# Translations
# ---------------------------------------------------------------------------

def preferredLanguage(langs, uiLang):
    """The language picked from ``langs`` by the precedence rules, or None."""
    langs = set(langs)
    if not langs:
        return None
    if uiLang in UI_LANGUAGES and uiLang in langs:
        return uiLang
    if FALLBACK_LANGUAGE in langs:
        return FALLBACK_LANGUAGE
    return min(langs, key=lambda lang: (lang == UNTAGGED, lang))


def collectTranslation(translations, lang, text):
    """Add one text to ``translations`` ({lang: text}).

    Blank texts are skipped: untranslated problems carry empty placeholders in
    some languages. Of two texts in the same language the smaller one is kept,
    so that the choice does not depend on the order the store returns them in.
    """
    if not text or not text.strip():
        return
    if lang not in translations or text < translations[lang]:
        translations[lang] = text


def chooseTranslation(translations, uiLang, requested=None):
    """The language to show from ``translations`` ({lang: text}), or None.

    ``requested`` (e.g. a ``lang`` URL parameter) wins when that translation
    exists; otherwise the precedence rules decide.
    """
    if requested is not None and requested in translations:
        return requested
    return preferredLanguage(translations, uiLang)


def getProblemTranslationsSPARQL(problemIris):
    """SPARQL JSON with every (problem, problemTextHtml) pair of the given problems."""
    values = ' '.join('<%s>' % iri for iri in problemIris)
    return sparql_query("""PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problem ?textHtml
WHERE {{
    VALUES ?problem {{ {values} }}
    ?problem eliozo:problemTextHtml ?textHtml .
}}
""".format(values=values))


# ---------------------------------------------------------------------------
# Ranking
# ---------------------------------------------------------------------------

# Variables and graph pattern that the queries selecting problems for a result
# list end with: ?problem must be bound by the query's own pattern before.
SORT_KEY_VARIABLES = '?problem ?problemid ?grade ?year ?country'
SORT_KEY_PATTERN = """    ?problem eliozo:problemID ?problemid .
    OPTIONAL { ?problem eliozo:problemGrade ?grade . }
    OPTIONAL { ?problem eliozo:problemYear ?year . }
    OPTIONAL { ?problem eliozo:country ?country . }"""


def _intOrNone(binding):
    if binding is None:
        return None
    try:
        return int(binding['value'])
    except ValueError:
        return None


def _naturalKey(text):
    """Sort key comparing the digit runs of ``text`` as numbers."""
    return tuple((0, int(part), '') if part.isdigit() else (1, 0, part)
                 for part in re.split(r'(\d+)', text) if part)


def _olympiadOf(problemid):
    parts = problemid.split('.')
    return parts[1] if len(parts) > 1 else None


_SORT_VALUES = {
    'grade': lambda p: p['grade'],
    'year': lambda p: p['year'],
    'country': lambda p: p['country'],
    'olympiad': lambda p: p['olympiad'],
    'problemid': lambda p: _naturalKey(p['problemid']),
}


def rankProblems(problems, order=None):
    """Return ``problems`` sorted by ``order`` (default: SEARCH_RESULT_ORDER)."""
    order = SEARCH_RESULT_ORDER if order is None else order
    ranked = list(problems)
    # Python's sort is stable, so sorting by each criterion in turn, from the
    # least to the most significant, yields the combined order.
    for criterion, direction in reversed(order):
        if criterion not in _SORT_VALUES or direction not in ('asc', 'desc'):
            raise ValueError('bad SEARCH_RESULT_ORDER entry: %r' % ((criterion, direction),))
        value = _SORT_VALUES[criterion]
        if direction == 'asc':
            ranked.sort(key=lambda p: (value(p) is None, value(p) if value(p) is not None else 0))
        else:
            # Reversed, so "has a value" must be the larger flag to stay first.
            ranked.sort(key=lambda p: (value(p) is not None, value(p) if value(p) is not None else 0),
                        reverse=True)
    return ranked


# ---------------------------------------------------------------------------
# Paged result lists
# ---------------------------------------------------------------------------

def listProblemsPage(raw, uiLang, offset=0, pageSize=None):
    """One page of a problem list, each problem at most once.

    ``raw`` is SPARQL JSON whose rows carry SORT_KEY_VARIABLES. The rows are
    deduplicated by problem, ranked by SEARCH_RESULT_ORDER and sliced; the
    translations are loaded for the page only. Returns::

        {'total': number of problems,
         'offset': offset of this page,
         'pageSize': page size,
         'problems': [{'problem' (IRI), 'problemid', 'grade', 'year', 'country',
                       'olympiad', 'translations' ({lang: textHtml}),
                       'lang' (the shown one), 'textHtml'}, ...]}
    """
    pageSize = PAGE_SIZE if pageSize is None else pageSize
    offset = max(0, offset)

    problems = {}
    for row in json.loads(raw)['results']['bindings']:
        iri = row['problem']['value']
        if iri in problems:
            continue
        problemid = row['problemid']['value']
        problems[iri] = {
            'problem': iri,
            'problemid': problemid,
            'grade': _intOrNone(row.get('grade')),
            'year': _intOrNone(row.get('year')),
            'country': row['country']['value'] if 'country' in row else None,
            'olympiad': _olympiadOf(problemid),
        }

    ranked = rankProblems(problems.values())
    page = ranked[offset:offset + pageSize]

    for p in page:
        p['translations'] = {}
    if page:
        byIri = {p['problem']: p for p in page}
        rows = json.loads(getProblemTranslationsSPARQL(list(byIri)))['results']['bindings']
        for row in rows:
            collectTranslation(byIri[row['problem']['value']]['translations'],
                               row['textHtml'].get('xml:lang', UNTAGGED),
                               row['textHtml']['value'])
    for p in page:
        p['lang'] = chooseTranslation(p['translations'], uiLang)
        p['textHtml'] = p['translations'].get(p['lang'], '')

    return {'total': len(ranked), 'offset': offset, 'pageSize': pageSize, 'problems': page}
