"""The Markdown help documents under eliozo/content/<docname>/content_<lang>.md."""

import os
import re
from functools import lru_cache

# eliozoapp/eliozo/content -- one directory per document, holding one Markdown
# file per language.
CONTENT_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'content')

# Only letters, digits, underscore and hyphen: no '/' and no '.', so a document
# name can never escape CONTENT_ROOT.
DOC_NAME_RE = re.compile(r'[A-Za-z0-9_-]+')

# Top-level documents under "Info": about the project (first item) and the
# help on writing SPARQL queries for the Advanced Search page.
ABOUT_PROJECT_DOC = 'about_project'
ABOUT_ADVANCED_SEARCH_DOC = 'about_advanced_search'

# The introduction to the ontology and the documents of the classifiers, in the
# order of the table in ontology/content_*.md. They are the leaves of the nested
# menu "Info > Advanced Search" (the node itself opens no document).
ONTOLOGY_DOC = 'ontology'
ONTOLOGY_SUBPAGES = [
    'ontology_topics',
    'ontology_methods',
    'ontology_genres',
    'ontology_question_types',
    'ontology_concepts',
    'ontology_olympiads',
    'ontology_models',
    'ontology_hint_types',
    'ontology_hints',
]


def find_content_file(docname, lang):
    """Path of ``content/<docname>/content_<lang>.md``, or None.

    English is the fallback when the requested language is missing.
    """
    if not docname or not DOC_NAME_RE.fullmatch(docname):
        return None
    doc_dir = os.path.join(CONTENT_ROOT, docname)
    for name in (f'content_{lang}.md', 'content_en.md'):
        path = os.path.join(doc_dir, name)
        if os.path.isfile(path):
            return path
    return None


@lru_cache(maxsize=256)
def _first_heading(path, mtime):
    with open(path, encoding='utf-8') as f:
        for line in f:
            if line.startswith('# '):
                return line[2:].strip()
    return None


def content_doc_title(docname, lang):
    """The document's own title (its first '# ' heading) in *lang*, or None."""
    path = find_content_file(docname, lang)
    if path is None:
        return None
    return _first_heading(path, os.path.getmtime(path))
