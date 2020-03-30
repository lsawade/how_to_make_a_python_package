from __future__ import (absolute_import, print_function, division)
import logging
from .log_util import CustomFormatter

# Setup the logger
logger = logging.getLogger("matpy")
logger.setLevel(logging.DEBUG)
logger.propagate = 0

# Add formatter
ch = logging.StreamHandler()
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)


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
