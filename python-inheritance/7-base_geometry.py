#!/usr/bin/python3
"""Defines BaseGeometry."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that *value* is a strictly positive integer."""
        if type(value) is not int:              # ← test de type STRICT
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
