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

.. literalinclude:: ../../../matpy/__init__.py
    :language: python
    :linenos:

The outline is as follows:

1. Retrieve the module's logger
2. Use how it outputs stuff using the :func:`matpy.log_util.modify_logger`
3. Set logging level

All necessary code for modifying the logging is located in the
:mod:`matpy.log_util`. The code is shown below and not all too complicated,
but it is 'long'. Do not get intimidated and continue below!

.. literalinclude:: ../../../matpy/log_util.py
    :language: python
    :linenos:

There are 3-4 important things here. The first one is the
:class:`matpy.log_util.CustomLogger`. The :class:`matpy.log_util.CustomLogger`
simply takes :class:`logging.Logger` and adds another Logging (see below) level
by using the function :func:`matpy.log_util.addLoggingLevel`. That's all the
functions are doing. Of course there are some details in
:func:`matpy.log_util.addLoggingLevel`, but those are simply there to handle
the adding if the :class:`matpy.log_util.CustomLogger` is called multiple times
so that the Logging level is not overwritten.
The most important part (why I started writing the logging docs) is the
:class:`matpy.log_util.CustomFormatter`.
The :class:`matpy.log_util.CustomFormatter` is a basic class containing some
info that specifies the nature of the logged print statements, i.e., colors and
whether a certain statement should be print depending on the logging levels etc.
It's basic string formatting that depends on the level of the statements.

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
When debugging for examples this can be a huge advantage, because you can
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
printed. Except the `DEBUG` message. An example output:

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


Then, just as in :func:`matpy.matrixmultiplication.matmul`, the logger can
print statements much like the normal print function.

.. code-block:: python

    # Setup Logger at the top of your module
    import logging
    from .log_util import modify_logger

    logger = logging.getLogger(__name__)
    modify_logger(logger)

    logger.debug("Test Debug")
    logger.error("Test Error")
    logger.critical("Test Critical")
    logger.info("Test info")
    logger.warning("Test Warning")


The last important this is modify logger. I wish it wasn't so but it also has
to be run to apply the :class:`matpy.log_util.CustomFormatter` because the
intrinsic logging facility has its one format. Just to explain it see the
code below.

.. code-block:: python

    def modify_logger(logger):

        # Make sure only this module prints the logger information.
        logger.propagate = 0

        # Add formatter
        ch = logging.StreamHandler()
        ch.setFormatter(CustomFormatter())
        logger.addHandler(ch)

        return logger

The propagate module sets only that the logging statements are not propagated
to a parent module, so that this is the only module to print the messages. The
:class:`loggingStreamHandler` handles how stuff is output, in our case we
want it to be output in a specific format, so we set our
:class:`matpy.log_util.CustomFormatter`. The formatter is optional but
convenient. instead of the :class:`matpy.log_util.CustomFormatter`, a "simple"

.. code-block:: python

    # Customformatter
    FORMAT = "%(name)s - %(levelname)s: %(message)s"
    formatter = logging.Formatter(FORMAT)
    ch.setFormatter(formatter)

would have worked as well, but let me elaborate the benefits (beauty) of a truly
custom formatter.

So, now you are all set for logging! Feel free to modify the logging!



