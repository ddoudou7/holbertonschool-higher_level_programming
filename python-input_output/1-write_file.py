#!/usr/bin/python3
"""
1-write_file.py
"""

def write_file(filename="", text=""):
    """
    Écrit la chaîne `text` dans le fichier `filename` (UTF-8).
    Retourne le nombre de caractères écrits.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
