"""Check that PostgreSQL is reachable and migrated; optionally start it.

    python -m eliozo_dao.postgres.check           # check only
    python -m eliozo_dao.postgres.check --start   # also try `docker compose up`

The ``flask-run.*`` scripts call this with ``--start`` before starting Flask
and stop if it exits non-zero. ``--start`` only starts a database that is run
by Docker Compose: a ``docker-compose.yml`` in ELIOZO_DB_COMPOSE_DIR, or else
next to the ELIOZO_ENV_FILE. A system-managed PostgreSQL (the Ubuntu server)
is never started from here; a reminder is printed instead.
"""

import argparse
import os
import shutil
import subprocess
import sys
import time

from sqlalchemy import create_engine, text

from .db import CONNECT_TIMEOUT, database_url, load_environment, missing_settings

# Seconds to wait for a freshly started container to accept connections.
STARTUP_WAIT = 60


def _probe():
    """None if the database is ready for the app, else a description of what is wrong."""
    engine = create_engine(database_url(), connect_args={'connect_timeout': CONNECT_TIMEOUT})
    try:
        with engine.connect() as conn:
            tables = set(conn.execute(text(
                "SELECT table_name FROM information_schema.tables "
                "WHERE table_schema = current_schema()")).scalars())
            if not {'problems', 'solution_chunks'} <= tables:
                return ('schema', 'the tables problems / solution_chunks do not exist')
            counts = conn.execute(text(
                "SELECT (SELECT count(*) FROM problems), (SELECT count(*) FROM solution_chunks)")).one()
            return ('ok', '%d problems, %d solution chunks' % tuple(counts))
    except Exception as e:
        # psycopg puts the useful part ("connection refused" etc.) on the last line.
        return ('down', str(getattr(e, 'orig', e)).strip().splitlines()[-1])
    finally:
        engine.dispose()


def _compose_dir():
    configured = os.environ.get('ELIOZO_DB_COMPOSE_DIR')
    if configured:
        return configured
    envFile = os.environ.get('ELIOZO_ENV_FILE')
    return os.path.dirname(os.path.abspath(envFile)) if envFile else None


def _start_with_compose(composeDir):
    print('PostgreSQL is not running; starting it: docker compose up -d (in %s)' % composeDir, flush=True)
    try:
        subprocess.run(['docker', 'compose', 'up', '-d'], cwd=composeDir, check=True)
    except (OSError, subprocess.CalledProcessError) as e:
        print('Could not start the container: %s' % e)
        return False
    return True


def _where():
    return 'DB_HOST=%s DB_PORT=%s DB_NAME=%s' % tuple(
        os.environ.get(n, '?') for n in ('DB_HOST', 'DB_PORT', 'DB_NAME'))


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--start', action='store_true',
                        help='start the Docker Compose database if it is not running')
    args = parser.parse_args(argv)

    envFile = load_environment()
    missing = missing_settings()
    if missing:
        print('PostgreSQL settings missing: %s' % ', '.join(missing))
        print('Set them in the environment, or point ELIOZO_ENV_FILE at a dotenv file '
              '(currently: %s).' % (os.environ.get('ELIOZO_ENV_FILE') or 'not set'))
        return 2

    status, detail = _probe()
    if status == 'down' and args.start:
        composeDir = _compose_dir()
        if (composeDir and os.path.isfile(os.path.join(composeDir, 'docker-compose.yml'))
                and shutil.which('docker') and _start_with_compose(composeDir)):
            deadline = time.monotonic() + STARTUP_WAIT
            while status == 'down' and time.monotonic() < deadline:
                time.sleep(2)
                status, detail = _probe()

    if status == 'ok':
        print('PostgreSQL OK (%s): %s' % (_where(), detail))
        return 0
    if status == 'schema':
        print('PostgreSQL is running (%s) but %s.' % (_where(), detail))
        print('Create the schema:  cd eliozo-db && python -m alembic upgrade head')
        return 1

    print('PostgreSQL is not reachable (%s): %s' % (_where(), detail))
    print('Settings from: %s' % (envFile or 'the process environment'))
    print('Start it first, then run this script again:')
    print('  Docker (workstation):  cd eliozo-db && docker compose up -d'
          '   (on macOS start colima first: colima start)')
    print('  System service (Ubuntu):  sudo systemctl start postgresql')
    return 1


if __name__ == '__main__':
    sys.exit(main())
