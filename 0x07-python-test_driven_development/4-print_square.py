#!/usr/bin/python3
"""module of a square-printing function."""


def print_square(size):
    """Print a square with the # character.
    Args:
        size: The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print((("#" * size + "\n") * size), end="")
