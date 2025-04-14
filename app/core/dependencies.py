from app.reports.dependencies import get_handler_report
from app.reports.reports import AbstractReport


def get_report_object(type_report: str) -> AbstractReport:
    if type_report == "handlers":
        return get_handler_report()
    return None
