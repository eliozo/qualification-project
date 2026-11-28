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
  reach anything. To allow federated queries, see
  [Federated queries (`SERVICE`): off or on](#federated-queries-service-off-or-on).
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

## Federated queries (`SERVICE`): off or on

Federated queries are **off** by default. Unlike the limits above, this is not
an environment variable in `config.py`. Two separate layers block `SERVICE`,
and each one is enough to stop it on its own:

| Layer | Where | Effect |
|---|---|---|
| 1. Query check | `check_query()` in `protocol.py` | Any query with the `SERVICE` keyword gets 400 before it reaches the store |
| 2. No network | The `eliozo-sparql` systemd unit, written by `eliozo-setup/scripts/setup-sparql-endpoint.sh` (`PrivateNetwork=yes`, `IPAddressDeny=any`, `RestrictAddressFamilies=AF_UNIX`) | The service process cannot open any connection except its Unix socket |

To check the current state on the server:

```bash
systemctl show eliozo-sparql -p PrivateNetwork -p IPAddressDeny -p RestrictAddressFamilies
systemctl cat eliozo-sparql      # also shows drop-ins (see below), if any
curl -s https://eliozo.dudajevagatve.lv/sparql \
     --data-urlencode 'query=SELECT * WHERE { SERVICE <http://example.org/sparql> { ?s ?p ?o } }'
# off: "SERVICE (federated query) is not allowed on this endpoint."
```

### Before you turn it on

With `SERVICE` allowed, anyone on the internet can make the server send HTTP
requests to any address they name. That includes addresses only the server can
reach: `prog-validate` on `127.0.0.1:8001`, the Flask site, and the cloud
metadata service at `169.254.169.254`. So:

* Prefer an **allow-list** of the remote endpoints you actually need
  (option B below) over opening the network completely (option A).
* Time spent waiting on a remote endpoint counts against
  `SPARQL_QUERY_TIMEOUT` (soft) and the Gunicorn hard timeout. A slow remote
  endpoint can therefore tie up one of the two workers for up to about 30 s.
  Consider lowering the Nginx request rate at the same time
  (`sudo RATE=2r/s bash scripts/setup-sparql-endpoint.sh --skip-pip`).

### Turning it on

Both layers must be changed. Changing only one still leaves `SERVICE` blocked.

**1. Remove the query check (code).** In `sparql_endpoint/protocol.py`, function
`check_query()`, delete the two lines

```python
    if 'SERVICE' in words:
        raise ProtocolError(400, 'SERVICE (federated query) is not allowed on this endpoint.')
```

Then update the places that tell users `SERVICE` is refused:

* the help page in `app.py`: search for `SERVICE`;
* the Service Description text in `description.py`;
* `test_service_is_refused` in `tests/test_sparql_endpoint.py`, which should
  now expect the query to pass the check.

Commit, push and run the `deploy_eliozo` pipeline with `*/main`. Editing the
live tree by hand does not last, because the next deploy overwrites it.

**2. Give the service network access (systemd).** Do not edit
`/etc/systemd/system/eliozo-sparql.service`. The setup script rewrites it on
every run. Add a drop-in file instead, which the script leaves alone:

```bash
sudo systemctl edit eliozo-sparql      # creates .../eliozo-sparql.service.d/override.conf
```

*Option A: open network.* Put this in the drop-in:

```ini
[Service]
PrivateNetwork=no
# An empty assignment clears the list from the main unit.
IPAddressDeny=
RestrictAddressFamilies=
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6 AF_NETLINK
# Still keep the metadata service and the local services out of reach.
IPAddressDeny=169.254.0.0/16 localhost
IPAddressAllow=127.0.0.53
```

`127.0.0.53` is the local DNS resolver (systemd-resolved). Without it, host
names in `SERVICE <…>` cannot be resolved.

*Option B: allow-list (recommended).* Keep `IPAddressDeny=any` from the main
unit and allow only the resolver and the remote endpoints' addresses:

```ini
[Service]
PrivateNetwork=no
RestrictAddressFamilies=
RestrictAddressFamilies=AF_UNIX AF_INET AF_INET6 AF_NETLINK
IPAddressAllow=127.0.0.53
# One line per remote endpoint, e.g. for query.wikidata.org:
#   getent ahosts query.wikidata.org
IPAddressAllow=203.0.113.10 2001:db8::10
```

Remote endpoints that change address (CDNs) will stop working until the list
is updated.

Then apply it:

```bash
sudo systemctl daemon-reload
sudo systemctl restart eliozo-sparql
```

**3. Expect two smoke-test failures.** After this change,
`setup-sparql-endpoint.sh` reports *"SERVICE is refused"* and *"no network
inside the service"* as FAILED, because both checks test that federation is
off. That is expected while federation is on. The other checks must still
pass.

### Turning it off again

```bash
sudo rm -r /etc/systemd/system/eliozo-sparql.service.d   # or delete only the network lines
sudo systemctl daemon-reload
sudo systemctl restart eliozo-sparql
```

Then restore the check in `protocol.py`, along with its texts and test, and
deploy. Re-running `setup-sparql-endpoint.sh` afterwards should pass all its
checks again.

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
