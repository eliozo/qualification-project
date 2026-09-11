from . import sparql_query


# Values of the "search-target" select box in main_content.html.
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


def _buildSearchQuery(buildMatch, searchTarget):
    """Assemble the SPARQL query shared by keyword and regex search.

    ``buildMatch`` is a callable that takes a SPARQL variable name and returns
    a boolean expression matching that variable.

    With ``searchTarget == 'questions'`` the expression is a plain FILTER on
    the problem text. With ``'solutions'`` the problem text and the solution
    texts are matched in a UNION and the problem is then joined back in, so a
    problem is returned when either its own text or any of its solutions
    matches. The UNION lets the engine run the match once per stored literal;
    the equivalent ``FILTER (... || EXISTS {...})`` re-ran the sub-pattern per
    candidate problem and measured 6.7s against 0.1s on the full problem base.
    """
    if searchTarget == SEARCH_TARGET_SOLUTIONS:
        matchExpr = buildMatch('?matched')
        selective = """    {{
        {{ ?problem eliozo:problemText ?matched .
           FILTER ({matchExpr}) }}
        UNION
        {{ ?solution eliozo:solutionText ?matched .
           FILTER ({matchExpr}) .
           ?problem eliozo:problemSolution ?solution . }}
    }}
""".format(matchExpr=matchExpr)
        filterTail = ''
    else:
        selective = ''
        filterTail = '    FILTER ({matchExpr})\n'.format(matchExpr=buildMatch('?text'))

    return """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT DISTINCT ?problem ?problemid ?text ?textHtml ?grade
WHERE {{
{selective}    ?problem eliozo:problemID ?problemid ;
    eliozo:problemText ?text ;
    eliozo:problemTextHtml ?textHtml .
    OPTIONAL {{
        ?problem eliozo:problemGrade ?grade .
    }}
{filterTail}}} ORDER BY ?grade ?problemid
LIMIT 10
""".format(selective=selective, filterTail=filterTail)


def getProblemsByKeywordSPARQL(thePattern, isCaseSensitive, searchTarget=SEARCH_TARGET_PROBLEMS):
    """Substring search. ``thePattern`` is taken literally, not as a regex."""
    if not isCaseSensitive:
        escapedPattern = escape_sparql_literal(thePattern.lower())
        def buildMatch(var):
            return 'contains(lcase(%s), "%s")' % (var, escapedPattern)
    else:
        escapedPattern = escape_sparql_literal(thePattern)
        def buildMatch(var):
            return 'contains(%s, "%s")' % (var, escapedPattern)
    return sparql_query(_buildSearchQuery(buildMatch, searchTarget))


def getProblemsByRegexSPARQL(thePattern, isCaseSensitive, searchTarget=SEARCH_TARGET_PROBLEMS):
    """Regex search (XPath/XQuery regex flavour, as required by SPARQL 1.1).

    Case insensitivity uses the regex ``i`` flag rather than lowercasing the
    pattern: lowercasing would silently corrupt character classes such as
    ``\\S`` or ``[A-Z]``.
    """
    escapedPattern = escape_sparql_literal(thePattern)
    flags = '' if isCaseSensitive else ', "i"'

    def buildMatch(var):
        return 'regex(%s, "%s"%s)' % (var, escapedPattern, flags)

    return sparql_query(_buildSearchQuery(buildMatch, searchTarget))
