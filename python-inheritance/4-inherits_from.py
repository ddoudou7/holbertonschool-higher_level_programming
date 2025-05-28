#!/usr/bin/python3
"""
This module defines a function that checks if an object inherits from a given class (excluding the class itself).
"""

def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class, False otherwise."""
    return isinstance(obj, a_class) and type(obj) is not a_class

