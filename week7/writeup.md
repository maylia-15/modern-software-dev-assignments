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
> TODO

b. PR Description
> TODO

c. Graphite Diamond generated code review
> TODO

## Task 4: Improve tests for pagination and sorting
a. Links to relevant commits/issues
> TODO

b. PR Description
> TODO

c. Graphite Diamond generated code review
> TODO

## Brief Reflection 
a. The types of comments you typically made in your manual reviews (e.g., correctness, performance, security, naming, test gaps, API shape, UX, docs).
> TODO 

b. A comparison of **your** comments vs. **Graphite’s** AI-generated comments for each PR.
> TODO

c. When the AI reviews were better/worse than yours (cite specific examples)
> TODO

d. Your comfort level trusting AI reviews going forward and any heuristics for when to rely on them.
>TODO 



