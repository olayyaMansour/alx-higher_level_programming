#!/usr/bin/python3
"""
This module contains a function that divides all elements of a matrix.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Parameters:
    - matrix (list of lists): The matrix to be divided.
    - div (int or float): The number to divide the matrix elements by.

    Returns:
    list of lists: A new matrix with elements rounded to 2 decimal places.

    Raises:
    - TypeError: If the matrix is not a list of lists of integers or floats,
                 if each row of the matrix is not of the same size,
                 or if div is not a number.
    - ZeroDivisionError: If div is equal to 0.
    """

    # Validate matrix
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Validate row sizes
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Validate div
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Validate div is not 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Perform matrix division and round to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return result_matrix

if __name__ == "__main__":
    # Example usage
    matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]
    print(matrix_divided(matrix, 3))
    print(matrix)
