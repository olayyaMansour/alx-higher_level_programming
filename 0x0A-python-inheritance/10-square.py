#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Instantiation with size."""
        super().__init__(size, size)

    def __str__(self):
        """Return the square description."""
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
