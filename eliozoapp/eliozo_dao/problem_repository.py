from . import sparql_query


def getSPARQLOlympiads(lang):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?olympiadCountry ?olympiad ?olympiadCode ?olympiadName ?olympiadDescription WHERE {{
      ?olympiad eliozo:olympiadName ?olympiadName ;
                eliozo:olympiadDescription ?olympiadDescription ;
                eliozo:olympiadCode ?olympiadCode .
                FILTER (lang(?olympiadDescription) = "{language}")
                FILTER (lang(?olympiadName) = "{language}")
      OPTIONAL {{
        ?olympiad eliozo:olympiadCountry ?olympiadCountry .
      }}
    }} ORDER BY ?olympiadCountry ?olympiadName
    """
    return sparql_query(queryTemplate.format(language=lang))


def getSPARQLOlympiadYears(country, olympiad):
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?year ?grade WHERE {{
      ?problem eliozo:country '{country}' ;
               eliozo:olympiadCode '{olympiad}' ;
               eliozo:problemYear ?year ;
               eliozo:problemGrade ?grade .
    }} ORDER BY DESC(?year) ?grade"""
    return sparql_query(queryTemplate.format(country=country, olympiad=olympiad))


def getSPARQLOlympiadTimeIDs(country, olympiad):
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?problemTimeID  WHERE {{
      ?problem eliozo:country '{country}' ;
               eliozo:olympiadCode '{olympiad}' ;
               eliozo:problemTimeID ?problemTimeID .
    }} ORDER BY DESC(?problemTimeID)"""
    return sparql_query(queryTemplate.format(country=country, olympiad=olympiad))


def getSPARQLOlympiadTimeIDsGrades(country, olympiad):
    queryTemplate = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?problemTimeID ?grade WHERE {{
      ?problem eliozo:country '{country}' ;
               eliozo:olympiadCode '{olympiad}' ;
               eliozo:problemTimeID ?problemTimeID ;
               eliozo:problemGrade ?grade .
    }} ORDER BY DESC(?problemTimeID) ?grade"""
    return sparql_query(queryTemplate.format(country=country, olympiad=olympiad))


def getSPARQLOlympiadProblemsByEvent(event, country, olympiad, lang):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?text ?problemid ?problem_number ?problem_grade ?suffix WHERE {{
      ?problem eliozo:problemTimeID '{event}' .
      ?problem eliozo:country '{country}' .
      ?problem eliozo:problemTextHtml ?text .
      ?problem eliozo:problemID ?problemid .
      ?problem eliozo:problem_number ?problem_number .
      ?problem eliozo:problemGrade ?problem_grade .
      ?problem eliozo:olympiadCode '{olympiad_code}' .
      OPTIONAL {{ ?problem eliozo:problemSuffix ?suffix . }}
    }} ORDER BY ?problem_number
    """
    return sparql_query(queryTemplate.format(event=event, country=country, olympiad_code=olympiad))


def getSPARQLOlympiadProblemsByEventAndGrade(event, country, grade, olympiad, lang):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?text ?problemid ?problem_number WHERE {{
      ?problem eliozo:problemTimeID '{event}' .
      ?problem eliozo:country '{country}' .
      ?problem eliozo:problemTextHtml ?text .
      ?problem eliozo:problemID ?problemid .
      ?problem eliozo:problem_number ?problem_number .
      ?problem eliozo:problemGrade {grade} .
      ?problem eliozo:olympiadCode '{olympiad_code}' .
    }} ORDER BY ?problem_number
    """
    return sparql_query(queryTemplate.format(event=event, country=country, grade=grade, olympiad_code=olympiad))


def getSPARQLProblem(arg, lang):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemTextHtml ?problemYear ?country ?olympiad
           ?problemGrade ?problemBook ?problemBookSection
           ?problem_number ?topicIdentifier ?methodIdentifier
           ?concepts ?questionType ?domain ?video
           WHERE {{
      ?problem eliozo:problemID '{problemID}' ;
               eliozo:problemTextHtml ?problemTextHtml .
      OPTIONAL {{ ?problem eliozo:problemYear ?problemYear . }}
      OPTIONAL {{ ?problem eliozo:country ?country . }}
      OPTIONAL {{ ?problem eliozo:olympiad ?olympiad . }}
      OPTIONAL {{ ?problem eliozo:problemGrade ?problemGrade . }}
      OPTIONAL {{ ?problem eliozo:problemBook ?problemBook . }}
      OPTIONAL {{ ?problem eliozo:problemBookSection ?problemBookSection . }}
      OPTIONAL {{ ?problem eliozo:problem_number ?problem_number . }}
      OPTIONAL {{ ?problem eliozo:topic ?topic . ?topic eliozo:topicIdentifier ?topicIdentifier . }}
      OPTIONAL {{ ?problem eliozo:method ?method . ?method eliozo:methodIdentifier ?methodIdentifier . }}
      OPTIONAL {{ ?problem eliozo:concepts ?concepts . }}
      OPTIONAL {{ ?problem eliozo:questionType ?questionType . }}
      OPTIONAL {{ ?problem eliozo:domain ?domain . }}
      OPTIONAL {{ ?problem eliozo:hasVideo ?video . }}
    }}
    """
    return sparql_query(queryTemplate.format(problemID=arg))


def getSPARQLProblemSolutions(arg, lang):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemTextHtml ?solutionTextHtml ?solutionID WHERE {{
      ?problem eliozo:problemID '{problemID}' ;
              eliozo:problemTextHtml ?problemTextHtml .
      OPTIONAL {{
        ?problem eliozo:problemSolution ?soln .
        ?soln eliozo:solutionTextHtml ?solutionTextHtml .
        OPTIONAL {{ ?soln eliozo:solutionID ?solutionID . }}
      }}
    }}
    """
    return sparql_query(queryTemplate.format(problemID=arg))


def getSPARQLVideoBookmarks(arg):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>

    SELECT ?problem ?youtubeID ?videoTitle ?tstamp ?bmtext WHERE {{
        ?problem eliozo:problemID '{problemID}' .
        ?problem eliozo:hasVideo ?video .
        ?video eliozo:videoTitle ?videoTitle ;
              eliozo:videoYoutube ?youtubeID .
        OPTIONAL {{
            ?video eliozo:videoBookmarks ?seq .
            ?seq ?p ?bm .
            ?bm eliozo:videoBookmarkTstamp ?tstamp ;
                eliozo:videoBookmarkText ?bmtext .
        }}
    }}
    ORDER BY ?tstamp
    """
    return sparql_query(queryTemplate.format(problemID=arg))


def getAllSPARQLVideos():
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemid ?text ?textHtml ?youtubeID WHERE {
        ?problem eliozo:hasVideo ?video .
        ?video eliozo:videoYoutube ?youtubeID .
        ?problem eliozo:problemID ?problemid .
        ?problem eliozo:problemText ?text .
        ?problem eliozo:problemTextHtml ?textHtml .
    }
    """
    return sparql_query(queryTemplate)


def getSPARQLBook(bookid, sectionid):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo:<http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problem ?text ?imagefile ?problemid ?problem_number WHERE {{
      ?problem eliozo:problemBook '{bookid}' ;
               eliozo:problemBookSection '{sectionid}' ;
               eliozo:problemID ?problemid ;
               eliozo:problemTextHtml ?text .
      OPTIONAL {{ ?problem eliozo:hasImage ?imagefile . }}
      OPTIONAL {{ ?problem eliozo:problem_number ?problem_number . }}
    }} ORDER BY ?problemid
    """
    return sparql_query(queryTemplate.format(bookid=bookid, sectionid=sectionid))
