#!/usr/bin/python3
"""
This module provides a function to append a string to the end of a text file
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a file.

    :param filename: Name of the file to be appende
    :param text: The string to be appended to the file
    :return: The number of characters added
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        return file.write(text)
