"""PostgreSQL + pgvector data access (semantic search).

The RDF store (``eliozo_dao.sparql_query``) stays the source of truth for
problems; PostgreSQL holds a copy of the problem and solution texts with their
embeddings, so that they can be searched by meaning.

Modules:

  db               engine, environment loading, ``Problem`` / ``SolutionChunk``
  embeddings       OpenAI embedding client
  semantic_search  nearest problems to a query text
  check            ``python -m eliozo_dao.postgres.check``: is the DB up?
  load_problems    ``python -m eliozo_dao.postgres.load_problems``: copy the
                   RDF store's problems and solutions into PostgreSQL

The schema itself is owned by the Alembic migrations in ``eliozo-db``.
Connection settings and the OpenAI key come from the environment only; see
``db.load_environment``.
"""
