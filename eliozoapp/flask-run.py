import os
import subprocess
import sys

# Setting the environment variables
os.environ['FLASK_APP'] = 'eliozo'
os.environ['FLASK_ENV'] = 'development'
# PostgreSQL / OpenAI settings for search by meaning (see flask-run.sh)
os.environ.setdefault('ELIOZO_ENV_FILE', os.path.join(
    os.path.dirname(os.path.abspath(__file__)), '..', '..', 'eliozo-db', '.env'))

# Make sure PostgreSQL is up before starting Flask
if subprocess.run([sys.executable, '-m', 'eliozo_dao.postgres.check', '--start']).returncode != 0:
    sys.exit(1)

# Running the Flask application
os.system('flask run')
