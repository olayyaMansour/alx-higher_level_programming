#!/usr/bin/python3
"""
Defines a function for text indentation.
"""


def text_indentation(text):
    """
    Print a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ['.', '?', ':']
    start = 0
    for i, char in enumerate(text):
        if char in delimiters:
            print(text[start:i+1].strip() + "\n")
            start = i + 1

    if start < len(text):
        print(text[start:].strip(), end="")
