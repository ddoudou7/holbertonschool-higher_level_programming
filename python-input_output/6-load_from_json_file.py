#!/usr/bin/python3
"""
6-load_from_json_file.py
"""

import json

def load_from_json_file(filename):
    """
    Crée un objet Python à partir du contenu JSON d'un fichier.

    Args:
        filename (str): Nom du fichier JSON à ouvrir.

    Returns:
        L'objet Python obtenu après désérialisation du JSON.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
