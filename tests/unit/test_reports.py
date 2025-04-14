import pytest

from app.reports.datas import StatusCollectData
from app.reports.dependencies import get_handler_report


def test_create_handler() -> None:
    hr = get_handler_report()
    assert hr.name == "handler"

lines_data = [
    "2025-03-28 12:25:45,000 DEBUG django.db.backends: (0.41) SELECT * FROM 'products' WHERE id = 4",
    "2025-03-28 12:44:46,000 INFO django.request: GET /api/v1/reviews/ 204 OK [192.168.1.59]",
    "2025-03-28 12:11:57,000 ERROR django.request: Internal Server Error: /admin/dashboard/ [192.168.1.29] - ValueError: Invalid input data",
    "2025-03-28 12:40:47,000 CRITICAL django.core.management: DatabaseError: Deadlock detected",
]
expecteds_data = [
    {},
    {"/api/v1/reviews/": {"debug": 0, "info": 1, "warning": 0, "error": 0, "critical": 0}},
    {
        "/api/v1/reviews/": {"debug": 0, "info": 1, "warning": 0, "error": 0, "critical": 0},
        "/admin/dashboard/": {"debug": 0, "info": 0, "warning": 0, "error": 1, "critical": 0},
    },
    {
        "/api/v1/reviews/": {"debug": 0, "info": 1, "warning": 0, "error": 0, "critical": 0},
        "/admin/dashboard/": {"debug": 0, "info": 0, "warning": 0, "error": 1, "critical": 0},
    },
]

def test_collect_statistic() -> None:
    hr = get_handler_report()
    for idx, line in enumerate(lines_data):
        hr.collect_statistic(line)
        assert len(hr.collector) == len(expecteds_data[idx])
        for key, val in expecteds_data[idx].items():
            assert hr.collector[key] == StatusCollectData(**val)

@pytest.mark.parametrize(
    ("data", "expected"),
    [(
        {},
        {"debug": 0, "info": 0, "warning": 0, "error": 0, "critical": 0},
    ),
    (
        {"debug": 5},
        {"debug": 5, "info": 0, "warning": 0, "error": 0, "critical": 0},
    ),
    (
        {"debug": 1, "info": 2, "warning": 3, "error": 4, "critical": 5},
        {"debug": 1, "info": 2, "warning": 3, "error": 4, "critical": 5},
    )],
)
def test_status_collect_data(data, expected) -> None:
    scd = StatusCollectData(**data)
    assert scd.critical == expected["critical"]
    assert scd.debug == expected["debug"]
    assert scd.error == expected["error"]
    assert scd.info == expected["info"]
    assert scd.warning == expected["warning"]

def test_handler_report_empty() -> None:
    hr = get_handler_report()
    hr.collect_statistic("")
    assert hr.show() == []

def test_handler_report() -> None:
    hr = get_handler_report()
    hr.collect_statistic("oqwp[op ERROR django.request: GET /api/test1/")
    assert hr.show() == [
        'HANDLER      DEBUG       INFO        WARNING     ERROR       CRITICAL    ',
        '/api/test1/             0           0           0           1           0',
        '',
        'Total request:               1'
        ]
