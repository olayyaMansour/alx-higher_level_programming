#!/usr/bin/python3
"""
This module provides a function to read and print the content of a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    :param filename: Name of the file to be read (default is an empty string)
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
