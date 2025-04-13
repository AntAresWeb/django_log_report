import argparse
import logging
from logging.handlers import RotatingFileHandler

import app.core.constants as const


def parse_arguments(arg_list: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=const.SERVICE_NAME,
        usage=const.SERVICE_USAGE,
        description=const.SERVICE_DECRIPTION,
    )
    parser.add_argument(
        "files",
        type=str,
        metavar="files",
        nargs="+",
        help="Список лог-файлов для анализа и включения в отчет",
    )
    parser.add_argument(
        "--report",
        type=str,
        choices=const.REPORT_TYPES,
        help="Вид отчета",
    )

    return parser.parse_args(arg_list)


def configure_logging() -> None:
    log_dir = const.BASE_DIR / "logs"
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / f"{const.SERVICE_NAME}.log"

    rotating_handler = RotatingFileHandler(log_file, maxBytes=10**6, backupCount=5)
    logging.basicConfig(
        datefmt=const.DATETIME_FORMAT,
        format=const.SEVICE_LOG_FORMAT,
        level=logging.INFO,
        handlers=(rotating_handler, logging.StreamHandler()),
    )
