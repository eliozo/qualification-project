import sys
import os
from unittest.mock import MagicMock
import re

# Mock flask and flask_babel
sys.modules['flask'] = MagicMock()
sys.modules['flask_babel'] = MagicMock()

sys.path.append(os.getcwd())

try:
    from eliozoapp.eliozo.webmd_utils import proc_markdown
except ImportError:
    sys.path.append(os.path.join(os.getcwd(), '..', '..'))
    from eliozoapp.eliozo.webmd_utils import proc_markdown

path = 'eliozoapp/eliozo/static/books/bbk2012-part1/content_lv.md'
if not os.path.exists(path):
    print(f"File not found: {path}")
    sys.exit(1)

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Test lines near the user example (around line 1-100)
chunk_lines = lines[0:50]
chunk = "".join(chunk_lines)

print(f"Processing chunk lines 0-50...")
html = proc_markdown(chunk)

print("HTML Output Snippet:")
print(html[:1000])

if "<h1>1.Daļa: SKAITĻU DALĀMĪBA</h1>" in html:
    print("\nSUCCESS: Header found.")
else:
    print("\nFAILURE: Header NOT found.")

# Check for mangled formulas
if r"\(m\)" in html or r"\(n\)" in html:
     print("SUCCESS: Inline math seems to be preserved.")
else:
     print("FAILURE: Inline math not found in expected format.")

# Check for leftover placeholders (should not happen if replaced correctly)
if "LATEX_PH" in html:
    print("FAILURE: Found leftover placeholder 'LATEX_PH' in output.")
else:
     print("SUCCESS: No leftover placeholders found.")
