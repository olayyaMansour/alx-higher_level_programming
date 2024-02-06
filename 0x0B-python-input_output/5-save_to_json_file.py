#!/usr/bin/python3
"""
This module provides a function to write an Object to a text file.
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.

    :param my_obj: The object to be saved to the file
    :param filename: The name of the file to save the object to
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file)
