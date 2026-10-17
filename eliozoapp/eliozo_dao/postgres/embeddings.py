"""Text embeddings from the OpenAI API (or any OpenAI-compatible endpoint).

The API key is read from OPENAI_API_KEY; OPENAI_BASE_URL, if set, points the
client at a compatible endpoint (the OpenAI library reads it itself). One
client is created per process on first use and shared: it is thread-safe and
keeps its HTTP connections open.
"""

import threading
from functools import lru_cache

from openai import OpenAI

from .db import EMBEDDING_DIM, load_environment

EMBEDDING_MODEL = 'text-embedding-3-small'

# The model accepts at most 8191 tokens per input; texts are cut to this many
# characters first, which stays below that for Latvian text with LaTeX.
MAX_INPUT_CHARS = 8000

# Inputs per API request when embedding many texts.
BATCH_SIZE = 100

_client = None
_client_lock = threading.Lock()


def get_client():
    global _client
    if _client is not None:
        return _client
    with _client_lock:
        if _client is None:
            load_environment()
            # Without an explicit api_key the library reads OPENAI_API_KEY and
            # raises a clear error if it is missing.
            _client = OpenAI(timeout=20.0, max_retries=2)
    return _client


def embed_texts(texts, task='document'):
    """Embeddings of ``texts``, in the same order.

    ``task`` is "document" for indexing and "query" for search queries.
    text-embedding-3-small ignores the distinction; it is kept so that a model
    with asymmetric query/document prefixes can be swapped in here.
    """
    vectors = []
    for start in range(0, len(texts), BATCH_SIZE):
        batch = [t[:MAX_INPUT_CHARS] for t in texts[start:start + BATCH_SIZE]]
        resp = get_client().embeddings.create(model=EMBEDDING_MODEL, input=batch,
                                              encoding_format='float')
        vectors.extend(item.embedding for item in sorted(resp.data, key=lambda d: d.index))
    for v in vectors:
        if len(v) != EMBEDDING_DIM:
            raise ValueError('%s returned %d dimensions, the database expects %d'
                             % (EMBEDDING_MODEL, len(v), EMBEDDING_DIM))
    return vectors


def embed_text(text, task='document'):
    return embed_texts([text], task)[0]


@lru_cache(maxsize=256)
def embed_query(text):
    """Embedding of a search query, cached: paging through the results of one
    query must not call the API again for every page."""
    return tuple(embed_text(text, task='query'))
