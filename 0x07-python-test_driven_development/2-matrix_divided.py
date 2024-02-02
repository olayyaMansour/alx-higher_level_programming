#!/usr/bin/python3
"""
This module contains a function for dividing all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    :param matrix: A list of lists containing integers or floats.
    :param div: The number to divide each element of the matrix by.
    :return: A new matrix with elements rounded to 2 decimal places.
    """
    if not all(isinstance(row, list) for row in matrix) or not all(
        all(isinstance(el, (int, float)) for el in row) for row in matrix
    ):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [[round(el / div, 2) for el in row] for row in matrix]
    return result_matrix
