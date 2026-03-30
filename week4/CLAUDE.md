# Claude Code Repository Guidance

## Project Overview
This repository contains a minimal full-stack developer command center application.

The backend is built with FastAPI and SQLite using SQLAlchemy.
The frontend is a simple static interface served by FastAPI.

## Project Structure

backend/
Contains the FastAPI application including API routes, models, and database logic.

frontend/
Contains static UI files served by the backend.

data/
Contains the SQLite database and seed data.

docs/
Contains developer tasks and documentation.

.claude/commands/
Contains custom slash commands used to automate developer workflows.

## Running the Application

To start the backend server:

uvicorn backend.app.main:app --reload

The application will run at:
http://localhost:8000

API documentation is available at:
http://localhost:8000/docs

## Testing

Run the test suite using pytest:

pytest backend/tests

## Development Workflow

Recommended development workflow:

1. Write or update tests for new functionality.
2. Implement the backend logic.
3. Run linting and formatting tools.
4. Run tests to verify functionality.
5. Update documentation if necessary.

## Automation

This repository includes developer automations such as:

/run-tests

This command runs the backend test suite and summarizes results.