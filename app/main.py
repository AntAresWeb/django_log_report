import logging

from app.core.configs import configure_logging, parse_arguments
from app.engines.engines import SerialEngine
from app.core.dependencies import report_matrix

def get_handlers_report() -> None:
    pass

MODE_FUNCTION_SERVICE = {
    "handlers": get_handlers_report,
}


def main() -> None:
    args = parse_arguments()

    configure_logging()

    if report_matrix.get(args.report):
        
    logging.info("Формирование отчета запущено!")
    # engine = SerialEngine(args.files)
    # engine.run()
    logging.info("Аргументы командной строки: %s", args)
    logging.info("Формирование отчета завершено!")


if __name__ == "__main__":
    main()
