"""

This module includes a custom logger to make it easier to identify errors and
debug etc.

:author:
    Lucas Sawade (lsawade@princeton.edu, 2019)

:copyright:
    Use it copy it and do whatever you like with it.

"""
import logging

class CustomFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    # Setting up the different ANSI color escape sequences for color terminals:
    grey = "\x1b[38;21m"
    lightblue = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    # Formats The spaces accommodate the different length of the words and
    # amount of detail wanted in the message:
    format_inf = "[%(asctime)s] %(name)s | %(levelname)s     | %(message)s"
    format_war = "[%(asctime)s] %(name)s | %(levelname)s  | %(message)s"
    format_dbg = "[%(asctime)s] %(name)s | %(levelname)s    | %(message)s (%(filename)s:%(lineno)d)"
    format_err = "[%(asctime)s] %(name)s | %(levelname)s    | %(message)s (%(filename)s:%(lineno)d)"
    format_cri = "[%(asctime)s] %(name)s | %(levelname)s | %(message)s (%(filename)s:%(lineno)d)"

    # Create format dictionary
    FORMATS = {
        logging.INFO: format_inf,
        logging.DEBUG: format_dbg,
        logging.WARNING: yellow + format_war + reset,
        logging.ERROR: red + format_err + reset,
        logging.CRITICAL: bold_red + format_cri + reset
    }

    # Initialize with a default logging.Formatter
    def __init__(self):
        super().__init__(fmt="%(levelno)d: %(msg)s", datefmt=None, style='%')

    def format(self, record):

        # Use the logging.LEVEL to get the right formatting
        log_fmt = self.FORMATS.get(record.levelno)

        # Create new formatter with modified timestamp formatting.
        formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")

        # Return
        return formatter.format(record)
