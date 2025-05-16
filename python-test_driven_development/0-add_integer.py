#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer().
It adds two integers or floats, returning an integer.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats, casts to int if needed.

    Args:
        a: first number
        b: second number, default is 98

    Returns:
        int: the sum of a and b

    Raises:
        TypeError: if a or b are not int or float

    Example:
    >>> add_integer(2, 3)
    5
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
