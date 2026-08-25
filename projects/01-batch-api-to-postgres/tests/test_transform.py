from src.transform import deduplicate_latest, normalize_record


def test_keeps_latest_record_per_id() -> None:
    rows = deduplicate_latest(
        [
            {"id": 2, "updated_at": "2026-01-01T10:00:00Z", "amount": "4"},
            {"id": 2, "updated_at": "2026-01-02T10:00:00Z", "amount": "7"},
            {"id": 1, "updated_at": "2026-01-01T10:00:00Z", "amount": 3},
        ]
    )

    assert rows == [
        {"id": "1", "updated_at": "2026-01-01T10:00:00Z", "amount": 3.0},
        {"id": "2", "updated_at": "2026-01-02T10:00:00Z", "amount": 7.0},
    ]


def test_missing_field_is_rejected() -> None:
    try:
        normalize_record({"id": 1, "updated_at": "2026-01-01T00:00:00Z"})
    except ValueError as error:
        assert "amount" in str(error)
    else:
        raise AssertionError("invalid record should be rejected")
