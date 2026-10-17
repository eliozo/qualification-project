#!/usr/bin/env python3
"""Start the Eliozo Flask app for local development (Windows, macOS, Linux).

    python flask-run.py                  # http://127.0.0.1:5000 (5001 on macOS)
    python flask-run.py --port 5002      # any other `flask run` options
    python flask-run.py --debug          # auto-reload + debugger

Run it with the Python of a virtual environment that has the app's packages
(``pip install -r requirements.txt``); the working directory does not matter.

Before Flask starts:

1. OXIGRAPH_DB_PATH defaults to ``data/oxigraph_db`` and must exist (build it
   with ``python -m eliozo_dao.load_rdf``).
2. ELIOZO_ENV_FILE defaults to ``../../eliozo-db/.env``: the PostgreSQL
   settings and OPENAI_API_KEY for search by meaning. The file overrides
   variables already in the environment.
3. PostgreSQL must be reachable; if it is not, its eliozo-db Docker container
   is started, or the script explains how to start the database and stops
   (``python -m eliozo_dao.postgres.check --start``).
"""

import os
import platform
import subprocess
import sys

APP_DIR = os.path.dirname(os.path.abspath(__file__))


def main():
    os.chdir(APP_DIR)
    os.environ.setdefault('OXIGRAPH_DB_PATH', os.path.join(APP_DIR, 'data', 'oxigraph_db'))
    os.environ.setdefault('ELIOZO_ENV_FILE', os.path.normpath(
        os.path.join(APP_DIR, '..', '..', 'eliozo-db', '.env')))
    os.environ['FLASK_APP'] = 'eliozo'
    # macOS AirPlay Receiver occupies port 5000.
    if platform.system() == 'Darwin':
        os.environ.setdefault('FLASK_RUN_PORT', '5001')

    try:
        import flask  # noqa: F401
    except ImportError:
        print('Flask is not installed for %s.\nActivate the project virtual environment '
              '(or run this script with its python) and install requirements.txt.' % sys.executable)
        return 1

    store = os.environ['OXIGRAPH_DB_PATH']
    print('OXIGRAPH_DB_PATH = %s' % store)
    if not os.path.isdir(store):
        print('Error: Oxigraph store not found. Build it first:  python -m eliozo_dao.load_rdf')
        return 1

    from eliozo_dao.postgres.check import main as check_postgres
    if check_postgres(['--start']) != 0:
        return 1

    sys.stdout.flush()  # keep the messages above ahead of Flask's output

    # `python -m flask` rather than the `flask` launcher: a relocated venv's
    # launchers can point at an interpreter that no longer exists.
    try:
        return subprocess.call([sys.executable, '-m', 'flask', 'run', *sys.argv[1:]])
    except KeyboardInterrupt:
        return 0


if __name__ == '__main__':
    sys.exit(main())
