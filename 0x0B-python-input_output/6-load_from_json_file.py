#!/usr/bin/python3
"""
This module provides a function to create an object from a JSON file.
"""


import json

def load_from_json_file(filename):
    """
    Creates an object from a JSON file.

    :param filename: The name of the JSON file
    :return: The object created from the JSON file
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        return json.load(file)
