#!/usr/bin/python3
def text_indentation(text):
    """Prints text with 2 new lines after '.', '?', and ':' characters"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""
    if buffer.strip():
        print(buffer.strip())
