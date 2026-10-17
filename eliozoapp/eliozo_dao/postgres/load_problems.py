"""Copy the problems and solutions of the RDF store into PostgreSQL.

    python -m eliozo_dao.postgres.load_problems                      # fake embeddings
    python -m eliozo_dao.postgres.load_problems --embeddings openai  # real ones
    python -m eliozo_dao.postgres.load_problems --limit 50           # first 50 problems

The tables are rebuilt from scratch on every run. Each problem gets one row
with its statement in one language (Latvian if there is one; see
``problem_listing.preferredLanguage``); every solution text, in every
language, becomes one solution chunk.

``--embeddings fake`` (the default) stores deterministic pseudo-random unit
vectors: the search runs end to end, but its ranking means nothing.
``--embeddings openai`` embeds every text with the OpenAI API (about 1M tokens
for the whole problem base) and needs OPENAI_API_KEY.

Reads the oxigraph store read-only, so the Flask app may keep running.
"""

import argparse
import hashlib
import json
import math
import random
import sys
from collections import defaultdict

from sqlalchemy import text
from sqlalchemy.orm import Session

from .. import sparql_query
from ..problem_listing import UNTAGGED, preferredLanguage
from .db import EMBEDDING_DIM, Problem, SolutionChunk, get_engine

# Language of the stored problem statement when the problem has several.
PROBLEM_LANGUAGE = 'lv'


def fake_embedding(content):
    """A pseudo-random unit vector, the same for the same text. NOT a real embedding."""
    rng = random.Random(hashlib.sha256(content.encode('utf-8')).digest())
    v = [rng.gauss(0.0, 1.0) for _ in range(EMBEDDING_DIM)]
    norm = math.sqrt(sum(x * x for x in v))
    return [x / norm for x in v]


def _bindings(query):
    return json.loads(sparql_query(query))['results']['bindings']


def read_problems():
    """{problemid: {'texts': {lang: markdown}, 'solutions': [(solutionKey, lang, markdown)]}}"""
    problems = defaultdict(lambda: {'texts': {}, 'solutions': []})
    for row in _bindings("""PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemid ?text WHERE {
    ?problem eliozo:problemID ?problemid ;
             eliozo:problemText ?text .
}"""):
        content = row['text']['value']
        if content.strip():
            problems[row['problemid']['value']]['texts'][row['text'].get('xml:lang', UNTAGGED)] = content

    for row in _bindings("""PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT ?problemid ?solution ?num ?text WHERE {
    ?problem eliozo:problemID ?problemid ;
             eliozo:problemSolution ?solution .
    ?solution eliozo:solutionText ?text .
    OPTIONAL { ?solution eliozo:solutionNum ?num . }
}"""):
        content = row['text']['value']
        if content.strip() and row['problemid']['value'] in problems:
            key = (row['num']['value'] if 'num' in row else '', row['solution']['value'])
            problems[row['problemid']['value']]['solutions'].append(
                (key, row['text'].get('xml:lang', UNTAGGED), content))
    return problems


def build_rows(problems, limit=None):
    """ORM objects for ``problems`` (without embeddings), in problem ID order."""
    rows = []
    for problemid in sorted(problems)[:limit]:
        p = problems[problemid]
        if not p['texts']:
            continue
        lang = preferredLanguage(p['texts'], PROBLEM_LANGUAGE)
        content = p['texts'][lang]
        problem = Problem(problem_iri=problemid, content=content, lang=lang,
                          has_image='![' in content or '<img' in content)
        for chunkId, (_, solLang, solText) in enumerate(sorted(p['solutions'])):
            problem.solution_chunks.append(SolutionChunk(chunk_id=chunkId, content=solText, lang=solLang))
        rows.append(problem)
    return rows


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--embeddings', choices=('fake', 'openai'), default='fake')
    parser.add_argument('--limit', type=int, default=None, help='load only the first N problems')
    args = parser.parse_args(argv)

    rows = build_rows(read_problems(), args.limit)
    targets = rows + [c for p in rows for c in p.solution_chunks]
    print('%d problems, %d solution chunks' % (len(rows), len(targets) - len(rows)))

    if args.embeddings == 'openai':
        from .embeddings import embed_texts
        print('Embedding %d texts with OpenAI ...' % len(targets))
        vectors = embed_texts([t.content for t in targets])
    else:
        vectors = [fake_embedding(t.content) for t in targets]
    for target, vector in zip(targets, vectors):
        target.embedding = vector

    with Session(get_engine()) as session, session.begin():
        session.execute(text('TRUNCATE problems, solution_chunks RESTART IDENTITY'))
        session.add_all(rows)
    print('Loaded into PostgreSQL (%s embeddings).' % args.embeddings)
    return 0


if __name__ == '__main__':
    sys.exit(main())
