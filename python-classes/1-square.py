#!/usr/bin/python3
"""This module defines a Square class with a private size."""


class Square:
    """A class that defines a square by its size."""

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square.
        """
        self.__size = size
