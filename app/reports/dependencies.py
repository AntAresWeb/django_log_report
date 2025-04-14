from app.parsers.dependencies import get_django_request_parser
from app.reports.reports import HandlersReport


def get_handler_report() -> HandlersReport:
    return HandlersReport(get_django_request_parser())
