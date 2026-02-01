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

# To ensure the environment stays active after termination if the script was not dot-sourced
if ($MyInvocation.CommandOrigin -eq 'Runspace') {
   # Script was run directly (not dot-sourced)
   Write-Host "Flask process terminated."
   Write-Host "Entering nested shell to maintain virtual environment..."
   # Spawn a new interactive PowerShell session which inherits the current environment (including venv)
   powershell
}
