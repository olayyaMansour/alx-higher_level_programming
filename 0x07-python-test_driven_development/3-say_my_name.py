#!/usr/bin/python3
"""
This module contains a function for printing a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a formatted string with the person's name.

    :param first_name: The first name as a string.
    :param last_name: The last name as a string (default is an empty string).
    :return: None
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
