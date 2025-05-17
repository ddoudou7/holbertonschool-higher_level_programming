#!/usr/bin/python3
"""
This is the "0-add_integer" module.

The 0-add_integer module supplies one function, add_integer().
It adds two integers or floats, returning an integer.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, returning an integer.

    Args:
        a: The first number.
        b: The second number (default is 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
