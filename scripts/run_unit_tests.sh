#!/bin/bash

export PROJECT_ROOT='..'

# Define test directories
TEST_DIRECTORIES=(
    "$(PROJECT_ROOT)/eliozo/unit-tests"
    "$(PROJECT_ROOT)/migration-script/unit-tests"
)

# Define log file location
LOG_FILE="$(PROJECT_ROOT)/logs/unit-tests.log"

# Clear previous log file
> $LOG_FILE

# Iterate over directories and run pytest
for TEST_DIR in "${TEST_DIRECTORIES[@]}"; do
    if [ -d "$TEST_DIR" ]; then
        echo "Running tests in $TEST_DIR"
        pytest "$TEST_DIR" | tee -a $LOG_FILE
    else
        echo "Directory $TEST_DIR does not exist."
    fi
done

exit 0
