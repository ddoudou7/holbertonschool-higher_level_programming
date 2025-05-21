#!/usr/bin/python3
"""This module defines a Square class with size getter and setter."""


class Square:
    """A class that defines a square by its size and can compute area."""

    def __init__(self, size=0):
        """Initialize a new Square instance with size validation."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size ** 2
