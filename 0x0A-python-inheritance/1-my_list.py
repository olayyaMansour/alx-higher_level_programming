#!/usr/bin/python3
"""Module for MyList class."""


class MyList(list):
    """MyList class that inherits from list."""

    def print_sorted(self):
        """Prints the list in ascending order."""
        sorted_list = sorted(self)
        print(sorted_list)
