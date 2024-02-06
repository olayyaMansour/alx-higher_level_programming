#!/usr/bin/python3
"""
This module defines a Student class.
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

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.

        :return: A dictionary representation of the student
        """
        return self.__dict__
