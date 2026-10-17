"""Nearest problems to a query text by embedding (cosine) distance.

Problem statements and solution chunks are searched separately, each with an
``ORDER BY distance LIMIT`` query so that its HNSW index is used, and merged
per problem: a problem ranks by its closest text.
"""

from sqlalchemy import select, text
from sqlalchemy.orm import Session

from .db import Problem, SolutionChunk, get_engine
from .embeddings import embed_query

# How many problems a semantic search returns in all (shown on several pages).
SEMANTIC_RESULT_LIMIT = 20

# Solution chunks fetched per wanted problem: one problem has several chunks
# (solutions and their translations), so more chunks than problems are needed
# to still find SEMANTIC_RESULT_LIMIT distinct problems.
CHUNKS_PER_PROBLEM = 3

# Candidate list size of the HNSW index scan (pgvector default 40). It caps the
# rows an index scan can return, so it must be at least the LIMIT used.
HNSW_EF_SEARCH = 100


def semanticSearch(queryText, includeSolutions, limit=SEMANTIC_RESULT_LIMIT):
    """The ``limit`` problems closest to ``queryText``, closest first.

    Returns a list of dicts::

        {'problemid':      e.g. 'LV.SOL.2020.5.1',
         'distance':       cosine distance of the closest text (0 = same direction),
         'content':        the stored problem statement (Markdown),
         'contentLang':    its language,
         'inSolution':     True if a solution text is closer than the statement,
         'solutionLang':   the language of that solution text, or None}

    With ``includeSolutions`` False only the problem statements are searched.
    """
    queryVector = list(embed_query(queryText))
    problemRows, chunkRows = [], []

    with Session(get_engine()) as session:
        # SET LOCAL lasts until the end of this session's transaction.
        session.execute(text('SET LOCAL hnsw.ef_search = %d' % max(HNSW_EF_SEARCH, limit * CHUNKS_PER_PROBLEM)))

        distance = Problem.embedding.cosine_distance(queryVector).label('distance')
        problemRows = session.execute(
            select(Problem.problem_iri, Problem.content, Problem.lang, distance)
            .where(Problem.embedding.is_not(None))
            .order_by(distance)
            .limit(limit)).all()

        if includeSolutions:
            distance = SolutionChunk.embedding.cosine_distance(queryVector).label('distance')
            chunkRows = session.execute(
                select(Problem.problem_iri, Problem.content, Problem.lang, SolutionChunk.lang, distance)
                .join(SolutionChunk.problem)
                .where(SolutionChunk.embedding.is_not(None))
                .order_by(distance)
                .limit(limit * CHUNKS_PER_PROBLEM)).all()

    return mergeHits(problemRows, chunkRows, limit)


def mergeHits(problemRows, chunkRows, limit):
    """Merge the nearest statements and the nearest solution chunks per problem.

    ``problemRows`` are (problemid, content, lang, distance) tuples,
    ``chunkRows`` (problemid, content, lang, solutionLang, distance) tuples.
    Returns the result list of ``semanticSearch``.
    """
    found = {}
    for problemid, content, lang, d in problemRows:
        found[problemid] = {'problemid': problemid, 'content': content, 'contentLang': lang,
                            'problemDistance': d, 'solutionDistance': None, 'solutionLang': None}
    for problemid, content, lang, solutionLang, d in chunkRows:
        hit = found.setdefault(problemid, {
            'problemid': problemid, 'content': content, 'contentLang': lang,
            'problemDistance': None, 'solutionDistance': None, 'solutionLang': None})
        if hit['solutionDistance'] is None or d < hit['solutionDistance']:
            hit['solutionDistance'] = d
            hit['solutionLang'] = solutionLang

    results = []
    for hit in found.values():
        # A problem found only through a solution chunk has no statement
        # distance: its statement was not among the closest ones.
        inSolution = hit['solutionDistance'] is not None and (
            hit['problemDistance'] is None or hit['solutionDistance'] < hit['problemDistance'])
        results.append({
            'problemid': hit['problemid'],
            'distance': hit['solutionDistance'] if inSolution else hit['problemDistance'],
            'content': hit['content'],
            'contentLang': hit['contentLang'],
            'inSolution': inSolution,
            'solutionLang': hit['solutionLang'] if inSolution else None,
        })
    results.sort(key=lambda r: (r['distance'], r['problemid']))
    return results[:limit]
