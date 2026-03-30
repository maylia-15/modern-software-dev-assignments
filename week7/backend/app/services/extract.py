import re
from datetime import datetime, timedelta
from typing import List
from backend.app.schemas import ActionItemCreate

# Regex patterns
DUE_PATTERNS = [
    (re.compile(r"\bdue tomorrow\b", re.IGNORECASE), lambda: (datetime.now() + timedelta(days=1)).date()),
    (re.compile(r"\bby Friday\b", re.IGNORECASE), lambda: "Friday"),  # keep symbolic if not exact date
    (re.compile(r"\bdeadline:\s*(\d{4}-\d{2}-\d{2})", re.IGNORECASE), lambda m: m.group(1)),
]

PRIORITY_PATTERNS = {
    re.compile(r"\burgent\b", re.IGNORECASE): "urgent",
    re.compile(r"\bhigh priority\b", re.IGNORECASE): "high",
    re.compile(r"\blow priority\b", re.IGNORECASE): "low",
}


def extract_action_items(text: str) -> List[ActionItemCreate]:
    items: List[ActionItemCreate] = []

    # Split text into candidate sentences or lines
    candidates = re.split(r"[.\n]", text)

    for candidate in candidates:
        candidate = candidate.strip()
        if not candidate:
            continue

        due_date = None
        priority = None

        # Detect due dates
        for pattern, handler in DUE_PATTERNS:
            match = pattern.search(candidate)
            if match:
                due_date = handler(match) if match else handler()
                break

        # Detect priority
        for pattern, level in PRIORITY_PATTERNS.items():
            if pattern.search(candidate):
                priority = level
                break

        # Build ActionItemCreate object
        item = ActionItemCreate(
            description=candidate, 
            due_date=str(due_date) if due_date else None,
            priority=priority,
        )
        items.append(item)

    return items
