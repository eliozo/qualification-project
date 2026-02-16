
import json
import os
import pytest
from eliozo_dao.problem_repository import getSPARQLVideoBookmarks

def test_get_video_bookmarks():
    # Use environment variables if set, otherwise rely on default
    # This test assumes a running Fuseki instance or appropriate mocking, 
    # but as requested, it calls the real function.
    
    video_bookmarks_json = getSPARQLVideoBookmarks("LV.AMO.2011.5.1")
    video_bookmarks = json.loads(video_bookmarks_json)
    
    # Expected structure verification
    assert "head" in video_bookmarks
    assert "vars" in video_bookmarks["head"]
    assert video_bookmarks["head"]["vars"] == ["problem", "youtubeID", "videoTitle", "tstamp", "bmtext"]
    
    assert "results" in video_bookmarks
    assert "bindings" in video_bookmarks["results"]
    
    bindings = video_bookmarks["results"]["bindings"]
    assert len(bindings) == 8 # Verify total count as requested
    
    # Verify the first two items as specified in the request
    # Note: The order returned by SPARQL is by ?tstamp (ORDER BY ?tstamp in the query)
    # The example provided shows tstamp 5 then 45, which matches the order.
    
    item1 = bindings[0]
    assert item1["problem"]["value"] == "http://www.dudajevagatve.lv/eliozo#LV.AMO.2011.5.1"
    assert item1["youtubeID"]["value"] == "tWx-UGFeuSA"
    assert item1["videoTitle"]["value"] == "AMO2011, 5.klases 1.uzdevums"
    assert item1["tstamp"]["value"] == "5"
    assert item1["bmtext"]["value"] == "Uzdevuma saprašana: Piemērā abi reizinātāji ir īsti divciparu skaitļi."
    
    item2 = bindings[1]
    assert item2["problem"]["value"] == "http://www.dudajevagatve.lv/eliozo#LV.AMO.2011.5.1"
    assert item2["youtubeID"]["value"] == "tWx-UGFeuSA"
    assert item2["videoTitle"]["value"] == "AMO2011, 5.klases 1.uzdevums"
    assert item2["tstamp"]["value"] == "45"
    assert item2["bmtext"]["value"] == "Uzdevuma saprašana: Kādēļ pilnā pārlase neder."
