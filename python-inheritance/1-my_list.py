#!/usr/bin/python3
"""MyList module
This module defines a subclass of list with a method to print sorted list.
"""

class MyList(list):
    """MyList inherits from list."""

    def __init__(self):
        """Initialize the list."""
        super().__init__()

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
