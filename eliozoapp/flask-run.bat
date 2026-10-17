@echo off
REM Run the Eliozo Flask app locally (Windows / cmd.exe).
REM
REM The app reads its RDF data from an embedded pyoxigraph store whose location
REM comes from OXIGRAPH_DB_PATH. If that variable is not set in the environment,
REM fall back to the default store location under eliozoapp\data\oxigraph_db.
REM Build/refresh the store with:  python -m eliozo_dao.load_rdf

cd /d "%~dp0"

IF NOT DEFINED VIRTUAL_ENV (
    IF EXIST "..\venv-eliozo\Scripts\activate.bat" (
        call "..\venv-eliozo\Scripts\activate.bat"
    ) ELSE (
        echo Error: Virtual environment not found at ..\venv-eliozo
        pause
        exit /b 1
    )
)

IF NOT DEFINED OXIGRAPH_DB_PATH set "OXIGRAPH_DB_PATH=%~dp0data\oxigraph_db"

IF NOT EXIST "%OXIGRAPH_DB_PATH%" (
    echo Error: Oxigraph store not found at %OXIGRAPH_DB_PATH%
    echo Build it first:  python -m eliozo_dao.load_rdf
    pause
    exit /b 1
)

echo OXIGRAPH_DB_PATH = %OXIGRAPH_DB_PATH%

REM Search by meaning uses PostgreSQL + pgvector and the OpenAI API. Their
REM settings (DB_*, OPENAI_API_KEY) are read from this dotenv file; it overrides
REM settings in the environment.
IF NOT DEFINED ELIOZO_ENV_FILE set "ELIOZO_ENV_FILE=%~dp0..\..\eliozo-db\.env"

REM Make sure PostgreSQL is up; starts the eliozo-db Docker container if needed,
REM otherwise explains how to start the database and stops here.
python -m eliozo_dao.postgres.check --start
IF ERRORLEVEL 1 (
    pause
    exit /b 1
)

set FLASK_APP=eliozo
set FLASK_ENV=development
REM Use "python -m flask" rather than the flask.exe shim: this venv was created
REM under a different path, so the console-script .exe wrappers still point at
REM an interpreter that no longer exists and fail silently with exit code 1.
python -m flask run
