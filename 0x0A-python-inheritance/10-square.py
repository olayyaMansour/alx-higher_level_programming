#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Instantiation with size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
