#!/usr/bin/env python

"""

This module includes a custom logger to make it easier to identify errors and
debug etc.

The module adds both another level to the logger and the corresponding
formatter. If you want to remove or add any logging level make sure to edit
both the CustomLogger and the CustomFormatter to accommodate your changes!

:author:
    Lucas Sawade (lsawade@princeton.edu, 2019)

:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lgpl.html)
"""
import logging

from logging import getLoggerClass
from logging import NOTSET

VERBOSE = 15


def addLoggingLevel(levelName, levelNum, methodName=None):
    """
    Comprehensively adds a new logging level to the `logging` module and the
    currently configured logging class.

    `levelName` becomes an attribute of the `logging` module with the value
    `levelNum`. `methodName` becomes a convenience method for both `logging`
    itself and the class returned by `logging.getLoggerClass()` (usually just
    `logging.Logger`). If `methodName` is not specified, `levelName.lower()` is
    used.

    To avoid accidental clobberings of existing attributes, this method will
    raise an `AttributeError` if the level name is already an attribute of the
    `logging` module or if the method name is already present

    .. rubric:: Example

    .. code-block::

        addLoggingLevel('TRACE', logging.DEBUG - 5)
        logging.getLogger(__name__).setLevel("TRACE")
        logging.getLogger(__name__).trace('that worked')
        logging.trace('so did this')
        logging.TRACE
        5

    Taken from StackOverflow because the code was beautifully simple.
    Author: Mad Physicist (Mar 4, 2016)

    """
    if not methodName:
        methodName = levelName.lower()

    if hasattr(logging, levelName):
        raise AttributeError(
            '{} already defined in logging module'.format(levelName))
    if hasattr(logging, methodName):
        raise AttributeError(
            '{} already defined in logging module'.format(methodName))
    if hasattr(logging.getLoggerClass(), methodName):
        raise AttributeError(
            '{} already defined in logger class'.format(methodName))

    # This method was inspired by the answers to Stack Overflow post
    # http://stackoverflow.com/q/2183233/2988730, especially
    # http://stackoverflow.com/a/13638084/2988730
    def logForLevel(self, message, *args, **kwargs):
        if self.isEnabledFor(levelNum):
            self._log(levelNum, message, args, **kwargs)

    def logToRoot(message, *args, **kwargs):
        logging.log(levelNum, message, *args, **kwargs)

    logging.addLevelName(levelNum, levelName)
    setattr(logging, levelName, levelNum)
    setattr(logging.getLoggerClass(), methodName, logForLevel)
    setattr(logging, methodName, logToRoot)


class CustomLogger(getLoggerClass()):
    """
    This class is just created ot add the VERBOSE level. More
    level could be added to this class to accommodate other levels.

    The variable VERBOSE is given at the top of the module. That way it can be
    changed for all depending function

    The class makes it possible to add extra levels to the classic logger
    The line `addLoggingLevel("VERBOSE", VERBOSE)` in the initalization is
    an example on how to add a level using the `addLoggingLevel` function
    located in this module.

    Don't forget to edit the `CustomFormatter` to accommodate for your
    introduced levels if you are using the `CustomFormatter`.
    An example is given in the class under `# EXTRA LEVELS` for the
    `VERBOSE` level.

    """

    def __init__(self, name, level=NOTSET):
        super().__init__(name, level)

        addLoggingLevel("VERBOSE", VERBOSE)


class CustomFormatter(logging.Formatter):
    """
    Logging Formatter to add colors and count warning / errors

    This class organizes the customization of the logging output.
    The formatter as of now outputs the logs in the following manner in
    order of Loglevel:

    .. rubric:: Example Output

    .. code-block:: python

        [2020-04-03 14:17:18] -- matpy.matrixmultiplication ----- [INFO]: Initializing matrices...
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication ---- [ERROR]: Test Error Level (matrixmultiplication.py:60)
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication - [CRITICAL]: Test Critical Level (matrixmultiplication.py:61)
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication -- [VERBOSE]: Test Verbose Level
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication -- [VERBOSE]: A:
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication -- [VERBOSE]:     [1 2]
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication -- [VERBOSE]:     [3 4]
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication -- [VERBOSE]: B:
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication -- [VERBOSE]:     [2 3 5]
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication -- [VERBOSE]:     [4 5 6]
        [2020-04-03 14:17:18] -- matpy.matrixmultiplication -- [WARNING]: Matrix size exceeds 4 elements.

    These outputs are colored in the actual output but the formatting is just
    as shown above. VERBOSE is an extra added LogLevel formatting. More can be
    added below the comment `EXTRA LEVELS` in the same way the VERBOSE is added.

    The variable VERBOSE is given at the top of the module. That way it can be
    changed for all depending function

    """

    # Setting up the different ANSI color escape sequences for color terminals:
    # Codes are 3/4-bit codes from here:
    # https://en.wikipedia.org/wiki/ANSI_escape_code
    # For 8-colors: use "\x1b[38;5;<n>m" where <n> is the number of the color.
    grey = "\x1b[38;21m"
    green = "\x1b[38;5;64m"
    light_grey = "\x1b[38;5;240m"
    dark_blue = "\x1b[38;5;25m"
    light_blue = "\x1b[38;5;69m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    dark_red = "\x1b[38;5;97m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"

    # Formats The spaces accommodate the different length of the words and
    # amount of detail wanted in the message:
    time_fmt = light_grey + "[%(asctime)s]" + reset
    name_fmt = "-- %(name)s -"
    pre_fmt = time_fmt + " " + name_fmt

    debug_fmt = "--- [" + light_blue + "%(levelname)s" + reset + "]:" \
        + light_blue + " %(message)s (%(filename)s:%(lineno)d)" + reset
    info_fmt = "---- [%(levelname)s]: %(message)s"
    warning_fmt = "- [" + yellow + "%(levelname)s" + reset + "]:" \
                 + yellow + " %(message)s" + reset
    error_fmt = "--- [" + red + "%(levelname)s" + reset + "]:" \
        + red + " %(message)s (%(filename)s:%(lineno)d)" + reset
    critical_fmt = " [" + bold_red + "%(levelname)s" + reset + "]:" \
        + bold_red + " %(message)s (%(filename)s:%(lineno)d)" + reset

    # Create format dictionary
    FORMATS = {
        logging.DEBUG: pre_fmt + debug_fmt,
        logging.INFO: pre_fmt + info_fmt,
        logging.WARNING: pre_fmt + warning_fmt,
        logging.ERROR: pre_fmt + error_fmt,
        logging.CRITICAL: pre_fmt + critical_fmt
    }

    # EXTRA LEVELS
    # Verbose
    addLoggingLevel('VERBOSE', VERBOSE)
    verbose_fmt = "- [%(levelname)s]: %(message)s"
    FORMATS[logging.VERBOSE] = pre_fmt + verbose_fmt  # add to format dictionary

    # Initialize with a default logging.Formatter
    def __init__(self):
        super().__init__(fmt="-- %(name)s ---- [%(levelname)s]: %(message)s",
                         datefmt=None, style='%')

    def format(self, record):

        # Use the logging.LEVEL to get the right formatting
        log_fmt = self.FORMATS.get(record.levelno)

        # Create new formatter with modified timestamp formatting.
        formatter = logging.Formatter(log_fmt, "%Y-%m-%d %H:%M:%S")

        # Return
        return formatter.format(record)


def modify_logger(logger):

    # Make sure only this module prints the logger information.
    logger.propagate = 0

    # Add formatter
    ch = logging.StreamHandler()
    ch.setFormatter(CustomFormatter())
    logger.addHandler(ch)

    return logger