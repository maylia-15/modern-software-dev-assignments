# Run Tests Automation

Intent:
Run the backend test suite and summarize results for the developer.

Steps:
1. Navigate to the backend directory.
2. Run the pytest test suite.
3. Stop on first failure.
4. Summarize the results.

Command to run:

pytest backend/tests -q --maxfail=1 -x

Expected Output:
- If tests pass: show summary of passing tests.
- If tests fail: show failing test and possible fix suggestions.