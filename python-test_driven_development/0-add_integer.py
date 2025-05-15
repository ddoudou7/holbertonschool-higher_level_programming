#!/usr/bin/python3
"""
This module provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers.

    Both arguments must be integers or floats, otherwise a TypeError is raised.
    Floats are cast to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
