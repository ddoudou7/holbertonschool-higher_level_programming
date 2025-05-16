#!/usr/bin/python3
def text_indentation(text):
    """Print a text with two new lines after each '.', '?', or ':' character."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    start = 0
    for i, char in enumerate(text):
        if char in ".?:":
            line = text[start:i + 1].strip()
            print(line)
            print()
            start = i + 1
    if start < len(text):
        print(text[start:].strip(), end="")
