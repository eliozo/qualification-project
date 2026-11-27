# sparql_endpoint — read-only SPARQL 1.1 endpoint

A small WSGI application (no Flask) that serves the Eliozo Oxigraph store over
the [SPARQL 1.1 Protocol](https://www.w3.org/TR/sparql11-protocol/), for tools
such as YASGUI, ViziQuer and Sampo-UI.

Public URL: **https://eliozo.dudajevagatve.lv/sparql**. On the server it runs
as its own systemd unit, `eliozo-sparql` (Gunicorn), separate from the Flask
site. Setup and maintenance: `eliozo-setup/REQUEST022-sparql-endpoint.md` and
the *SPARQL Endpoint* section of `eliozo-setup/ADMIN-GUIDE.md`.

## What it does

| URL | |
|---|---|
| `GET /sparql?query=…`, `POST /sparql` (form or `application/sparql-query`) | SELECT, ASK, CONSTRUCT, DESCRIBE; `default-graph-uri` / `named-graph-uri` are honoured |
| `GET /sparql` without a query | SPARQL Service Description (Turtle, N-Triples, RDF/XML, JSON-LD); a short help page for browsers |
| `GET /sparql/void` | VoID description: triples, classes and properties with counts |
| `GET /sparql/graph?default` or `?graph=<IRI>` | read-only Graph Store Protocol |
| `GET /sparql/health` | JSON status for monitoring |

Results: `application/sparql-results+json` (default), `+xml`, `text/csv`,
`text/tab-separated-values`. Graphs: `text/turtle` (default),
`application/n-triples`, `application/rdf+xml`, `application/ld+json`. The format
follows the `Accept` header; a `format=json|xml|csv|tsv|turtle|nt|rdfxml|jsonld`
parameter overrides it.

## What it refuses

* **Updates** (`update=`, `application/sparql-update`, `INSERT`, `DROP`, …) → 400.
  The store is also opened read-only.
* **`SERVICE`** (federated queries) → 400, because the store would send HTTP
  requests to whatever address a query names. On the server the systemd unit
  also has no network at all (`PrivateNetwork=yes`, `IPAddressDeny=any`,
  `RestrictAddressFamilies=AF_UNIX`), so even an undetected `SERVICE` cannot
  reach anything.
* Queries longer than `SPARQL_MAX_QUERY_LENGTH` and bodies larger than
  `SPARQL_MAX_REQUEST_BYTES` → 413.

## Limits

All set by environment variables (see `config.py`); on the server in
`/etc/eliozo/sparql.env`.

* **Rows / triples:** at most `SPARQL_MAX_ROWS` / `SPARQL_MAX_TRIPLES`; a cut-off
  response has the headers `X-SPARQL-Truncated: true` and `X-SPARQL-Limit: N`.
* **Time:** a query still producing results after `SPARQL_QUERY_TIMEOUT` seconds
  gets 503. A query stuck before its first row (e.g. sorting a huge cross
  product) cannot be interrupted from Python, so Gunicorn kills the worker
  10 s later (`gunicorn_conf.py`) and Nginx answers 503.
* **Rate and size per IP**, **gzip** and **CORS on Nginx errors** are set in Nginx
  (`eliozo-setup/scripts/setup-sparql-endpoint.sh`).

## Data reloads

The `load_rdf` Jenkins pipeline deletes and rebuilds the store while the
service runs. `store.StoreHolder` notices the rebuilt store and reopens it once
no process holds the writer lock and the files have not changed for
`SPARQL_RELOAD_SETTLE` seconds. Until then the old data is served. No restart
is needed.

## Running it locally

```bash
cd qualification-project/eliozoapp
python -m sparql_endpoint            # http://127.0.0.1:5001/sparql
python -m pytest tests/test_sparql_endpoint.py
```

It uses the store in `OXIGRAPH_DB_PATH` (default `eliozoapp/data/oxigraph_db`).
On Linux you can also run it as on the server:

```bash
SPARQL_BIND=127.0.0.1:5001 gunicorn -c sparql_endpoint/gunicorn_conf.py sparql_endpoint.app:application
```

## Logs

Each query is logged twice to stderr (journald on the server): a `query` line
with its text before it runs, and a `done` line with status, row count and
time. A query that has a `query` line but no `done` line with the same `sha`
was killed by the hard timeout.
