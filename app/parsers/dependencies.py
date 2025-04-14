from app.parsers.parsers import DjangoRequestParser


def get_django_request_parser() -> DjangoRequestParser:
    return DjangoRequestParser()
