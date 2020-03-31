"""
This is a small script that shows how to simply create a tests class. The
reason why a tests class is the superior choice over a function is that it can
set up a testing environment, e.g. a tests directory structure needed to check
existing files. The unittest testclass also contains an easy way to check
whether your function throws an error, when it should.


:author:
    Lucas Sawade (lsawade@princeton.edu, 2019)

:license:
    GNU Lesser General Public License, Version 3
    (http://www.gnu.org/copyleft/lgpl.html)

"""

import unittest
import numpy as np
from matpy.matrixmultiplication import matmul
from matpy.matrixmultiplication import dotprod
from matpy.matrixmultiplication import MatrixMultiplication


class TestMatMul(unittest.TestCase):
    """"A sample tests class to check if your modules' functions ar
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


class TestDot(unittest.TestCase):
    """"A sample tests class to check if your modules' functions ar
    functioning."""

    def test_raise_shape_error(self):
        """Tests if error is raised when either A or B does not have 2
        dimensions"""

        # A does not have 2 dimensions
        a = np.array([[[1, 0], [0, 1]], [[0, 1], [0, 1]]])
        b = np.array([[4, 1], [2, 2]])

        with self.assertRaises(ValueError):
            dotprod(a, b)

        # B does not have 2 dimensions
        a = np.array([[1, 0], [0, 1]])
        b = np.array([[[1, 0], [0, 1]], [[0, 1], [0, 1]]])

        with self.assertRaises(ValueError):
            dotprod(a, b)

    def test_raise_shape_match_error(self):
        """Tests whether an error is thrown when b doesn't match a."""

        # B has more rows than a has columns!
        a = np.array([[1, 0], [0, 1]])
        b = np.array([[4, 1], [2, 2], [2, 2]])

        # Check if error is raised
        with self.assertRaises(ValueError):
            dotprod(a, b)

    def test_multiplication(self):
        """Test the multiplication itself."""

        # Define matrix content.
        a = np.array([[1, 0], [0, 1]])
        b = np.array([[4, 1], [2, 2]])

        # Check result
        self.assertTrue(np.all(np.array([[4, 1], [2, 2]] == matmul(a, b))))


class TestMM(unittest.TestCase):
    """"A sample tests class to check if your modules' functions are
    functioning."""

    def test_raise_method_error(self):
        """Tests if error is raised when either A or B does not have 2
        dimensions, but here mainly for class initiation. As the methods
        themselves are already proven to work."""

        # A does not have 2 dimensions
        a = np.array([[[1, 0], [0, 1]], [[0, 1], [0, 1]]])
        b = np.array([[4, 1], [2, 2]])

        # Assign wrong method to raise error
        method = "blub"

        with self.assertRaises(ValueError):
            MM = MatrixMultiplication(a, b, method=method)

        # Assign right method to check for size error
        method = "matmul"
        with self.assertRaises(ValueError):
            MM = MatrixMultiplication(a, b, method=method)
            MM()

        # B does not have 2 dimensions
        a = np.array([[1, 0], [0, 1]])
        b = np.array([[[1, 0], [0, 1]], [[0, 1], [0, 1]]])

        with self.assertRaises(ValueError):
            MM = MatrixMultiplication(a, b, method=method)
            print(MM())


if __name__ == "__main__":
    unittest.main()
