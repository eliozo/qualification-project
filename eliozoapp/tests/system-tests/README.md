# System Test Scenario: Topic Navigation

This document describes a manual test scenario to verify the `getTopic` function (and subsequently `getAllTopicChildren`) in the `indexes` blueprint.

## Objectives
- Verify that `getTopic` correctly handles a `topicIdentifier` parameter.
- Verify that `getAllTopicChildren` retrieves the correct child topics.
- Verify that `getTopicProblemsSPARQL` retrieves associated problems.

## Prerequisites
- The application must be running (e.g., at `http://127.0.0.1:5000`).
- The Fuseki SPARQL endpoint must be accessible and populated with topic data.

## Test Steps

1.  **Open Browser**: Launch a web browser.
2.  **Navigate to Topic Page**: Enter the following URL:
    `http://127.0.0.1:5000/eliozo/topic_tasks?topicIdentifier=1.1`
    *(Replace `1.1` with a valid topic identifier from your dataset, e.g., Algebra/Arithmetic)*

3.  **Verify Page Content**:
    - **Header**: Check if the page title displays "Tēma".
    - **Parent Info**: Verify that the parent topic number, name, and description are displayed correctly.
    - **Child Topics**: Verify that a list of subtopics (children of `1.1`) is displayed. This confirms `getAllTopicChildren` is working.
    - **Problems**: Verify that a list of problems associated with this topic is displayed. This confirms `getTopicProblemsSPARQL` is working.

4.  **Navigation**: Click on one of the child topics.
    - Verify that the URL updates to the new `topicIdentifier`.
    - Verify that the page content refreshes with the new topic's details.

## Expected Behavior
- The page should load without errors (HTTP 200).
- Data from the SPARQL endpoint should be correctly parsed and displayed.
- Navigation links should point to valid `topic_tasks` URLs.
