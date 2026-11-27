"""Run the SPARQL endpoint locally, without Gunicorn (Windows, macOS, Linux).

    python -m sparql_endpoint [--host 127.0.0.1] [--port 5001]

Run it from ``eliozoapp``. It serves the store in ``OXIGRAPH_DB_PATH`` (or
``eliozoapp/data/oxigraph_db``) at http://127.0.0.1:5001/sparql. There is no
hard query timeout here; that is Gunicorn's job on the server.
"""

import argparse
from wsgiref.simple_server import make_server

from .app import create_app


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--host', default='127.0.0.1')
    parser.add_argument('--port', type=int, default=5001)
    args = parser.parse_args()
    app = create_app()
    print(f'store: {app.settings.store_path}')
    print(f'SPARQL endpoint: http://{args.host}:{args.port}{app.settings.path_prefix}')
    with make_server(args.host, args.port, app) as server:
        server.serve_forever()


if __name__ == '__main__':
    main()
