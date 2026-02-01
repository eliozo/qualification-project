#!/bin/bash

# Check if VIRTUAL_ENV is set
if [[ -z "$VIRTUAL_ENV" ]]; then
    if [[ -f "../venv-eliozo/bin/activate" ]]; then
        source "../venv-eliozo/bin/activate"
    else
        echo "Error: Virtual environment not found at ../venv-eliozo"
        exit 1
    fi
fi

export FLASK_APP=eliozo
export FLASK_ENV=development
flask run

# If the script is executed (not sourced), spawn a shell to keep the venv active
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
    echo "Flask process terminated. Spawning new shell to keep virtual environment active."
    exec $SHELL
fi