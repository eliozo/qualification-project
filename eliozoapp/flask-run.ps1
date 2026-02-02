# Check if VIRTUAL_ENV is set
if (-not $env:VIRTUAL_ENV) {
    if (Test-Path "..\venv-eliozo\Scripts\Activate.ps1") {
        . "..\venv-eliozo\Scripts\Activate.ps1"
    } else {
        Write-Error "Virtual environment not found at ..\venv-eliozo"
        exit 1
    }
}

$env:FLASK_APP = "eliozo"
$env:FLASK_ENV = "development"
flask run

