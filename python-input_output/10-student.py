#!/usr/bin/python3
"""Defines a Student class with a filtered to_json method."""

class Student:
    """Représente un étudiant avec un prénom, nom et âge."""

    def __init__(self, first_name, last_name, age):
        """
        Initialise une nouvelle instance Student.

        Args:
            first_name (str): Prénom de l'étudiant.
            last_name (str): Nom de l'étudiant.
            age (int): Âge de l'étudiant.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retourne un dictionnaire reprenant les attributs de l'instance.

        Si attrs est une liste de chaînes, ne renvoie que les attributs
        dont le nom figure dans cette liste et qui existent réellement.
        Sinon, renvoie tous les attributs.

        Args:
            attrs (list, optional): Liste de noms d'attributs à inclure.

        Returns:
            dict: Dictionnaire de paires "attribut": valeur.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            filtered = {}
            for attr in attrs:
                if hasattr(self, attr):
                    filtered[attr] = getattr(self, attr)
            return filtered
        # Sinon, on renvoie tous les attributs
        return self.__dict__
