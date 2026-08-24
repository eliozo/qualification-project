# Run the Eliozo Flask app locally (Windows / PowerShell).
#
# The app reads its RDF data from an embedded pyoxigraph store whose location
# comes from OXIGRAPH_DB_PATH. If that variable is not set in the environment,
# fall back to the default store location under eliozoapp/data/oxigraph_db.
# Build/refresh the store with:  python -m eliozo_dao.load_rdf

Set-Location $PSScriptRoot

# Check if VIRTUAL_ENV is set
if (-not $env:VIRTUAL_ENV) {
    if (Test-Path "..\venv-eliozo\Scripts\Activate.ps1") {
        . "..\venv-eliozo\Scripts\Activate.ps1"
    } else {
        Write-Error "Virtual environment not found at ..\venv-eliozo"
        exit 1
    }
}

if (-not $env:OXIGRAPH_DB_PATH) {
    $env:OXIGRAPH_DB_PATH = Join-Path $PSScriptRoot "data\oxigraph_db"
}

if (-not (Test-Path $env:OXIGRAPH_DB_PATH)) {
    Write-Error @"
Oxigraph store not found at $($env:OXIGRAPH_DB_PATH)
Build it first:
    python -m eliozo_dao.load_rdf
"@
    exit 1
}

Write-Host "OXIGRAPH_DB_PATH = $($env:OXIGRAPH_DB_PATH)"

$env:FLASK_APP = "eliozo"
$env:FLASK_ENV = "development"
# Use "python -m flask" rather than the flask.exe shim: this venv was created
# under a different path, so the console-script .exe wrappers still point at an
# interpreter that no longer exists and fail silently with exit code 1.
python -m flask run
