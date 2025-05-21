#!/usr/bin/python3
"""This module defines a Square class with validated size and area method."""


class Square:
    """A class that defines a square by its size and can compute area."""

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (default is 0).
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
