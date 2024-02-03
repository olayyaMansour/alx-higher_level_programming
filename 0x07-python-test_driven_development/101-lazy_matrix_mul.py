#!/usr/bin/python3
"""
Defines a function that multiplies two matrices using NumPy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   or if one element is not an integer or a float.
        ValueError: If m_a or m_b is empty, or if m_a and m_b can't be multiplied.

    Returns:
        list: The resulting matrix.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")

    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")

    if not all(isinstance(el, (int, float)) for row in m_a for el in row) or not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")

    if all(len(row) == 0 for row in m_a) or all(len(row) == 0 for row in m_b):
        raise ValueError("m_a can't be empty or m_b can't be empty")

    if not all(len(row) == len(m_a[0]) for row in m_a) or not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = np.dot(m_a, m_b)
    return result.tolist()
