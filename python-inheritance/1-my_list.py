#!/usr/bin/python3
"""Defines the MyList class inheriting from list."""


class MyList(list):
    """List subclass that prints itself sorted."""

    def print_sorted(self):
        """Print the list in ascending order without modifying it."""
        print(sorted(self))
