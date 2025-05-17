#!/usr/bin/python3
"""
This is the "0-add_integer" module.

This module provides a function add_integer(a, b=98) that adds
two numbers and returns the result as an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, cast to integers.

    Args:
        a: The first number.
        b: The second number (default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an int or float.

    Example:
    >>> add_integer(2, 3)
    5
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
