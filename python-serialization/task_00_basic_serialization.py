#!/usr/bin/python3
"""Module for basic JSON serialization and deserialization"""

import json

def serialize_and_save_to_file(data, filename):
    """Serializes a dictionary and saves it to a JSON file"""
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Loads JSON data from a file and returns it as a dictionary"""
    with open(filename, "r") as f:
        return json.load(f)

