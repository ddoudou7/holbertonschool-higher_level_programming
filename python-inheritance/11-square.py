#!/usr/bin/python3
"""
This module defines a Square class inheriting from Rectangle with custom __str__.
"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Square class based on Rectangle with overridden __str__."""

    def __init__(self, size):
        """Initialize the square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)

