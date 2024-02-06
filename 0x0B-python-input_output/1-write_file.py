#!/usr/bin/python3
"""
This module provides a function to write a string to a text file and return
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of chars.

    :param filename: Name of the file to be written
    :param text: The string to be written to the file
    :return: The number of characters written
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)
