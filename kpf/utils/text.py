"""Text processing utilities."""

import re


def extract_json_block(text: str) -> str:
    """Strip markdown code fences from LLM JSON responses."""
    # Try to extract from ```json ... ``` block
    pattern = r"```(?:json)?\s*\n?([\s\S]*?)\n?```"
    match = re.search(pattern, text)
    if match:
        return match.group(1).strip()
    # Try to find first { ... } block
    start = text.find("{")
    end = text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return text[start : end + 1]
    return text.strip()


def truncate(text: str, max_chars: int) -> str:
    if len(text) <= max_chars:
        return text
    return text[:max_chars] + "..."
