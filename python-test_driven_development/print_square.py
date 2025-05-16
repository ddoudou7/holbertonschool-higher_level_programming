#!/usr/bin/python3
"""
This module defines the function print_square which prints a square with "#"
"""
def print_square(size):
    """Prints a square with "#" of size `size`."""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
