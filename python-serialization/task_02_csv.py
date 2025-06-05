#!/usr/bin/python3
"""Module to convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts CSV to JSON and writes to 'data.json'"""
    try:
        with open(csv_filename, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)
        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile)
        return True
    except Exception:
        return False
