Logging
------------

As you probably noticed almost no package, e.g. :mod:`numpy` has print
functions. Most packages use so called logging. Logging enables you to turn
on/off printing depending on the logging mode. It is a standard python built-in,
so I suggest you make use of it


Setting up your logging
+++++++++++++++++++++++

A standard practice is to set the logger in the :mod:`matpy.__init__` using
Python's built-in :mod:`logging` module.

.. include:: ../../../matpy/__init__.py
    :code: python

The outline is as follows:

1. Retrieve the module's logger
2. Set the logging level
3. Add the print stream handler and a formatter.

The formatter is optional but convenient. instead of the
:class:`matpy.log_util.CustomFormatter`, a "simple"

.. code-block:: python

    # Customformatter
    FORMAT = "%(name)s - %(levelname)s: %(message)s"
    formatter = logging.Formatter(FORMAT)
    ch.setFormatter(formatter)

would have worked as well, but let me elaborate the benefits (beauty) of a truly
custom formatter. The code is shown below and not all too complicated.


.. include:: ../../../matpy/log_util.py
    :code: python

The :class:`matpy.log_util.CustomFormatter` is a basic class containing some
info that specifies the nature of the logged print statements, i.e., colors and
whether a certain statement should be print depending on the logging levels.

There are a number 6 different logging levels:

- 0. Not-set
- 10. Debug
- 20. Info
- 30. Warning
- 40. Error
- 50. Critical

In general, the lower the debug level the larger the number of messages.
Meaning, if the level is set to 50, only `Critical` messages will be printed,
but if the level is set to 20, `Critical`, `Error`, `Warning`, and `Info`
messages will be printed.

We can in theory create a different format for any of those message-levels.
When debugging for examples this can be a huge advantage. because you can
assign a different color to the debugging messages and find the correct lines
faster.

The logging level of any package can be set by any script from anywhere by
retrieving the logger and setting the level:

.. code-block:: python

    import logging

    # Retrieve logger
    logger = logging.getLogger("matpy")

    # Set level
    logger.setLevel(logging.INFO)


For this package, we put set the level to VERBOSE, so that all messages are
printed. Except the

Then, just as in :func:`matpy.matrixmultiplication.matmul`, the logger can
print statements much like the normal print function.

.. code-block:: python

    # import from `__init__.py`
    from . import logger

    logger.debug("Test Debug")
    logger.error("Test Error")
    logger.critical("Test Critical")
    logger.info("Test info")
    logger.warning("Test Warning")

So, now you are all set for logging! Feel free to modify the logging!



## CustomLogger


