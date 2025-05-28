#!/usr/bin/python3
"""
This module defines a function that checks if an object is an instance of a class or a subclass.
"""

def is_kind_of_class(obj, a_class):
    """Return True if obj is an instance of a_class or a subclass of it, False otherwise."""
    return isinstance(obj, a_class)

