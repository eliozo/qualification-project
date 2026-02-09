
import os
import sys

# Add project root and eliozoapp/eliozo to sys.path
sys.path.append(os.getcwd())
sys.path.append(os.path.join(os.getcwd(), 'eliozoapp', 'eliozo'))

from flask import Flask
from webmd_utils import get_cached_book_content

def mock_app():
    app = Flask(__name__)
    app.config['USE_REMOTE_STATIC'] = False
    app.config['SERVER_NAME'] = 'localhost'
    return app

if __name__ == "__main__":
    # Mock environment and app context
    os.environ['PROBLEMBASE_ROOT'] = '/Users/kapsitis/workspace-public/math/problembase/BOOK.BBK'
    
    app = mock_app()
    
    with app.app_context():
        print("Running get_cached_book_content...")
        content = get_cached_book_content('bbk2012-part1', os.environ['PROBLEMBASE_ROOT'])
        
        if content.startswith("ERROR"):
            print(content)
        else:
            print("Success! Content length:", len(content))
            print("First 500 chars:")
            print(content[:500])
            
            # Verify cache file creation
            cache_path = os.path.join(app.static_folder, 'books', 'bbk2012-part1.html')
            if os.path.exists(cache_path):
                print(f"Cache file created at: {cache_path}")
            else:
                print(f"Cache file NOT found at: {cache_path}")
