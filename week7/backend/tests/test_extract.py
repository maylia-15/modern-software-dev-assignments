from backend.app.services.extract import extract_action_items


def test_extract_action_items():
    text = """
    This is a note
    - TODO: write tests
    - ACTION: review PR
    - Ship it!
    Not actionable
    """.strip()
    
    items = extract_action_items(text)
    
    descriptions = [item.description for item in items]
    
    assert "- TODO: write tests" in descriptions
    assert "- ACTION: review PR" in descriptions
    assert "- Ship it!" in descriptions


