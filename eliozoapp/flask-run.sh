#!/bin/bash
# Run the Eliozo Flask app locally (macOS / Linux).
#
# The app reads its RDF data from an embedded pyoxigraph store whose location
# comes from OXIGRAPH_DB_PATH. If that variable is not set in the environment,
# fall back to the default store location under eliozoapp/data/oxigraph_db.
# Build/refresh the store with:  python -m eliozo_dao.load_rdf

cd "$(dirname "$0")" || exit 1

# Check if VIRTUAL_ENV is set
if [[ -z "$VIRTUAL_ENV" ]]; then
    if [[ -f "../venv-eliozo/bin/activate" ]]; then
        source "../venv-eliozo/bin/activate"
    else
        echo "Error: Virtual environment not found at ../venv-eliozo"
        exit 1
    fi
fi

: "${OXIGRAPH_DB_PATH:=$PWD/data/oxigraph_db}"
export OXIGRAPH_DB_PATH

if [[ ! -d "$OXIGRAPH_DB_PATH" ]]; then
    echo "Error: Oxigraph store not found at $OXIGRAPH_DB_PATH"
    echo "Build it first:  python -m eliozo_dao.load_rdf"
    exit 1
fi

echo "OXIGRAPH_DB_PATH = $OXIGRAPH_DB_PATH"

export FLASK_APP=eliozo
export FLASK_ENV=development
# Use "python -m flask" rather than the flask console script: a relocated venv
# keeps an absolute interpreter path in its bin/ wrappers and they then fail.
python -m flask run
