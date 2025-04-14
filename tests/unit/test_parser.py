import pytest

from app.parsers.dependencies import get_django_request_parser
from tests.unit.data import test_data


@pytest.mark.parametrize(("line", "expected"), test_data)
def test_parser_for_log_level(line: str, expected: dict) -> None:
    parser = get_django_request_parser()
    result = parser.parse(line)
    assert result == expected
