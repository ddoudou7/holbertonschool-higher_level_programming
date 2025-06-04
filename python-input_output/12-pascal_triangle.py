#!/usr/bin/python3
"""
12-pascal_triangle.py
"""

def pascal_triangle(n):
    """
    Retourne la liste des listes représentant le triangle de Pascal
    de hauteur n.

    Si n <= 0, renvoie une liste vide.
    On suppose que n est toujours un entier.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # première ligne

    for i in range(1, n):
        prev_row = triangle[i - 1]
        row = [1]  # chaque ligne commence par 1
        # calculer les valeurs du milieu
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        row.append(1)  # chaque ligne se termine par 1
        triangle.append(row)

    return triangle
