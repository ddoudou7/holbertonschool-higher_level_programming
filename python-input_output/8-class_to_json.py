#!/usr/bin/python3
"""
Module 8-class_to_json
Returns the dictionary description for JSON serialization of an object.
"""

def class_to_json(obj):
    """
    Returns the __dict__ of an object, i.e. all its attributes as a dictionary.
    """
    return obj.__dict__
