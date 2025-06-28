import sys
import os
import pytest
import markdown

# Add the parent directory to the sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from webmd_utils import mathBeautify, extract_latex, replace_placeholders, proc_markdown

def test_underscore():
    problemText = r"""Ievērosim, ka

$$\underbrace{111\ldots{}1}_{\mbox{81 vieninieki}} = 
\underbrace{111\ldots{}1}_{\mbox{9 vieninieki}} \cdot \underbrace{100\ldots{}0100\ldots{}01}_{\mbox{9 vieninieki}}.$$

Katrs no reizinātājiem dalās ar $9$, jo ciparu summa dalās ar $9$. Tātad reizinājums dalās ar $81$."""

    # problemTextHtml = markdown.markdown(problemText, extensions=['tables']).strip()
    # problemTextHtml = mathBeautify(problemTextHtml)
    # print(problemTextHtml)
    # assert len(problemTextHtml) > 10

    # # Extract LaTeX formulas and placeholders
    # text_with_placeholders, latex_placeholders = extract_latex(problemText)
    #
    # # Apply markdown processing
    # problemTextHtml = markdown.markdown(text_with_placeholders, extensions=['tables']).strip()
    #
    # # Replace placeholders with LaTeX
    # problemTextHtml = replace_placeholders(problemTextHtml, latex_placeholders)

    problemTextHtml = proc_markdown(problemText)

    # Apply mathBeautify
    problemTextHtml = mathBeautify(problemTextHtml)

    print(problemTextHtml)
    assert len(problemTextHtml) > 10
