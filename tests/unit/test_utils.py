from pathlib import Path

import pytest

from app.core.utils import check_file_list, check_report_type

TEST_FILE = Path(__file__).parent.parent / "fixtures/test_file"

@pytest.mark.parametrize(
    ("report_type", "expected"),
    [
        ("handlers", True),
        ("HANDLERS", False),
        ("routers", False),
        (None, False),
    ],
)
def test_check_report_type(report_type, expected) -> None:
    assert check_report_type(report_type) == expected

@pytest.mark.parametrize(
    ("file_list", "expected"),
    [
        ([TEST_FILE], [TEST_FILE]),
        ([TEST_FILE, TEST_FILE], [TEST_FILE]),
        ([TEST_FILE, "abcd"], [TEST_FILE]),
        (["abcd", "qwert"], None),
        (None, None),
    ],
)
def test_check_file_list(file_list, expected) -> None:
    assert check_file_list(file_list) == expected
