import logging

from app.core.configs import configure_logging, parse_arguments


def get_handlers_report() -> None:
    pass

MODE_FUNCTION_SERVICE = {
    "handlers": get_handlers_report,
}


def main() -> None:
    args = parse_arguments()

    configure_logging()

    logging.info("Формирование отчета запущено!")
    logging.info("Аргументы командной строки: %s", args)
    logging.info("Формирование отчета завершено!")


if __name__ == "__main__":
    main()
