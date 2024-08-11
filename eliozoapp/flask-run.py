import os

# Setting the environment variables
os.environ['FLASK_APP'] = 'eliozo'
os.environ['FLASK_ENV'] = 'development'

# Running the Flask application
os.system('flask run')
