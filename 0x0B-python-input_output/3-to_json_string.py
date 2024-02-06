#!/usr/bin/python3
"""
This module provides a function to return a JSON object.
"""

import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).

    :param my_obj: The object to be converted to JSON
    :return: JSON representation of the object as a string
    """
    return json.dumps(my_obj)
