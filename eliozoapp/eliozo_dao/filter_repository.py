from . import sparql_query


def getProblemsByFiltersSPARQL(params, theOffset):
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemid ?text ?grade WHERE {{
  {extraClauses}
  ?problem eliozo:problemID ?problemid ;
           {grade}
           {olympiad}
           {domain}
           {questionType}
           {method}
           {solution}
           {video}
      eliozo:problemTextHtml ?text .

      {fGrade} {fOlympiad} {fDomain} {fQuestionType} {fMethod} {fSolution} {fVideo}

      OPTIONAL {{
        ?problem eliozo:problemGrade ?grade .
      }}
}} ORDER BY ?grade ?problemid LIMIT 10 OFFSET {offset}
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

    q = queryTemplate.format(grade=theGrade, olympiad=theOlympiad,
                             domain=theDomain, questionType=theQuestionType,
                             method=theMethod, offset=theOffset,
                             solution=theSolution, video=theVideo,
                             extraClauses=theExtraClauses,
                             fGrade=theFGrade, fOlympiad=theFOlympiad, fDomain=theFDomain,
                             fQuestionType=theFQuestionType, fMethod=theFMethod,
                             fSolution=theFSolution, fVideo=theFVideo)
    return sparql_query(q)


def getProblemCountsByFiltersSPARQL(params):
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT (COUNT(*) AS ?count) WHERE {{
  ?problem eliozo:problemID ?problemid ;
           {grade}
           {olympiad}
           {domain}
           {questionType}
           {method}
           {solution}
           {video} .
           {fGrade} {fOlympiad} {fDomain} {fQuestionType} {fMethod} {fSolution} {fVideo}
}}
"""
    theGrade = '' if params["grade"] in ["NA","-"] else f'eliozo:suggestedGrade {params["grade"]} ; '
    theOlympiad = '' if params["olympiad"] in ["NA","-"] else f'eliozo:olympiadType "{params["olympiad"]}" ; '
    theDomain = '' if params["domain"] in ["NA","-"] else f'eliozo:domain "{params["domain"]}" ; '
    theQuestionType = '' if params["questionType"] in ["NA","-"] else f'eliozo:questionType "{params["questionType"]}" ; '
    theMethod = '' if params["method"] in ["NA","-"] else f'eliozo:method ?mymethod . ?mymethod skos:broader* {params["method"]} ; '
    theSolution = "" if params["hasSolution"] in ["NA","-"] else f'eliozo:problemSolution ?someSolution ; '
    theVideo = "" if params["hasVideo"] in ["NA","-"] else f'eliozo:hasVideo ?someVideo ; '
    theFGrade = "" if params["grade"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:suggestedGrade ?gg . }"
    theFOlympiad = "" if params["olympiad"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:olympiadType ?oo . }"
    theFDomain = "" if params["domain"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:domain ?dd . }"
    theFQuestionType = "" if params["questionType"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:questionType ?qq . }"
    theFMethod = "" if params["method"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:method ?mm . }"
    theFSolution = "" if params["hasSolution"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:problemSolution ?ss . }"
    theFVideo = "" if params["hasVideo"] != "-" else "FILTER NOT EXISTS { ?problem eliozo:hasVideo ?vv . }"

    q = queryTemplate.format(grade=theGrade, olympiad=theOlympiad,
                             domain=theDomain, questionType=theQuestionType,
                             method=theMethod, solution=theSolution, video=theVideo,
                             fGrade=theFGrade, fOlympiad=theFOlympiad, fDomain=theFDomain,
                             fQuestionType=theFQuestionType, fMethod=theFMethod,
                             fSolution=theFSolution, fVideo=theFVideo)
    return sparql_query(q)
