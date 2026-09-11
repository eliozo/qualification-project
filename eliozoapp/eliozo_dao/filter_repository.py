from . import sparql_query
from .problem_listing import SORT_KEY_PATTERN, SORT_KEY_VARIABLES


_PREFIXES = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
"""


def _filterPattern(params):
    """Graph pattern binding ?problem to the problems selected by ``params``.

    For every parameter "NA" means "not filtered" and "-" means "the property
    is absent". Shared by the problem list and the counts, so that the counts
    shown next to the filters always describe the listed problems.
    """
    theGrade = "" if params["grade"] in ["NA","-"] else f'eliozo:suggestedGrade {params["grade"]} ; '
    theOlympiad = "" if params["olympiad"] in ["NA","-"] else f'eliozo:olympiadType "{params["olympiad"]}" ; '
    theDomain = "" if params["domain"] in ["NA","-"] else f'eliozo:domain "{params["domain"]}" ; '
    theQuestionType = "" if params["questionType"] in ["NA","-"] else f'eliozo:questionType "{params["questionType"]}" ; '
    theMethod = "" if params["method"] in ["NA","-"] else f'eliozo:method ?mymethod ; '
    theSolution = "" if params["hasSolution"] in ["NA","-"] else f'eliozo:problemSolution ?someSolution ; '
    theVideo = "" if params["hasVideo"] in ["NA","-"] else f'eliozo:hasVideo ?someVideo ; '
    theExtraClauses = "" if params["method"] in ["NA", "-"] else f'?mymethod skos:broader* {params["method"]} . '

    theFGrade = "" if params["grade"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:suggestedGrade ?gg . }"
    theFOlympiad = "" if params["olympiad"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:olympiadType ?oo . }"
    theFDomain = "" if params["domain"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:domain ?dd . }"
    theFQuestionType = "" if params["questionType"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:questionType ?qq . }"
    theFMethod = "" if params["method"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:method ?mm . }"
    theFSolution = "" if params["hasSolution"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:problemSolution ?ss . }"
    theFVideo = "" if params["hasVideo"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:hasVideo ?vv . }"

    return """{extraClauses}
    ?problem {grade}{olympiad}{domain}{questionType}{method}{solution}{video}eliozo:problemID ?filteredID .
    {fGrade} {fOlympiad} {fDomain} {fQuestionType} {fMethod} {fSolution} {fVideo}""".format(
        grade=theGrade, olympiad=theOlympiad, domain=theDomain, questionType=theQuestionType,
        method=theMethod, solution=theSolution, video=theVideo, extraClauses=theExtraClauses,
        fGrade=theFGrade, fOlympiad=theFOlympiad, fDomain=theFDomain,
        fQuestionType=theFQuestionType, fMethod=theFMethod,
        fSolution=theFSolution, fVideo=theFVideo)


def getProblemsByFiltersSPARQL(params):
    """SPARQL JSON with one row per problem selected by the Filter page and its
    sort keys, unordered and unlimited: ``problem_listing.listProblemsPage``
    ranks and pages it."""
    q = _PREFIXES + """SELECT {variables} WHERE {{
    {{
        SELECT DISTINCT ?problem WHERE {{
            {pattern}
        }}
    }}
{sortKeys}
}}
""".format(variables=SORT_KEY_VARIABLES, pattern=_filterPattern(params), sortKeys=SORT_KEY_PATTERN)
    return sparql_query(q)


def getProblemCountsByFiltersSPARQL(params):
    """SPARQL JSON with ?count, the number of distinct problems selected by ``params``.

    Distinct, because a problem with several solutions or methods matches the
    pattern once per solution or method.
    """
    q = _PREFIXES + """SELECT (COUNT(DISTINCT ?problem) AS ?count) WHERE {{
    {pattern}
}}
""".format(pattern=_filterPattern(params))
    return sparql_query(q)
