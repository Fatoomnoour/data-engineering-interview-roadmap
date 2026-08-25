"""Pure transformations for Project 01.

The functions are intentionally side-effect free so they can be unit tested
before adding an API client or a database loader.
"""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any


REQUIRED_FIELDS = {"id", "updated_at", "amount"}


def normalize_record(record: Mapping[str, Any]) -> dict[str, Any]:
    """Validate and normalize one source record."""
    missing = REQUIRED_FIELDS - record.keys()
    if missing:
        raise ValueError(f"missing required fields: {sorted(missing)}")

    return {
        "id": str(record["id"]),
        "updated_at": str(record["updated_at"]),
        "amount": float(record["amount"]),
    }


def deduplicate_latest(records: Iterable[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """Keep the latest record per id using lexicographic timestamp ordering.

    In production, parse timestamps into timezone-aware datetime values and
    define a tie-breaker such as source sequence number.
    """
    latest: dict[str, dict[str, Any]] = {}
    for raw in records:
        record = normalize_record(raw)
        current = latest.get(record["id"])
        if current is None or record["updated_at"] >= current["updated_at"]:
            latest[record["id"]] = record
    return sorted(latest.values(), key=lambda row: row["id"])
