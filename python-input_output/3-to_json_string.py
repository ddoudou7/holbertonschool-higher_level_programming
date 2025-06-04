#!/usr/bin/python3
"""
Module 3-to_json_string
Returns the JSON representation of an object (string).
"""

import json

def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    
    Args:
        my_obj: The object to convert to JSON string.
    
    Returns:
        str: JSON string representation.
    """
    return json.dumps(my_obj)
