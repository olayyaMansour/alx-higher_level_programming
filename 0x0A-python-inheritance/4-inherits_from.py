#!/usr/bin/python3
"""Module for inherits_from function."""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise, False.

    Args:
        obj: The object to check.
        a_class: The class to compare with.

    Returns:
        True if obj is an instance of a subclass of a_class, otherwise False.
    """

    return issubclass(type(obj), a_class) and type(obj) != a_class
