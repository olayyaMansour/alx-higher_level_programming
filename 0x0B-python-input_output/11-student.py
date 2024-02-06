#!/usr/bin/python3
"""
This module defines a Student class with reload from JSON.
"""


class Student:
    """
    Defines a student with first_name, last_name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        :param first_name: The first name of the student
        :param last_name: The last name of the student
        :param age: The age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.

        :param attrs: List of attributes to include in the dictionary
        :return: A dictionary representation of the student
        """
        if attrs is None:
            return self.__dict__
        return {key: getattr(self, key) for key in attrs if hasattr(self, key)}

    def reload_from_json(self, json):
        """
        Replaces all attributes Student instance with a provided dictionary.

        :param json: The dictionary representation of the student
        """
        for key, value in json.items():
            setattr(self, key, value)
