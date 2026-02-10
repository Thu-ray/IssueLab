"""Shared mention parsing helpers."""

import re

# GitHub username pattern: alnum/underscore, can include internal hyphen/underscore.
GITHUB_MENTION_PATTERN = re.compile(r"@([a-zA-Z0-9_](?:[a-zA-Z0-9_-]*[a-zA-Z0-9_])?)")


def extract_github_mentions(text: str | None) -> list[str]:
    """Extract deduplicated @mentions while preserving order."""
    if not text:
        return []

    matches = GITHUB_MENTION_PATTERN.findall(text)

    seen: set[str] = set()
    result: list[str] = []
    for username in matches:
        if username not in seen:
            seen.add(username)
            result.append(username)
    return result
