#!/usr/bin/env python

from matpy import MatrixMultiplication
import numpy as np
import logging

# Use this to set the logger to different levels.
logger = logging.getLogger("matpy")


# Set up tests arrays
a = np.array([[1, 2],
              [3, 4]])
b = np.array([[2, 3, 5],
              [4, 5, 6]])

# Use class and function call
M = MatrixMultiplication(a, b, method='matmul')
c = M()

print("C:")
print(c)