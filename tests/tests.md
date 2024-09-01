# Testing Guide

This document provides instructions for running both automatic and manual tests for the project. Please note that all tests should be run from the root directory of the project.

## Automatic Tests

### Python Tests

To run all automatic Python tests, use the following command:  
```bash
pytest
```

#### Running Tests in Parallel

To speed up the testing process, you can run tests in parallel using the `-n` option. For example, to run tests with 4 workers:  
```bash
pytest -n 4
```

#### Verbose Output

If you want more detailed information about each test, use the `-v` (verbose) option:  
```bash
pytest -v
```

#### Specific Test Files

To run a specific Python test file:  
```bash
pytest tests/<path_to_test_file>.py
```

### C++ Tests

## Manual Tests

### Python Manual Tests

Manual tests are used for scenarios that require human interaction. For example, testing live audio input.

#### Speech-to-Text Testing

To test the speech-to-text functionality manually, you can use the following command:  
```bash
pytest -s tests/nlp_tests/manual_live_audio.py
```
This will allow the script to capture live audio from your microphone.

### C++ Manual Tests

---

**Note:** All tests should be run via the root directory of the project to ensure correct relative paths and dependencies.
