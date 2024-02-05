#!/usr/bin/python3
"""Defines a function to add a new attribute to an object."""


def add_attribute(obj, attribute, value):
    """Adds a new attribute to an object if possible.

    Args:
        obj (object): The object to add the attribute to.
        attribute (str): The name of the new attribute.
        value (any): The value of the new attribute.

    Raises:
        TypeError: If the object cannot have a new attribute.
    """
    # Check if the object has __dict__ attribute
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")

    # Add the new attribute to the object
    obj.__dict__[attribute] = value
