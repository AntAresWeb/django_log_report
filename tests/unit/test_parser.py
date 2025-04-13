import pytest

from app.parsers.parsers import get_django_request_parser

test_data = [
    (
        "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]",
        {"status": "INFO", "method": "GET", "endpoint": "/api/v1/reviews/"},
    ),
    (
        "2025-03-28 12:11:57,000 ERROR django.request: Internal Server Error: /admin/dashboard/ [192.168.1.29] - ValueError: Invalid input data",
        {"status": "ERROR", "method": None, "endpoint": "/admin/dashboard/"},
    ),
    ("2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected", None),
    ("2025-03-28 12:25:45,000 DEBUG django.db.backends: (0.41) SELECT * FROM 'products' WHERE id = 4", None),
    ("2025-03-28 12:01:42,000 WARNING django.security: IntegrityError: duplicate key value violates unique constraint", None),
]

@pytest.mark.parametrize(("line", "expected"), test_data)
def test_parser_for_log_level(line: str, expected: dict) -> None:
    parser = get_django_request_parser()
    result = parser.parse(line)
    assert result == expected
