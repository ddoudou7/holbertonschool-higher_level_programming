#!/usr/bin/python3
"""
5-save_to_json_file.py
"""

import json

def save_to_json_file(my_obj, filename):
    """
    Écrit l’objet my_obj dans le fichier filename
    en utilisant sa représentation JSON.

    Args:
        my_obj: Objet Python à sérialiser (liste, dict, etc.).
        filename: Nom du fichier où écrire le JSON.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
