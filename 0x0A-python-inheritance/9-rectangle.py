#!/usr/bin/python3
"""Module for Rectangle class with implemented area method."""


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry with area method."""
    def __init__(self, width, height):
        """Instantiation with width and height."""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
