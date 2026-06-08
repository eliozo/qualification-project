# Running the test suite

These tests now run against an **in-memory pyoxigraph store** loaded with a
small TTL fixture defined in `tests/conftest.py` (the `hermetic_store`
fixture). No Fuseki/Tomcat service or SSH tunnel is required.

## Setup

1. Activate the project venv from the repo root:

   ```bash
   source venv-eliozo/bin/activate
   ```

2. Install `pytest` if needed:

   ```bash
   pip install pytest
   ```

## Running tests

From the `eliozoapp/` directory:

```bash
cd eliozoapp
pytest tests/
```

Or target a specific suite:

```bash
pytest tests/eliozo_dao/                          # repository tests
pytest tests/unit-tests/test_topics_sparql.py     # topics / wizard
pytest tests/eliozo_dao/test_oxigraph_integration.py  # adapter health
```

Add `-v` for verbose output or `-s` to see prints.

## How the fixture works

Each test that uses `hermetic_store` gets a fresh in-memory
`pyoxigraph.Store()` pre-loaded from `FIXTURE_TTL` in `tests/conftest.py`.
The fixture monkey-patches `eliozo_dao._store` so any call to
`sparql_query(...)` (and therefore any repository function) talks to the
test store rather than the on-disk one at `OXIGRAPH_DB_PATH`.

This means:

- Tests do not require `python -m eliozo_dao.load_rdf` to have been run.
- Tests do not pollute or depend on the operator's on-disk store.
- Tests run anywhere in milliseconds.

If you want a test to hit the real on-disk store instead, simply omit the
`hermetic_store` fixture from its arguments — `sparql_query` will then use
the default lazy singleton against `OXIGRAPH_DB_PATH`.
