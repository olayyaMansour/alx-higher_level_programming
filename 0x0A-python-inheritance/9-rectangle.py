#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle using the BaseGeometry class."""

    def __init__(self, width, height):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
        """
        # Validate and set the width using the integer_validator method from the parent class
        super().integer_validator("width", width)
        self.__width = width
        
        # Validate and set the height using the integer_validator method from the parent class
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return a string representation of the Rectangle for print() and str()."""
        # Create a formatted string representation with class name, width, and height
        string_representation = f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
        return string_representation
