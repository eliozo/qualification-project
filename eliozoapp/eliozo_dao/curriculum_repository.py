from . import sparql_query


# The curriculum functions take ``grades`` as a collection of grade numbers
# (problems of any of these grades match; empty or None means all grades)
# and ``years`` as an inclusive (min, max) pair.
def _gradeFilter(grades):
    if not grades:
        return ''
    return 'FILTER (?grade IN (%s))' % ', '.join(str(int(g)) for g in sorted(grades))


def getSPARQLCurriculumCoverage(olympiads):
    """Distinct (olympiad, year, grade) combinations of the given olympiads' problems."""
    queryTemplate = """
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT DISTINCT ?olympiad ?year ?grade WHERE {{
        VALUES ?olympiad {{ {olympiads} }}
        ?problem a eliozo:Problem ;
                 eliozo:olympiad ?olympiad ;
                 eliozo:problemYear ?year ;
                 eliozo:problemGrade ?grade .
    }}
    """
    return sparql_query(queryTemplate.format(olympiads=' '.join("'%s'" % o for o in olympiads)))


def getSPARQLCurriculumQuestionTypes(olympiad, grades, years):
    """Problems with their question type and domain (if any); the question type's
    name, description and sort keys come from its eliozo:Question resource, if there is one."""
    queryTemplate = """
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID ?questionType ?domain ?questionName ?questionDescription ?L1 ?L2 WHERE {{
        ?problem a eliozo:Problem ;
                 eliozo:problemID ?problemID ;
                 eliozo:olympiad '{olympiadCode}' ;
                 eliozo:problemGrade ?grade ;
                 eliozo:problemYear ?year ;
                 eliozo:questionType ?questionType .
        {gradeFilter}
        FILTER (?year <= {yearMax} && ?year >= {yearMin})
        OPTIONAL {{ ?problem eliozo:domain ?domain . }}
        OPTIONAL {{
            ?question a eliozo:Question ;
                      eliozo:questionID ?questionType ;
                      eliozo:questionName ?questionName ;
                      eliozo:questionDescription ?questionDescription ;
                      eliozo:sorter_L1 ?L1 ;
                      eliozo:sorter_L2 ?L2 .
        }}
    }}
    """
    return sparql_query(queryTemplate.format(olympiadCode=olympiad,
                                             gradeFilter=_gradeFilter(grades),
                                             yearMax=years[1],
                                             yearMin=years[0]))


def getSPARQLOlympiadOverview(olympiad, grades, years):
    queryTemplate = """
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemID ?topicID ?topicNumber ?topicName ?topicDescription ?L1 ?L2 ?L3 WHERE {{
  ?problem eliozo:topic ?topic ;
           eliozo:problemID ?problemID ;
           eliozo:olympiad '{olympiadCode}' ;
           eliozo:problemGrade ?grade ;
           eliozo:problemYear ?year .
  {gradeFilter}
  FILTER (?year <= {yearMax} && ?year >= {yearMin})
  ?topic a eliozo:Topic ;
            eliozo:topicID ?topicID ;
            eliozo:topicNumber ?topicNumber ;
            eliozo:topicName ?topicName ;
            eliozo:topicDescription ?topicDescription ;
            eliozo:sorter_L1 ?L1 ;
            eliozo:sorter_L2 ?L2 ;
            eliozo:sorter_L3 ?L3 ;
            eliozo:sorter_L4 ?L4 ;
            eliozo:sorter_L5 ?L5 .
}} ORDER BY ?L1 ?L2 ?L3 ?L4 ?L5
"""
    return sparql_query(queryTemplate.format(olympiadCode=olympiad,
                                             gradeFilter=_gradeFilter(grades),
                                             yearMax=years[1],
                                             yearMin=years[0]))


def getSPARQLCurriculumMethods(olympiad, grades, years):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID ?methodID ?methodNumber ?methodName ?methodDescription ?L1 ?L2 WHERE {{
    ?problem eliozo:method ?method ;
            eliozo:problemID ?problemID ;
            eliozo:olympiad '{olympiadCode}' ;
            eliozo:problemGrade ?grade ;
            eliozo:problemYear ?year .
    {gradeFilter}
    FILTER (?year <= {yearMax} && ?year >= {yearMin})
    ?method a eliozo:Method ;
                eliozo:methodNumber ?methodNumber ;
                eliozo:methodID ?methodID ;
                eliozo:methodName ?methodName ;
                eliozo:methodDescription ?methodDescription ;
                eliozo:sorter_L1 ?L1 ;
                eliozo:sorter_L2 ?L2 .
    }} ORDER BY ?L1 ?L2
    """
    return sparql_query(queryTemplate.format(olympiadCode=olympiad,
                                             gradeFilter=_gradeFilter(grades),
                                             yearMax=years[1],
                                             yearMin=years[0]))


def getSPARQLCurriculumSubdomains(olympiad, grades, years):
    queryTemplate = """
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX skos: <http://www.w3.org/2004/02/skos/core#>
    PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
    SELECT ?problemID ?domainID ?domainName ?domainDescription ?L1 ?L2 ?L3 WHERE {{
      ?problem eliozo:subdomain ?domain ;
               eliozo:problemID ?problemID ;
               eliozo:olympiad '{olympiadCode}' ;
               eliozo:problemGrade ?grade ;
               eliozo:problemYear ?year .
      {gradeFilter}
      FILTER (?year <= {yearMax} && ?year >= {yearMin})
      ?domain a eliozo:Domain ;
              eliozo:domainID ?domainID ;
              eliozo:domainName ?domainName ;
              eliozo:domainDescription ?domainDescription ;
              eliozo:sorter_L1 ?L1 ;
              eliozo:sorter_L2 ?L2 ;
              eliozo:sorter_L3 ?L3 .
    }} ORDER BY ?L1 ?L2 ?L3 ?problemID
    """
    return sparql_query(queryTemplate.format(olympiadCode=olympiad,
                                             gradeFilter=_gradeFilter(grades),
                                             yearMax=years[1],
                                             yearMin=years[0]))
