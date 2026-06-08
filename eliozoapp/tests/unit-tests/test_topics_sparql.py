"""Tests for the topics/wizard queries against the embedded oxigraph store."""

import json

from eliozo_dao.indexes_repository import (
    getAllTopicsTableSPARQL,
    getSPARQLtopics,
    getWizardTopicsSPARQL,
)


def test_wizard_topics_response_shape(hermetic_store):
    """The wizard query should return valid SPARQL JSON with the expected vars."""
    response_text = getWizardTopicsSPARQL()
    data = json.loads(response_text)

    assert "head" in data and "vars" in data["head"]
    assert "results" in data and "bindings" in data["results"]

    expected_vars = {"topicIdentifier", "topicNumber",
                     "topicDescription", "topicName", "L1", "L2"}
    assert set(data["head"]["vars"]) == expected_vars


def test_wizard_topics_returns_top_level_categories_only(hermetic_store):
    """The wizard query filters to L3=L4=L5=0 (top-level categories only)."""
    response_text = getWizardTopicsSPARQL()
    bindings = json.loads(response_text)["results"]["bindings"]
    assert len(bindings) == 2, "fixture has two top-level topics"
    for item in bindings:
        # Wizard FILTER drops anything where L3/L4/L5 are non-zero
        assert int(item["L2"]["value"]) == 0


def test_all_topics_table_returns_full_hierarchy(hermetic_store):
    """getAllTopicsTableSPARQL has no L3/L4/L5 filter, so it returns
    everything the topic queries are designed to return."""
    response_text = getAllTopicsTableSPARQL()
    bindings = json.loads(response_text)["results"]["bindings"]
    assert len(bindings) == 2
    names = {b["topicName"]["value"] for b in bindings}
    assert names == {"Algebra", "Geometry"}


def test_get_topics_returns_distinct_rows(hermetic_store):
    """getSPARQLtopics uses SELECT DISTINCT; with one Topic the count is 1
    even though OPTIONAL would otherwise multiply rows."""
    response_text = getSPARQLtopics()
    bindings = json.loads(response_text)["results"]["bindings"]
    # Two distinct topics in the fixture, each with a single (or zero) problem
    topic_ids = {b["topicIdentifier"]["value"] for b in bindings}
    assert topic_ids == {"ALG", "GEO"}
