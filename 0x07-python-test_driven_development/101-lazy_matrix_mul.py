#!/usr/bin/python3

"""Define a matrix multiplication function."""
import numpy as np


def lazy_matrix_mul(matrix_a, matrix_b):
    """Return a multiplication of two matrices.
    Args:
        matrix_g (list of lists of ints/floats): The first matrix.
        matrix_b (list of lists of ints/floats): The second matrix.
    """

    return np.matmul(matrix_a, matrix_b)
