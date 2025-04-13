import shlex

import pytest

from app.core.configs import parse_arguments

test_data = [
    ("file1 file2 --report handlers", ["file1", "file2"], "handlers"),
    ("file1", ["file1"], None),
]

@pytest.mark.parametrize(
    ("param_str", "file_list", "report_type"), test_data,
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


