import logging

from app.core.configs import configure_logging, parse_arguments
from app.core.dependencies import get_report_object
from app.core.utils import check_file_list, check_report_type
from app.engines.engines import SerialEngine


def main() -> None:
    args = parse_arguments()
    configure_logging()
    logging.info("Программа запущена!")
    logging.info("Аргументы командной строки: %s", args)

    if not check_file_list(args.files):
        return

    if not check_report_type(args.report):
        logging.error("Неверно указан тип отчета!")
        return

    engine = SerialEngine(get_report_object(args.report), args.files)
    logging.info("Формирование отчета запущено!")
    engine.run()
    for line in engine.get_report():
        logging.info(line)
    logging.info("Формирование отчета завершено!")

if __name__ == "__main__":
    main()
    logging.info("Программа завершена!")
