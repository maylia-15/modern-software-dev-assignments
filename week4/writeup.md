# Week 4 Write-up
Tip: To preview this markdown file
- On Mac, press `Command (⌘) + Shift + V`
- On Windows/Linux, press `Ctrl + Shift + V`

## INSTRUCTIONS

Fill out all of the `TODO`s in this file.

## SUBMISSION DETAILS

Name: **Rabiah Riska Amaliah** \
SUNet ID: **TODO** \
Citations: **Claude Code Best Practices (https://www.anthropic.com/engineering/claude-code-best-practices), Claude SubAgents Documentation (https://docs.anthropic.com/en/docs/claude-code/sub-agents)**

This assignment took me about **TODO** hours to do. 


## YOUR RESPONSES
### Automation #1
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> The design of this automation was inspired by the Claude Code Best Practices documentation, which emphasizes creating reusable workflows that reduce repetitive developer tasks. Running tests is a common task during development, so automating this process helps streamline the workflow.

b. Design of each automation, including goals, inputs/outputs, steps
> Goal:
The goal of this automation is to simplify running backend tests by providing a reusable command that executes the test suite and summarizes the results.

Inputs:
No required inputs. The automation runs the backend test suite automatically.

Steps:
1. Navigate to the backend test directory.
2. Execute pytest to run the test suite.
3. Stop after the first failing test.
4. Summarize the results for the developer.

Outputs:
The automation outputs a summary of test results, showing whether tests passed or which test failed.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
>How to run:
The automation is defined in `.claude/commands/run-tests.md`.

Command used internally:

pytest backend/tests -q --maxfail=1 -x

Expected output:
A summary of the backend test results, including passed tests or the first failing test.

Safety notes:
This automation does not modify source code. It only executes tests, so it is safe to run repeatedly.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> Before automation:
Developers needed to manually navigate directories and remember the correct pytest command to run tests.

After automation:
Developers can rely on the predefined slash command workflow, which standardizes the test execution process and reduces repetitive manual steps.

e. How you used the automation to enhance the starter application
> This automation helps developers quickly validate changes made to the starter application by running the backend tests. It simplifies the process of checking whether the application still works after modifying backend logic or API endpoints.


### Automation #2
a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> This automation was inspired by the Claude Code repository guidance concept described in the Claude Code Best Practices documentation. The CLAUDE.md file helps AI tools and developers understand the structure and workflow of the repository.

b. Design of each automation, including goals, inputs/outputs, steps
> Goal:
The goal of this automation is to provide clear repository guidance so that developers and AI assistants can easily understand the project structure and development workflow.

Inputs:
None. The CLAUDE.md file is automatically read when working within the repository.

Steps:
1. Document the project structure.
2. Explain how to run the application.
3. Provide testing instructions.
4. Define the recommended development workflow.

Outputs:
A clear repository guide that explains how the project is organized and how developers should interact with it.

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> How to run:
This automation is implemented through the `CLAUDE.md` file located in the repository root.

Expected output:
Developers or AI assistants can read the CLAUDE.md file to understand the repository layout, development workflow, and testing procedures.

Safety notes:
This file only provides documentation and guidance. It does not modify the application code.

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> Before automation:
Developers had to manually explore the repository to understand its structure and workflow.

After automation:
The CLAUDE.md file provides structured documentation that explains the repository layout and development workflow.

e. How you used the automation to enhance the starter application
> The CLAUDE.md file improves the developer experience by clearly documenting the project structure and instructions for running and testing the application. This makes it easier to maintain and extend the starter application.


### *(Optional) Automation #3*
*If you choose to build additional automations, feel free to detail them here!*

a. Design inspiration (e.g. cite the best-practices and/or sub-agents docs)
> TODO

b. Design of each automation, including goals, inputs/outputs, steps
> TODO

c. How to run it (exact commands), expected outputs, and rollback/safety notes
> TODO

d. Before vs. after (i.e. manual workflow vs. automated workflow)
> TODO

e. How you used the automation to enhance the starter application
> TODO
