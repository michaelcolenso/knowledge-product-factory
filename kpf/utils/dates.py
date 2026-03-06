"""Date utilities."""

from datetime import date


def today_str() -> str:
    return date.today().isoformat()
