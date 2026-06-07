# eliozo_dao

Data access layer for the Eliozo Flask app. Talks to an **embedded
[pyoxigraph](https://pyoxigraph.readthedocs.io/) store** — no separate
Apache Jena Fuseki / Tomcat process required.

## Overview

| | |
|---|---|
| Backend | pyoxigraph 0.5+ (Rust [oxigraph](https://github.com/oxigraph/oxigraph) bindings) |
| Storage | On-disk RocksDB store at `eliozoapp/data/oxigraph_db` |
| Query API | `from eliozo_dao import sparql_query` → returns SPARQL 1.1 JSON Results string |

The repositories in this package (`problem_repository.py`,
`indexes_repository.py`, etc.) all delegate to `sparql_query(...)`. The
returned text is the standard SPARQL JSON results format, so callers can
do `json.loads(text)["results"]["bindings"]` exactly as they did when the
backend was Fuseki.

## One-time setup

Install the dependency into your venv:

```bash
pip install pyoxigraph
```

(Once `setup.py` is updated, this is pulled in automatically.)

## Importing RDF data

The loader walks one or more directories for `*.ttl` files and bulk-loads
them. Default source directories are the two TTL trees in the sibling
`worksheet-generation-with-llms` project:

- `worksheet-generation-with-llms/scripts/setup/resources/`
- `worksheet-generation-with-llms/scripts/setup/temp/`

Stop the Flask app first (oxigraph holds an exclusive lock on the store),
then run:

```bash
cd qualification-project/eliozoapp
source ../venv-eliozo/bin/activate
python -m eliozo_dao.load_rdf
```

To load from custom directories:

```bash
python -m eliozo_dao.load_rdf /path/to/dir1 /path/to/another/dir
```

To append to an existing store instead of wiping it first:

```bash
python -m eliozo_dao.load_rdf --keep /path/to/extra/data
```

To override the store location:

```bash
OXIGRAPH_DB_PATH=/var/lib/eliozo/oxigraph python -m eliozo_dao.load_rdf
```

After loading you can start the Flask app:

```bash
./flask-run.sh
```

## Persistence and how often to run `load_rdf`

The oxigraph store is a **RocksDB database on disk**, not an in-memory cache.
Everything you load survives across Flask restarts, machine reboots, and
`pip` upgrades — the data lives in files, not in the Python process.

So `load_rdf` is a **one-time setup step**, not something to re-run before
each `flask run`. The usual lifecycle is:

| Situation | Re-run `load_rdf`? |
|---|---|
| Restarting the Flask app | No |
| Rebooting the machine | No |
| Upgrading pyoxigraph or other deps | No |
| New / changed TTL files you want to pick up | Yes |
| Suspect the store is corrupted | Yes (it wipes and rebuilds) |
| Switching to a new `OXIGRAPH_DB_PATH` | Yes (the new path is empty) |

Re-running is cheap and idempotent (≈1.4s for the full 80-file fixture on a
laptop), so when in doubt, just re-run it.

## Where the store files live

By default the store is at:

```
qualification-project/eliozoapp/data/oxigraph_db/
```

That directory is created on first `load_rdf` and contains RocksDB
internals — `*.sst` data files, `MANIFEST-*`, `CURRENT`, `LOG`, `OPTIONS-*`,
and a `LOCK` file. **Do not edit, rename, or delete individual files
inside it.** If you want a clean state, remove the whole directory and
re-run `load_rdf` (which does this for you unless `--keep` is passed).

A few practical notes to avoid disturbing it:

- The `LOCK` file is held while any process has the store open for writing.
  If you see "resource temporarily unavailable" when starting the loader,
  the Flask app or another loader is still running — stop it first.
- The Flask app opens the store **read-only**, so it does not take the
  writer lock and multiple Flask workers can read concurrently.
- Add `eliozoapp/data/` to `.gitignore` — the store is regenerated from
  TTL sources and should not be committed.
- To relocate the store (e.g. to `/var/lib/eliozo/oxigraph_db` on
  production), set `OXIGRAPH_DB_PATH` in your shell / systemd unit / `.env`
  before running both `load_rdf` and the Flask app.

## Running a test SELECT query

Two equally valid ways.

### From a Python REPL

```python
import json
from eliozo_dao import sparql_query

raw = sparql_query("""
PREFIX eliozo: <http://www.dudajevagatve.lv/eliozo#>
SELECT (COUNT(*) AS ?n) WHERE {
  ?p a eliozo:Problem .
}
""")

print(json.loads(raw)["results"]["bindings"])
# -> [{'n': {'datatype': 'http://www.w3.org/2001/XMLSchema#integer',
#            'type': 'literal', 'value': '1234'}}]
```

### Via the bundled probe script

```bash
python -m eliozo.cmd_post
```

This runs a small SELECT against the store and prints the raw JSON.

## Response shape

`sparql_query` returns a string containing the
[SPARQL 1.1 Query Results JSON Format](https://www.w3.org/TR/sparql11-results-json/):

```json
{
  "head": {"vars": ["problemid", "text"]},
  "results": {
    "bindings": [
      {
        "problemid": {"type": "literal", "value": "lv-amo-2003-1"},
        "text":      {"type": "literal", "value": "..."}
      }
    ]
  }
}
```

All SELECT queries currently in the app return tabular bindings of this
shape, so existing parsing code in the blueprints needs no changes.

## Production deployment notes

For an Ubuntu server, the same workflow applies:

1. `pip install pyoxigraph` in the prod venv.
2. Pick a stable store path (e.g. `/var/lib/eliozo/oxigraph_db`) and set
   `OXIGRAPH_DB_PATH` in the systemd unit / `.env`.
3. Run the loader once to import data.
4. Restart the Flask app.

The store is opened in **read-only** mode by the Flask process
(`Store.read_only(...)`), so the loader can be re-run while a fresh
deployment is being prepared in a different directory and then swapped in
via env var or a symlink.

## Removing Fuseki / Tomcat

After confirming the app works against oxigraph you can safely:

- Stop and uninstall the Tomcat service that hosted Fuseki.
- Delete the `jena-fuseki-war-*` deployment.
- Remove any port-9080 nginx / firewall rules.

No code in this repo references Fuseki any more.
