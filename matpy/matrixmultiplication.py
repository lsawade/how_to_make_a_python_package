#!/usr/bin/env python

""" This is a sample module that defines a bunch of matrix multiplication
function and puts them together in a class. So you it's easier to understand
how to actually use classes.

:author:
    Lucas Sawade (lsawade@princeton.edu, 2019)

:copyright:
    Use it copy it and do whatever you like with it.

"""

import numpy as np
import sys



class MatrixMultiplication(object):
    """Class to handle 2D matrix multiplication."""

    def __init__(self, a, b, method="matmul"):
        """ This function initializes the MatrixMultiplication class.

        :param a:
        :param b:
        """

        if method not in ["matmul", "dotprod"]:
            raise ValueError("Method not available")

        # Just assigning the variables
        self.a = a
        self.b = b

        # Here sys.modules[__name__] refers to the module it if you had
        # imported and outside module, e.g., `import os`, to get the join
        # function you would have to write
        # getattr(getattr(os, "path"), "join").
        self.method = getattr(sys.modules[__name__], method)
        print(self.method)

    def __call__(self):
        return self.method(self.a, self.b)



def matmul(a, b):
    """ Standard wrapper around numnpy's function.

    :param a: matrix A
    :type a: numpy.array
    :param b: matrix B
    :type a: numpy.array
    :return: multiply matrix
    """

    # First check whether the matrices can be multiplied! And for this case
    # are 2D
    if len(a.shape) != 2 or len(b.shape) != 2:
        raise ValueError("A or B is not of dimension 2")
    elif a.shape[1] != b.shape[0]:
        raise ValueError(
            "A's 2nd dimension does not match B's first dimension")

    # Compute the multiplication
    c = np.matmul(a, b)

    return c


def dotprod(a, b):
    """ Standard wrapper around numnpy's function.

    :param a: matrix A
    :type a: numpy.array
    :param b: matrix B
    :type a: numpy.array
    :return: multiply matrix
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