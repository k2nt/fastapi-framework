import logging

from domain.logger import strfmt


_DEFAULT_TIME_FORMAT = "%Y-%m-%d %H:%M:%S"
_DEFAULT_FORMAT = "%(asctime)s  %(name)s  %(levelname)-8s  %(message)s"


class ColoredFormatter():
    """Custom formatter class for API logging."""
    def __init__(self, fmt: str = _DEFAULT_FORMAT):
        self.fmt = fmt

    def format(self, record):
        FORMATS = {
            logging.DEBUG: strfmt.cyan(self.fmt),
            logging.INFO: strfmt.white(self.fmt),
            logging.WARNING: strfmt.yellow(self.fmt),
            logging.ERROR: strfmt.red(self.fmt),
            logging.CRITICAL: strfmt.red(self.fmt),
        }
        
        log_fmt = FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt=_DEFAULT_TIME_FORMAT)
        return formatter.format(record)
    