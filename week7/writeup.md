# Week 7 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## Instructions

Fill out all of the `TODO`s in this file.

## Submission Details

Name: Rabiah Riska Amaliah \
SUNet ID: **TODO** \
Citations: FastAPI Documentation, Pydantic V2 Migration Guide, Graphite AI (Diamond).

This assignment took me about 4 hours to do. 


## Task 1: Add more endpoints and validations
a. Links to relevant commits/issues
> https://app.graphite.com/github/pr/maylia-15/modern-software-dev-assignments/2

b. PR Description
> Implemented strict Pydantic validation for PATCH /notes/{id} to prevent empty titles/content. Fixed a Windows-specific PermissionError in conftest.py by adding a try-except block for database unlinking.

c. Graphite Diamond generated code review
> The AI found no issues, confirming that the field_validator and schema implementation follow best practices.

## Task 2: Extend extraction logic
a. Links to relevant commits/issues
> https://app.graphite.com/github/pr/maylia-15/modern-software-dev-assignments/3

b. PR Description
> Enhanced extract_action_items using Regex to identify priorities (high/urgent, low) and due dates (tomorrow, specific dates). Updated the function to return ActionItemCreate objects instead of strings.

c. Graphite Diamond generated code review
> AI reviewed the Regex patterns and confirmed the logic is robust for basic NLP extraction.

## Task 3: Try adding a new model and relationships
a. Links to relevant commits/issues
> https://app.graphite.com/github/pr/maylia-15/modern-software-dev-assignments/4

b. PR Description
> Implemented a Many-to-Many relationship between Note and Tag models using a note_tags association table. Added endpoints to associate and remove tags, and updated NoteRead schema to include nested tag data.

c. Graphite Diamond generated code review
> Graphite Diamond confirmed that the Many-to-Many implementation using an association table (note_tags) and SQLAlchemy's relationship with back_populates was correctly implemented without any architectural issues.

## Task 4: Improve tests for pagination and sorting
a. Links to relevant commits/issues
> https://app.graphite.com/github/pr/maylia-15/modern-software-dev-assignments/5

b. PR Description
> Added automated tests in test_pagination.py to verify limit, skip, and sort parameters. Ensured that sorting by title and creation date (ascending/descending) works correctly using consistent test data.

c. Graphite Diamond generated code review
> The AI found no issues, confirming that the test suite effectively covers pagination edge cases and correctly utilizes the client fixture for API testing.

## Brief Reflection 
a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).
> I focused on Correctness and Environment Compatibility, specifically catching ValidationError during schema mapping and fixing the Windows-specific PermissionError during test database cleanup.

b. A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.
> My comments were focused on runtime bugs and integration logic, while Graphite's comments were more focused on architectural standards and ensuring the code followed Python best practices.

c. When the AI reviews were better/worse than yours (cite specific examples)
> AI was better at ensuring clean code structure and naming conventions. However, AI was worse at detecting integration-level errors, such as the missing description field in the Pydantic schema which I had to debug manually.

d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.
>I am comfortable using AI for static code quality and security checks. My heuristic is to rely on AI for "cleanliness" but always perform manual testing for complex integration and OS-specific issues.



