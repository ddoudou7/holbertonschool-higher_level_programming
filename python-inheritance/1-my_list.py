#!/usr/bin/python3
"""
This module defines a class MyList that inherits from list and adds a method to print the list sorted.
"""

class MyList(list):
    """Subclass of list with a sorted print method."""

    def print_sorted(self):
        """Print the list sorted in ascending order (without modifying it)."""
        print(sorted(self))

