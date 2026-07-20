"""Load TTL files into the embedded oxigraph store.

Usage:
    python -m eliozo_dao.load_rdf [SOURCE_DIR ...]

If no directories are given, the script loads from the two default locations
used by the worksheet-generation project:

  * <repo>/../worksheet-generation-with-llms/scripts/setup/resources
  * <repo>/../worksheet-generation-with-llms/scripts/setup/temp

Override the store location with the ``OXIGRAPH_DB_PATH`` env var
(default: ``eliozoapp/data/oxigraph_db``).

The script rebuilds the store from scratch each time: it removes the target
directory before loading so re-running is idempotent. Stop the Flask app
before running — oxigraph holds an exclusive lock on the store path.
"""

import argparse
import os
import shutil
import sys
import time
from glob import glob

from pyoxigraph import RdfFormat, Store

from . import OXIGRAPH_DB_PATH

_DEFAULT_SOURCE_DIRS = [
    os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..",
        "worksheet-generation-with-llms", "scripts", "setup", "resources")),
    os.path.normpath(os.path.join(
        os.path.dirname(__file__), "..", "..", "..",
        "worksheet-generation-with-llms", "scripts", "setup", "temp")),
]


def collect_ttl_files(source_dirs):
    files = []
    for d in source_dirs:
        if not os.path.isdir(d):
            print(f"warning: source dir not found, skipping: {d}", file=sys.stderr)
            continue
        files.extend(sorted(glob(os.path.join(d, "*.ttl"))))
    return files


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
    ttl_files = collect_ttl_files(source_dirs)
    if not ttl_files:
        print("error: no .ttl files found in: " + ", ".join(source_dirs), file=sys.stderr)
        sys.exit(1)

    if not args.keep and os.path.isdir(OXIGRAPH_DB_PATH):
        print(f"removing existing store at {OXIGRAPH_DB_PATH}")
        shutil.rmtree(OXIGRAPH_DB_PATH)

    os.makedirs(OXIGRAPH_DB_PATH, exist_ok=True)
    store = Store(OXIGRAPH_DB_PATH)

    start = time.time()
    print(f"loading {len(ttl_files)} TTL file(s) into {OXIGRAPH_DB_PATH}")
    for i, path in enumerate(ttl_files, 1):
        try:
            store.bulk_load(path=path, format=RdfFormat.TURTLE)
        except (SyntaxError, OSError, ValueError) as exc:
            print(f"  [{i}/{len(ttl_files)}] FAILED {path}: {exc}", file=sys.stderr)
            continue
        print(f"  [{i}/{len(ttl_files)}] {os.path.basename(path)}")

    store.flush()
    store.optimize()
    elapsed = time.time() - start
    print(f"done in {elapsed:.1f}s")


if __name__ == "__main__":
    main()
