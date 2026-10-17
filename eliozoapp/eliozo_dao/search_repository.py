import html
import json

from . import sparql_query
from .problem_listing import (
    PAGE_SIZE,
    SORT_KEY_PATTERN,
    SORT_KEY_VARIABLES,
    UNTAGGED,
    chooseTranslation,
    collectTranslation,
    listProblemsPage,
    preferredLanguage,
)


# Values of the "searchMode" radio buttons and the "search-target" select box
# in main_content.html.
SEARCH_MODE_EXACT = 'exact'
SEARCH_MODE_REGEX = 'regex'
SEARCH_MODE_SEMANTIC = 'semantic'
SEARCH_TARGET_PROBLEMS = 'questions'
SEARCH_TARGET_SOLUTIONS = 'solutions'


def replace_non_ascii_with_unicode_escape(text):
    non_ascii_characters = {'ā': '\\u0101', 'č': '\\u010D', 'ē': '\\u0113', 'ģ': '\\u0123', 'ī': '\\u012B',
                        'ķ': '\\u0137', 'ļ': '\\u013C', 'ņ': '\\u0146', 'š': '\\u0161', 'ū': '\\u016B',
                        'ž': '\\u017E'}
    replaced_text = ''
    for char in text:
        if char in non_ascii_characters:
            replaced_text += non_ascii_characters[char]
        else:
            replaced_text += char
    return replaced_text


def escape_sparql_literal(text):
    """Make ``text`` safe to paste between the double quotes of a SPARQL literal.

    Order matters. Backslashes are doubled first, so a LaTeX keyword such as
    ``\\sqrt`` or a regex such as ``\\\\frac`` survives the SPARQL string
    parser (it would otherwise choke on the unknown escape ``\\s``). Only then
    are quotes and control characters escaped, and only as the last step are
    Latvian diacritics turned into ``\\uXXXX`` escapes -- doing that earlier
    would get their backslashes doubled as well.
    """
    text = text.replace('\\', '\\\\')
    text = text.replace('"', '\\"')
    text = text.replace('\n', '\\n').replace('\r', '\\r').replace('\t', '\\t')
    return replace_non_ascii_with_unicode_escape(text)


def keywordMatcher(thePattern, isCaseSensitive):
    """Callable turning a SPARQL variable into a substring match expression.

    ``thePattern`` is taken literally, not as a regex.
    """
    if not isCaseSensitive:
        escapedPattern = escape_sparql_literal(thePattern.lower())
        return lambda var: 'contains(lcase(%s), "%s")' % (var, escapedPattern)
    escapedPattern = escape_sparql_literal(thePattern)
    return lambda var: 'contains(%s, "%s")' % (var, escapedPattern)


def regexMatcher(thePattern, isCaseSensitive):
    """Callable turning a SPARQL variable into a regex match expression.

    The regex flavour is XPath/XQuery, as required by SPARQL 1.1. Case
    insensitivity uses the regex ``i`` flag rather than lowercasing the
    pattern: lowercasing would silently corrupt character classes such as
    ``\\S`` or ``[A-Z]``.
    """
    escapedPattern = escape_sparql_literal(thePattern)
    flags = '' if isCaseSensitive else ', "i"'
    return lambda var: 'regex(%s, "%s"%s)' % (var, escapedPattern, flags)


def _buildMatchQuery(buildMatch, searchTarget):
    """SPARQL query for the set of matching problems and their sort keys.

    ``buildMatch`` is a callable that takes a SPARQL variable name and returns
    a boolean expression matching that variable.

    The inner ``SELECT DISTINCT ?problem`` yields every matching problem once,
    however many of its translations or solutions matched. No texts are
    selected here: they are loaded for the shown page only.

    With ``searchTarget == 'solutions'`` the problem texts and the solution
    texts are matched in a UNION. That lets the engine run the match once per
    stored literal; the equivalent ``FILTER (... || EXISTS {...})`` re-ran the
    sub-pattern per candidate problem and measured 6.7s against 0.1s on the
    full problem base.
    """
    if searchTarget == SEARCH_TARGET_SOLUTIONS:
        matchExpr = buildMatch('?matched')
        matching = """{{ ?problem eliozo:problemText ?matched .
              FILTER ({matchExpr}) }}
            UNION
            {{ ?solution eliozo:solutionText ?matched .
              FILTER ({matchExpr}) .
              ?problem eliozo:problemSolution ?solution . }}""".format(matchExpr=matchExpr)
    else:
        matching = """?problem eliozo:problemText ?text .
            FILTER ({matchExpr})""".format(matchExpr=buildMatch('?text'))

    return """PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT {variables}
WHERE {{
    {{
        SELECT DISTINCT ?problem WHERE {{
            {matching}
        }}
    }}
{sortKeys}
}}
""".format(variables=SORT_KEY_VARIABLES, matching=matching, sortKeys=SORT_KEY_PATTERN)


def getProblemsByKeywordSPARQL(thePattern, isCaseSensitive, searchTarget=SEARCH_TARGET_PROBLEMS):
    """Substring search: SPARQL JSON with one row per matching problem and its
    sort keys, unordered and unlimited. ``searchProblems`` ranks and pages it."""
    return sparql_query(_buildMatchQuery(keywordMatcher(thePattern, isCaseSensitive), searchTarget))


def getProblemsByRegexSPARQL(thePattern, isCaseSensitive, searchTarget=SEARCH_TARGET_PROBLEMS):
    """Regex search; returns the same row shape as ``getProblemsByKeywordSPARQL``."""
    return sparql_query(_buildMatchQuery(regexMatcher(thePattern, isCaseSensitive), searchTarget))


def getMatchLocationsSPARQL(buildMatch, searchTarget, problemIris):
    """SPARQL JSON rows (?problem ?kind ?lang) telling where each given problem matched.

    ?kind is "problem" for a problem text and "solution" for a solution text;
    solution texts are looked at only when ``searchTarget`` is 'solutions'.
    """
    values = ' '.join('<%s>' % iri for iri in problemIris)
    matchExpr = buildMatch('?matched')
    branches = """{{ ?problem eliozo:problemText ?matched .
      FILTER ({matchExpr})
      BIND ("problem" AS ?kind) }}""".format(matchExpr=matchExpr)
    if searchTarget == SEARCH_TARGET_SOLUTIONS:
        branches += """
    UNION
    {{ ?problem eliozo:problemSolution ?solution .
      ?solution eliozo:solutionText ?matched .
      FILTER ({matchExpr})
      BIND ("solution" AS ?kind) }}""".format(matchExpr=matchExpr)
    return sparql_query("""PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problem ?kind ?lang
WHERE {{
    VALUES ?problem {{ {values} }}
    {branches}
    BIND (LANG(?matched) AS ?lang)
}}
""".format(values=values, branches=branches))


def searchProblems(pattern, searchMode, searchTarget=SEARCH_TARGET_PROBLEMS, uiLang=None,
                   offset=0, pageSize=None, isCaseSensitive=False):
    """One page of search results, each problem at most once.

    Returns the dict of ``problem_listing.listProblemsPage``. Every problem
    also tells where the match is when the shown text does not contain it:

      'matchLang'          a translation whose statement matches (the
                           precedence rules pick one if several do), else None
      'solutionMatchLang'  the language of a matching solution (picked the
                           same way), else None

    Both are None when the shown translation itself matches.
    """
    if searchMode == SEARCH_MODE_REGEX:
        matcher = regexMatcher(pattern, isCaseSensitive)
    else:
        matcher = keywordMatcher(pattern, isCaseSensitive)

    result = listProblemsPage(sparql_query(_buildMatchQuery(matcher, searchTarget)),
                              uiLang, offset, pageSize)
    page = result['problems']
    for p in page:
        p['matchLang'] = None
        p['solutionMatchLang'] = None
    if not page:
        return result

    found = {p['problem']: {'problem': set(), 'solution': set()} for p in page}
    raw = getMatchLocationsSPARQL(matcher, searchTarget, list(found))
    for row in json.loads(raw)['results']['bindings']:
        found[row['problem']['value']][row['kind']['value']].add(row['lang']['value'] or UNTAGGED)

    for p in page:
        where = found[p['problem']]
        if p['lang'] in where['problem']:
            continue
        # Only point at translations the problem page can actually show.
        p['matchLang'] = preferredLanguage(where['problem'] & set(p['translations']), uiLang)
        p['solutionMatchLang'] = preferredLanguage(where['solution'], uiLang)
    return result


def getProblemTranslationsByIdSPARQL(problemIds):
    """SPARQL JSON with every (problemid, problemTextHtml) pair of the given problem IDs."""
    values = ' '.join('"%s"' % escape_sparql_literal(pid) for pid in problemIds)
    return sparql_query("""PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemid ?textHtml
WHERE {{
    VALUES ?problemid {{ {values} }}
    ?problem eliozo:problemID ?problemid ;
             eliozo:problemTextHtml ?textHtml .
}}
""".format(values=values))


def semanticSearchProblems(queryText, searchTarget=SEARCH_TARGET_PROBLEMS, uiLang=None,
                           offset=0, pageSize=None):
    """One page of search-by-meaning results, closest first.

    The nearest problems come from PostgreSQL (``eliozo_dao.postgres``); the
    texts shown are the HTML translations from the RDF store, chosen as on the
    other result lists. Returns the same dict as ``searchProblems``; here
    'solutionMatchLang' is set when a solution text is closer to the query
    than the problem statement, and 'matchLang' is always None.

    Raises if PostgreSQL or the embedding API is unavailable.
    """
    # Imported here so that the other search modes work without the
    # PostgreSQL / OpenAI libraries installed.
    from .postgres.semantic_search import semanticSearch

    pageSize = PAGE_SIZE if pageSize is None else pageSize
    offset = max(0, offset)
    hits = semanticSearch(queryText, includeSolutions=(searchTarget == SEARCH_TARGET_SOLUTIONS))
    page = hits[offset:offset + pageSize]

    translations = {hit['problemid']: {} for hit in page}
    if page:
        for row in json.loads(getProblemTranslationsByIdSPARQL(list(translations)))['results']['bindings']:
            collectTranslation(translations[row['problemid']['value']],
                               row['textHtml'].get('xml:lang', UNTAGGED), row['textHtml']['value'])

    problems = []
    for hit in page:
        texts = translations[hit['problemid']]
        lang = chooseTranslation(texts, uiLang)
        if lang is None:
            # Not (or no longer) in the RDF store: show the stored Markdown as is.
            lang = hit['contentLang']
            textHtml = '<p>%s</p>' % html.escape(hit['content'])
        else:
            textHtml = texts[lang]
        solutionMatchLang = None
        if hit['inSolution']:
            solutionMatchLang = hit['solutionLang'] if hit['solutionLang'] not in (None, UNTAGGED) else lang
        problems.append({'problemid': hit['problemid'], 'lang': lang, 'textHtml': textHtml,
                         'distance': hit['distance'], 'matchLang': None,
                         'solutionMatchLang': solutionMatchLang})
    return {'total': len(hits), 'offset': offset, 'pageSize': pageSize, 'problems': problems}
