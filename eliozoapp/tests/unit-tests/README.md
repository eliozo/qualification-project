If you want to run the unit tests: 

* Activate virtual environment "source ./venv-eliozo/bin/activate" in the project root directory.
* If `FUSEKI_URL` is unavailable but you must test SPARQL queries, create a tunnel and ask the user to 
supply the hostname and to log in: 

```bash
ssh -L 9080:127.0.0.1:9080 kalvis@<hostname>
```

* Finally, run the unit tests:

### Running SPARQL Tests

To run the SPARQL topic unit test with `pytest`:

1.  **SSH Tunnel (if needed):**
    If FUSEKI_URL is unavailable (e.g., remote server), create a tunnel:
    ```bash
    ssh -L 9080:127.0.0.1:9080 kalvis@<hostname>
    ```

2.  **Environment Setup:**
    Navigate to the test directory and set PYTHONPATH:
    ```bash
    cd eliozoapp/tests/unit-tests
    export PYTHONPATH=$PYTHONPATH:$(pwd)/../..
    ```

3.  **Run Tests:**

    *   **Against REAL Fuseki (Default):**
        ```bash
        pytest -s test_topics_sparql.py
        ```

    *   **With MOCK Fuseki Response:**
        ```bash
        USE_MOCK_FUSEKI=true pytest -s test_topics_sparql.py
        ```