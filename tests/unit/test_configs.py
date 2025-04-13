import shlex

import pytest

from app.core.configs import parse_arguments


@pytest.mark.parametrize(
    ("param_str", "file_list", "report_type"),
    [
        ("file1 file2 --report handlers", ["file1", "file2"], "handlers"),
    ],
)
def test_argument_parser(
    param_str: str,
    file_list: list[str],
    report_type: str,
) -> None:
    arg_list = shlex.split(param_str)
    args = parse_arguments(arg_list)
    assert args.files == file_list
    assert args.report == report_type


