#!/usr/bin/env python

""" This is a sample module that defines a bunch of matrix multiplication
function and puts them together in a class. So you it's easier to understand
how to actually use classes.

:author:
    Lucas Sawade (lsawade@princeton.edu, 2019)

:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lgpl.html)

"""

import numpy as np
import sys
import logging
from .log_util import modify_logger

# Setup Logger
logger = logging.getLogger(__name__)
modify_logger(logger)


def matmul(a, b):
    """ Standard wrapper around numnpy's function.

    :param a: matrix A
    :type a: numpy.ndarray
    :param b: matrix B
    :type b: numpy.ndarray
    :return: multiplied matrix

    Usage:
        Assume that a and b are 2D numpy arrays that match in size for
        multiplication.

        .. code-block:: python

            from matpy.matrixmultiplication import matmul
            c = matmul(a, b)
            print(c)

    """

    # First check whether the matrices can be multiplied! And for this case
    # are 2D
    if len(a.shape) != 2 or len(b.shape) != 2:
        raise ValueError("A or B is not of dimension 2")
    elif a.shape[1] != b.shape[0]:
        raise ValueError(
            "A's 2nd dimension does not match B's first dimension")

    ''' Below just some usages of loggers. different levels of logging 
    can be set to control the printed output of a package.'''

    # Just for testing the loggers.
    logger.debug("Test Debug Level")
    logger.error("Test Error Level")
    logger.critical("Test Critical Level")
    logger.verbose("Test Verbose Level")

    # Logging the matrices
    logger.verbose("A:")
    for row in a:
        logger.verbose("    " + np.array_str(row, max_line_width=np.inf))
    if a.size > 4:
        logger.warning("Matrix size exceeds 4 elements.")

    logger.verbose("B:")
    for row in b:
        logger.verbose("    " + np.array_str(row, max_line_width=np.inf))

    if b.size > 4:
        logger.warning("Matrix size exceeds 4 elements.")
    # Compute the stuff
    c = np.matmul(a, b)

    return c


def dotprod(a, b):
    """ Standard wrapper around numpy's function.

    :param a: matrix A
    :type a: numpy.ndarray
    :param b: matrix B
    :type b: numpy.ndarray
    :return: multiplied matrix

     Usage:
        Assume that a and b are 2D numpy arrays that match in size for
        multiplication.

        .. code-block:: python

            >>> from matpy.matrixmultiplication import dotprod
            >>> c = dotprod(a, b)
            >>> print(c)

    """

    # First check whether the matrices can be multiplied! And for this case
    # are 2D
    if len(a.shape) != 2 or len(b.shape) != 2:
        raise ValueError("A or B is not of dimension 2")
    elif a.shape[1] != b.shape[0]:
        raise ValueError(
            "A's 2nd dimension does not match B's first dimension")

    # Compute the multiplication
    c = np.dot(a, b)

    return c


class MatrixMultiplication(object):
    """Class to handle 2D matrix multiplication.

    Usage:
        Assume that a and b are 2D numpy arrays that match in size for
        multiplication.

        .. code-block:: python

            >>> from matpy.matrixmultiplication import MatrixMultiplication
            >>> MM = MatrixMultiplication(a, b, method="matmul")
            >>> c = MM()
            >>> print(c)

        Or using the other method

        .. code-block:: python

            >>> from matpy.matrixmultiplication import MatrixMultiplication
            >>> MM = MatrixMultiplication(a, b, method="dotprod")
            >>> c = MM()
            >>> print(c)
    """

    def __init__(self, a, b, method="matmul"):
        """ This function initializes the MatrixMultiplication class.

        :param a: matrix A
        :type a: numpy.ndarray
        :param b: matrix B
        :type b: numpy.ndarray

        """

        if method not in ["matmul", "dotprod"]:
            raise ValueError("Method not available")

        logger.info("Initializing matrices...")
        # Just assigning the variables
        self.a = a
        self.b = b

        # Here sys.modules[__name__] refers to the module if you had
        # imported and outside module, e.g., `import os`, to get the join
        # function you would have to write
        # getattr(getattr(os, "path"), "join").
        self.method = getattr(sys.modules[__name__], method)

    def __call__(self):
        """Simple call function that executes the multiplication.

        .. note::

            This ``__call__`` function can of course take arguments. Let's
            say you create an interpolator with a specified amount of points.
            You could stick in your query points as arguments."""
        return self.method(self.a, self.b)
