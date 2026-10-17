"""SQLAlchemy engine and ORM models for the PostgreSQL + pgvector database.

No host names or credentials live in code. The connection is described either
by ``DATABASE_URL`` or by the ``DB_HOST``, ``DB_PORT``, ``DB_NAME``,
``DB_USER`` and ``DB_PASSWORD`` variables. On the workstation they point at the
Docker container of ``eliozo-db``; on the server at the system PostgreSQL.

The variables come from the dotenv file named by ``ELIOZO_ENV_FILE`` (the
``flask-run.*`` scripts set it to ``eliozo-db/.env``) or, without it, from the
process environment (a systemd ``EnvironmentFile``, the shell). A file named
explicitly wins over variables already in the environment, so that a stale
OPENAI_API_KEY in the shell does not shadow the project's key.

The models mirror the tables created by the Alembic migrations in
``eliozo-db/alembic/versions``; keep them in step with those.
"""

import os
import threading

from dotenv import load_dotenv
from pgvector.sqlalchemy import Vector
from sqlalchemy import (Boolean, DateTime, ForeignKey, Integer, Text, UniqueConstraint,
                        create_engine, func)
from sqlalchemy.engine import URL
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

# OpenAI text-embedding-3-small; the vector(...) width of both tables.
EMBEDDING_DIM = 1536

# Seconds to wait for a connection before giving up, so that a stopped
# database makes a search fail quickly instead of hanging the request.
CONNECT_TIMEOUT = 5

DB_VARIABLES = ('DB_HOST', 'DB_PORT', 'DB_NAME', 'DB_USER', 'DB_PASSWORD')

_engine = None
_engine_lock = threading.Lock()


def load_environment():
    """Load the dotenv file named by ELIOZO_ENV_FILE, if any, over the environment.

    Returns the path of the loaded file, or None.
    """
    path = os.environ.get('ELIOZO_ENV_FILE')
    if path and os.path.isfile(path):
        load_dotenv(path, override=True)
        return path
    return None


def missing_settings():
    """Names of the connection variables that are not set (empty if all are)."""
    if os.environ.get('DATABASE_URL'):
        return []
    return [name for name in DB_VARIABLES if not os.environ.get(name)]


def database_url():
    """The SQLAlchemy URL built from the environment (psycopg 3 driver)."""
    load_environment()
    if os.environ.get('DATABASE_URL'):
        return os.environ['DATABASE_URL']
    missing = missing_settings()
    if missing:
        raise RuntimeError(
            'PostgreSQL connection settings missing: %s. Set them in the environment '
            'or in the file named by ELIOZO_ENV_FILE.' % ', '.join(missing))
    # URL.create quotes special characters in the password properly.
    return URL.create(
        'postgresql+psycopg',
        username=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host=os.environ['DB_HOST'],
        port=int(os.environ['DB_PORT']),
        database=os.environ['DB_NAME'],
    )


def get_engine():
    """The process-wide engine, created on first use."""
    global _engine
    if _engine is not None:
        return _engine
    with _engine_lock:
        if _engine is None:
            _engine = create_engine(database_url(), pool_pre_ping=True,
                                    connect_args={'connect_timeout': CONNECT_TIMEOUT})
    return _engine


class Base(DeclarativeBase):
    pass


class Problem(Base):
    """One problem; ``content`` is its statement in one language (``lang``)."""
    __tablename__ = 'problems'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    # The problem ID as shown in the app, e.g. LV.SOL.2020.5.1 (eliozo:problemID),
    # not a full RDF IRI despite the column name.
    problem_iri: Mapped[str] = mapped_column(Text, nullable=False, unique=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)  # Markdown, may contain LaTeX
    lang: Mapped[str | None] = mapped_column(Text)
    has_image: Mapped[bool | None] = mapped_column(Boolean, server_default='false')
    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    embedding = mapped_column(Vector(EMBEDDING_DIM))

    solution_chunks: Mapped[list['SolutionChunk']] = relationship(
        back_populates='problem', cascade='all, delete-orphan',
        order_by='SolutionChunk.chunk_id')

    def __repr__(self):
        return '<Problem %s>' % self.problem_iri


class SolutionChunk(Base):
    """A piece of a problem's solution text, embedded separately."""
    __tablename__ = 'solution_chunks'
    __table_args__ = (UniqueConstraint('problem_id', 'chunk_id'),)

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    problem_id: Mapped[int] = mapped_column(
        Integer, ForeignKey('problems.id', ondelete='CASCADE'), nullable=False)
    chunk_id: Mapped[int] = mapped_column(Integer, nullable=False)  # 0-based order within the problem
    content: Mapped[str] = mapped_column(Text, nullable=False)
    lang: Mapped[str | None] = mapped_column(Text)
    embedding = mapped_column(Vector(EMBEDDING_DIM))

    problem: Mapped[Problem] = relationship(back_populates='solution_chunks')

    def __repr__(self):
        return '<SolutionChunk %s/%d>' % (self.problem_id, self.chunk_id)
