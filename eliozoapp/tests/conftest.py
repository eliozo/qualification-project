"""Shared pytest fixtures for the Eliozo test suite.

Provides a ``hermetic_store`` fixture that injects an in-memory pyoxigraph
store, pre-loaded with a tiny TTL fixture. Tests that use this fixture do
not depend on the user's on-disk RDF data load, so they run anywhere.

Also injects the ``eliozoapp`` source root onto ``sys.path`` so tests can
be invoked from any working directory.
"""

import os
import sys

import pytest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)


FIXTURE_TTL = """
@prefix rdf:    <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs:   <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos:   <http://www.w3.org/2004/02/skos/core#> .
@prefix eliozo: <http://www.dudajevagatve.lv/eliozo#> .

# --- Olympiads --------------------------------------------------------------
eliozo:LV.AMO a eliozo:Olympiad ;
    eliozo:olympiadCountry "LV" ;
    eliozo:olympiadCode "AMO" ;
    eliozo:olympiadName "Atklātā matemātikas olimpiāde"@lv ;
    eliozo:olympiadDescription "Atklātā matemātikas olimpiāde"@lv .

eliozo:LV.NOL a eliozo:Olympiad ;
    eliozo:olympiadCountry "LV" ;
    eliozo:olympiadCode "NOL" ;
    eliozo:olympiadName "Latvian Open Olympiad"@en ;
    eliozo:olympiadDescription "Latvian Open Olympiad"@en .

# --- Topics (wizard requires L3=L4=L5=0) -----------------------------------
eliozo:Algebra a eliozo:Topic ;
    skos:prefLabel "Algebra" ;
    eliozo:topicID "ALG" ;
    eliozo:topicNumber "1" ;
    eliozo:topicName "Algebra" ;
    eliozo:topicDescription "Algebra topics" ;
    eliozo:sorter_L1 1 ; eliozo:sorter_L2 0 ;
    eliozo:sorter_L3 0 ; eliozo:sorter_L4 0 ; eliozo:sorter_L5 0 .

eliozo:Geometry a eliozo:Topic ;
    skos:prefLabel "Geometry" ;
    eliozo:topicID "GEO" ;
    eliozo:topicNumber "2" ;
    eliozo:topicName "Geometry" ;
    eliozo:topicDescription "Geometry topics" ;
    eliozo:sorter_L1 2 ; eliozo:sorter_L2 0 ;
    eliozo:sorter_L3 0 ; eliozo:sorter_L4 0 ; eliozo:sorter_L5 0 .

# --- Sources ---------------------------------------------------------------
eliozo:src.amo a eliozo:Source ;
    eliozo:sourceLabel "AMO" ;
    eliozo:sourceName "Atklātā matemātikas olimpiāde"@lv ;
    eliozo:sourceDescription "Open Math Olympiad of Latvia"@lv ;
    eliozo:sourceUrl "https://example.org/amo" .

# --- Problem with video bookmarks -----------------------------------------
eliozo:LV.AMO.2011.5.1 a eliozo:Problem ;
    eliozo:problemID "LV.AMO.2011.5.1" ;
    eliozo:country "LV" ;
    eliozo:olympiadCode "AMO" ;
    eliozo:problemYear 2011 ;
    eliozo:problemGrade 5 ;
    eliozo:problemTimeID "2011-spring" ;
    eliozo:problemTextHtml "<p>Test problem</p>" ;
    eliozo:problemText "Test problem" ;
    eliozo:topic eliozo:Algebra ;
    eliozo:hasVideo eliozo:vid1 .

eliozo:vid1 a eliozo:Video ;
    eliozo:videoTitle "AMO2011, 5.klases 1.uzdevums" ;
    eliozo:videoYoutube "tWx-UGFeuSA" ;
    eliozo:videoBookmarks eliozo:vid1.bms .

eliozo:vid1.bms rdf:_1 eliozo:vid1.bm1 ;
                rdf:_2 eliozo:vid1.bm2 .

eliozo:vid1.bm1 eliozo:videoBookmarkTstamp 5 ;
                eliozo:videoBookmarkText "Uzdevuma saprašana" .

eliozo:vid1.bm2 eliozo:videoBookmarkTstamp 45 ;
                eliozo:videoBookmarkText "Kādēļ pilnā pārlase neder" .
"""


@pytest.fixture
def hermetic_store(monkeypatch):
    """Replace eliozo_dao's lazy singleton store with an in-memory store
    loaded from FIXTURE_TTL. Each test gets a fresh store.
    """
    from pyoxigraph import RdfFormat, Store

    import eliozo_dao

    store = Store()
    store.load(input=FIXTURE_TTL, format=RdfFormat.TURTLE)

    monkeypatch.setattr(eliozo_dao, "_store", store, raising=False)
    yield store
