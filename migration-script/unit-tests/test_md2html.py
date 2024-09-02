import os
import sys

#import rdflib
#from rdflib.namespace import Namespace
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from mdchunk_reader import *

PROB_LV_NOL_2015_12_5 = ""

# @pytest.fixture
# def readVars():
#     global PROB_LV_NOL_2015_12_5
#     file_path = 'test_data/LV.NOL.2015.12.5.md'
#     # Open the file in read mode and read its content into a variable
#     with open(file_path, 'r', encoding='UTF-8') as file:
#         PROB_LV_NOL_2015_12_5 = file.read()

@pytest.fixture
def readDD():
    dd = dict()
    probs = ['LV.NOL.2015.12.5']
    for probID in probs: 
        file_path = f'test_data/{probID}.md'
        with open(file_path, 'r', encoding='UTF-8') as file:
            dd[probID] = file.read()
    return dd


def test_dummy(readDD):
    assert 2==1+1
    p = readDD['LV.NOL.2015.12.5']
    assert len(p) > 0
    prob = extract_problem(p).strip()
    assert prob.startswith("Vai eksistē")
    assert prob.endswith("$2015$?")

