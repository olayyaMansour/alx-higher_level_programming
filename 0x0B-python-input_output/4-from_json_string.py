#!/usr/bin/python3
"""
This module provides a function to return an object.
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure) represented by a JSON string.

    :param my_str: The JSON string to be converted to an object
    :return: The object represented by the JSON string
    """
    return json.loads(my_str)
