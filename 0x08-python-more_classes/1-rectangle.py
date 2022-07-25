#!/usr/bin/python3
"""Defines a Rectangle class.
"""


class Rectangle:
    """Rectangle class defined by width and height."""

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle instance.
        Args:
            width: width of the rectangle
            height: height of the rectangle
        """
        self.width = width
        self.height = height

        @property
    def width(self):
        """gets the width of a Rectangle instance."""
        return self.__width

        @width.setter
    def width(self, value):
        """Sets the width of a Rectangle instance
        Args:
            value: value of the width
        """
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

        @property
    def height(self):
        """gets the height of a Rectangle instance."""
        return self.__height

        @height.setter
    def height(self, value):
        """Sets the height of a Rectangle instance
        Args:
            value: value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
