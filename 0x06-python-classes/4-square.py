#!/usr/bin/python3
"""defines a square class."""


class Square:
    """a square."""

    def __init__(self, size=0):
        """square initialized.
        Args:
            size: length of side of the square.
        """
        self.__size = size

        @property
        def size(self):
            """ size of a square."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

        def area(self):
            """Area of the square."""
            return (self.__size ** 2)
