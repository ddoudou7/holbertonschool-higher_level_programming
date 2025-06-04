#!/usr/bin/python3
"""
4-from_json_string.py
"""

import json

def from_json_string(my_str):
    """
    Retourne l’objet Python représenté par la chaîne JSON my_str.

    Args:
        my_str (str): Chaîne JSON à désérialiser.

    Returns:
        L’objet Python (list, dict, etc.) correspondant au JSON.
    """
    return json.loads(my_str)
