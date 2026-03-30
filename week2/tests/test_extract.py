import pytest

from ..app.services.extract import (
    extract_action_items,
    extract_action_items_llm,
)


def test_extract_bullets_and_checkboxes():
    text = """
    Notes from meeting:
    - [ ] Set up database
    * implement API extract endpoint
    1. Write tests
    Some narrative sentence.
    """.strip()

    items = extract_action_items(text)

    assert "Set up database" in items
    assert "implement API extract endpoint" in items
    assert "Write tests" in items


def test_extract_action_items_llm_basic():
    text = """
    - Set up database
    - Write documentation
    Some random sentence.
    """

    items = extract_action_items_llm(text)

    assert isinstance(items, list)


def test_extract_action_items_llm_empty():
    items = extract_action_items_llm("")
    assert items == []


def test_extract_action_items_llm_paragraph():
    text = "We need to implement authentication and update the API."

    items = extract_action_items_llm(text)

    assert isinstance(items, list)