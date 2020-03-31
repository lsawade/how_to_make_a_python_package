from __future__ import (absolute_import, print_function, division)
import logging
from .log_util import VERBOSE
from .log_util import modify_logger

# Setup the logger
logger = logging.getLogger("matpy")
modify_logger(logger)

'''The different levels are

 0: logging.NOTSET
10: logging.DEBUG
15: logging.VERBOSE
20: logging.INFO
30: logging.WARNING
40: logging.ERROR
50: logging.CRITICAL

'''

logger.setLevel(logging.VERBOSE)


'''The following line is simply used to make it possible to 

.. code-block::
    
    from matpy import MatrixMultiplication
    
instead of 

.. code-block::
    
    from matpy.matrixmultiplication import MatrixMultiplication
    
which is still a valid statement.

Note the  "#NOQA" after the statement? This is used to note make an additional
automatic documentation entry.

'''
from .matrixmultiplication import MatrixMultiplication  # NOQA
