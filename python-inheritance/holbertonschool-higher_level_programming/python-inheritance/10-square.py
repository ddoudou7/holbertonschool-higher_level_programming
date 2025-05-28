#!/usr/bin/python3
"""
This module defines a Square class inheriting from Rectangle.
"""

Rectangle = __import__("9-rectangle").Rectangle

class Square(Rectangle):
    """Square class based on Rectangle."""

    def __init__(self, size):
        """Initialize the square with validated size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

