import pytest
from unittest.mock import patch, MagicMock
from eliozo_dao.indexes_repository import getWizardTopicsSPARQL
import json
import os

def test_get_wizard_topics():
    """
    Test that getWizardTopicsSPARQL returns a valid JSON response with expected fields.
    Default: Test against REAL Fuseki.
    Set USE_MOCK_FUSEKI=true env var to test with a mock response.
    """
    use_mock_fuseki = os.environ.get('USE_MOCK_FUSEKI', 'false').lower() == 'true'

    if not use_mock_fuseki:
        print("\nTesting against REAL Fuseki instance...")
        # Ensure FUSEKI_URL is reachable or this will fail.
        # We assume the user has set up the tunnel or environment as per instructions.
        response_text = getWizardTopicsSPARQL()
    else:
        print("\nTesting with MOCK Fuseki response...")
        # Mock response data
        mock_response_data = {
            "head": {"vars": ["topicIdentifier", "topicNumber", "topicDescription", "topicName", "L1", "L2"]},
            "results": {
                "bindings": [
                    {
                        "topicIdentifier": {"type": "literal", "value": "ID_1"},
                        "topicName": {"type": "literal", "value": "Algebra"},
                        "L1": {"type": "literal", "value": "1"},
                        "L2": {"type": "literal", "value": "0"}
                    },
                    {
                        "topicIdentifier": {"type": "literal", "value": "ID_2"},
                        "topicName": {"type": "literal", "value": "Linear Equations"},
                        "L1": {"type": "literal", "value": "1"},
                        "L2": {"type": "literal", "value": "1"}
                    }
                ]
            }
        }
        
        # Configure the mock
        with patch('eliozo_dao.indexes_repository.requests.post') as mock_post:
            mock_response = MagicMock()
            mock_response.text = json.dumps(mock_response_data)
            mock_post.return_value = mock_response
            response_text = getWizardTopicsSPARQL()
    
    # Verify it's valid JSON
    try:
        data = json.loads(response_text)
    except json.JSONDecodeError:
        pytest.fail("getWizardTopicsSPARQL did not return valid JSON")
        
    # Verify basic structure of SPARQL response
    assert 'results' in data
    assert 'bindings' in data['results']
    
    bindings = data['results']['bindings']
    
    # For real Fuseki, we expect some data, but if the DB is empty, this might fail.
    # We'll assert > 0 with a helpful message.
    assert len(bindings) > 0, "No topics returned (Check DB content if testing real Fuseki)"
    
    if len(bindings) > 0:
        # Check first item for expected fields
        first_item = bindings[0]
        expected_fields = ['topicIdentifier', 'topicName', 'L1', 'L2']
        for field in expected_fields:
            assert field in first_item, f"Missing field {field} in response"
        
        # Verify hierarchy logic (L1/L2 presence)
        has_categories = False
        has_subtopics = False
        
        for item in bindings:
            l2_val = item['L2']['value']
            if int(l2_val) == 0:
                has_categories = True
            else:
                has_subtopics = True
                
        assert has_categories, "No top-level categories (L2=0) found"
        # Subtopics might not exist in a minimal test DB, but in a real one they should.
        # In mock mode, we force them.
        if use_mock_fuseki:
            assert has_subtopics, "No subtopics (L2>0) found"
