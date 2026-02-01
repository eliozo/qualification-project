@echo off

REM Check if VIRTUAL_ENV is set
IF NOT DEFINED VIRTUAL_ENV (
    IF EXIST "..\venv-eliozo\Scripts\activate.bat" (
        call "..\venv-eliozo\Scripts\activate.bat"
    ) ELSE (
        echo Error: Virtual environment not found at ..\venv-eliozo
        pause
        exit /b 1
    )
)

set FLASK_APP=eliozo
set FLASK_ENV=development
flask run

REM Keep the window open and environment active
cmd /k
