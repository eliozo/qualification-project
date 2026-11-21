"""Load TTL files into the embedded oxigraph store.

Usage:
    python -m eliozo_dao.load_rdf [SOURCE_DIR ...]

If no directories are given, the script loads from the two default locations:

  * <repo>/../worksheet-generation-with-llms/scripts/setup/resources
    (metadata: topics, methods, olympiads, ...)
  * eliozoapp/data/problem_ttl
    (problems, written by ``python -m eliozo_dao.import_problems``)

Override the store location with the ``OXIGRAPH_DB_PATH`` env var
(default: ``eliozoapp/data/oxigraph_db``).

The script rebuilds the store from scratch each time: it removes the target
directory before loading so re-running is idempotent. Stop the Flask app
before running — oxigraph holds an exclusive lock on the store path.

The store-level helpers below (``resolve_store_path``, ``create_store``,
``drop_store``, ``collect_ttl_files``, ``load_ttl_files``) are also used by
``worksheet-generation-with-llms/scripts/eliozo_client.py`` (subcommands
``drop-rdf``, ``create-rdf-dataset`` and ``ingest-rdf``), so both tools load
RDF in exactly the same way.
"""

import argparse
import os
import shutil
import sys
import time
from glob import glob

from pyoxigraph import RdfFormat, Store

from . import OXIGRAPH_DB_PATH
from .import_problems import PROBLEM_TTL_DIR

_DEFAULT_SOURCE_DIRS = [
    os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..",
        "worksheet-generation-with-llms", "scripts", "setup", "resources")),
    PROBLEM_TTL_DIR,
]

#: Store name that refers to the store the Flask app serves (``OXIGRAPH_DB_PATH``).
PUBLIC_STORE = "public"


def resolve_store_path(store):
    """Map a store name to its directory.

    ``"public"`` is the store read by the Flask app (``OXIGRAPH_DB_PATH``);
    any other value is taken as a path to a store directory.
    """
    if store == PUBLIC_STORE:
        return OXIGRAPH_DB_PATH
    return os.path.abspath(store)


def is_store_dir(path):
    """True if ``path`` is an existing oxigraph (RocksDB) store directory."""
    return os.path.isfile(os.path.join(path, "CURRENT"))


def create_store(path):
    """Create an empty store at ``path`` (no-op if one exists). Returns True if created."""
    if is_store_dir(path):
        return False
    os.makedirs(path, exist_ok=True)
    store = Store(path)
    store.flush()
    del store
    return True


def drop_store(path):
    """Delete the store at ``path``. Returns True if something was deleted.

    Refuses to delete a non-empty directory that is not an oxigraph store,
    so a mistyped path cannot wipe unrelated files.
    """
    if not os.path.exists(path):
        return False
    if not os.path.isdir(path) or (os.listdir(path) and not is_store_dir(path)):
        raise ValueError(f"not an oxigraph store, refusing to delete: {path}")
    shutil.rmtree(path)
    return True


def collect_ttl_files(sources):
    """Expand directories (their ``*.ttl`` files, sorted) and plain files into a file list."""
    files = []
    for src in sources:
        if os.path.isdir(src):
            files.extend(sorted(glob(os.path.join(src, "*.ttl"))))
        elif os.path.isfile(src):
            files.append(src)
        else:
            print(f"warning: source not found, skipping: {src}", file=sys.stderr)
    return files


def load_ttl_files(path, ttl_files):
    """Bulk-load Turtle files into the store at ``path`` (created if missing).

    Returns ``(loaded, failed)`` lists of file paths. A file that fails to
    parse is reported and skipped; the others are still loaded.
    """
    os.makedirs(path, exist_ok=True)
    store = Store(path)
    loaded, failed = [], []
    n = len(ttl_files)
    print(f"loading {n} TTL file(s) into {path}")
    for i, ttl in enumerate(ttl_files, 1):
        try:
            store.bulk_load(path=ttl, format=RdfFormat.TURTLE)
        except (SyntaxError, OSError, ValueError) as exc:
            print(f"  [{i}/{n}] FAILED {ttl}: {exc}", file=sys.stderr)
            failed.append(ttl)
            continue
        print(f"  [{i}/{n}] {os.path.basename(ttl)}")
        loaded.append(ttl)
    store.flush()
    store.optimize()
    del store
    return loaded, failed


def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("source_dirs", nargs="*",
                        help="Directories containing .ttl files. "
                             "Defaults to the two worksheet-generation-with-llms dirs.")
    parser.add_argument("--keep", action="store_true",
                        help="Append to existing store instead of wiping it first.")
    args = parser.parse_args()

    source_dirs = args.source_dirs or _DEFAULT_SOURCE_DIRS
    if not args.source_dirs and not glob(os.path.join(PROBLEM_TTL_DIR, "*.ttl")):
        print(f"error: no problem TTL files in {PROBLEM_TTL_DIR}\n"
              "Generate them first:  python -m eliozo_dao.import_problems", file=sys.stderr)
        sys.exit(1)
    ttl_files = collect_ttl_files(source_dirs)
    if not ttl_files:
        print("error: no .ttl files found in: " + ", ".join(source_dirs), file=sys.stderr)
        sys.exit(1)

    if not args.keep and os.path.isdir(OXIGRAPH_DB_PATH):
        print(f"removing existing store at {OXIGRAPH_DB_PATH}")
        shutil.rmtree(OXIGRAPH_DB_PATH)

    start = time.time()
    load_ttl_files(OXIGRAPH_DB_PATH, ttl_files)
    elapsed = time.time() - start
    print(f"done in {elapsed:.1f}s")


if __name__ == "__main__":
    main()
