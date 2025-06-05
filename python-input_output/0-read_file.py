#!/usr/bin/python3
"""Module for reading and printing the contents of a file."""


def read_file(filename=""):
    """Reads a text file and prints its contents to stdout.

    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
