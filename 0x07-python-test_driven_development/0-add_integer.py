#!/usr/bin/python3
"""
This module contains a function that adds two integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number (default is 98).

    Returns:
    int: The addition of a and b.

    Raises:
    TypeError: If a or b is not an integer or float.

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> try:
    ...     add_integer(4, "School")
    ... except Exception as e:
    ...     str(e)
    'b must be an integer'
    >>> try:
    ...     add_integer(None)
    ... except Exception as e:
    ...     str(e)
    'a must be an integer'
    """

    # Check if a is not an int or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    # Check if b is not an int or float
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast a and b to integers and perform the addition
    return int(a) + int(b)

if __name__ == "__main__":
    # Example usage
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))

    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)

    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
