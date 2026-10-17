"""Loading of the PostgreSQL / OpenAI settings from a dotenv file.

Kept apart from ``db`` so that ``create_app`` can call it with only
python-dotenv installed: an app without the PostgreSQL libraries still starts,
and only search by meaning reports that it is unavailable.
"""

import os

from dotenv import load_dotenv


def load_environment():
    """Load the dotenv file named by ELIOZO_ENV_FILE, if any, over the environment.

    Returns the path of the loaded file, or None.
    """
    path = os.environ.get('ELIOZO_ENV_FILE')
    if path and os.path.isfile(path):
        load_dotenv(path, override=True)
        return path
    return None
