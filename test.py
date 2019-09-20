"""
This is a small script that shows how to simply create a test class. The
reason why a test class is the superior choice over a function is that it can
set up a testing environment, e.g. a test directory structure needed to check
existing files. The unittest testclass also contains an easy way to check
whether your function throws an error, when it should.


:author:
    Lucas Sawade (lsawade@princeton.edu, 2019)

:copyright:
    Use it copy it and do whatever you like with it.

"""

import unittest
import numpy as np
from matrixmultiplication import matmul



class TestSomeModule(unittest.TestCase):
    """"A sample test class to check if your modules functions ar
    functioning."""

    def test_raise_shape_error(self):
        """Tests if error is raised when either A or B does not have 2
        dimensions"""

        # A does not have 2 dimensions
        a = np.array([[[1, 0], [0, 1]], [[0, 1], [0, 1]]])
        b = np.array([[4, 1], [2, 2]])

        with self.assertRaises(ValueError):
            matmul(a, b)

        # B does not have 2 dimensions
        a = np.array([[1, 0], [0, 1]])
        b = np.array([[[1, 0], [0, 1]], [[0, 1], [0, 1]]])

        with self.assertRaises(ValueError):
            matmul(a, b)

    def test_raise_shape_match_error(self):
        """Tests whether an error is thrown when b doesn't match a."""

        # B has more rows than a has columns!
        a = np.array([[1, 0], [0, 1]])
        b = np.array([[4, 1], [2, 2], [2, 2]])

        # Check if error is raised
        with self.assertRaises(ValueError):
            matmul(a, b)

    def test_multiplication(self):
        """Test the multiplication itself."""

        # Define matrix content.
        a = np.array([[1, 0], [0, 1]])
        b = np.array([[4, 1], [2, 2]])

        # Check result
        self.assertTrue(np.all(np.array([[4, 1], [2, 2]] == matmul(a, b))))


if __name__ == "__main__":
    unittest.main()