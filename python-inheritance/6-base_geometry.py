#!/usr/bin/python3
"""
This module defines a base class BaseGeometry with an area method.
"""

class BaseGeometry:
    """Base class for geometry-related operations."""

    def area(self):
        """Raise an exception indicating area is not implemented."""
        raise Exception("area() is not implemented")

