#!/usr/bin/python3
"""
Module 0-read_file
Reads and prints the contents of a text file (UTF8).
"""

def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str): Name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
