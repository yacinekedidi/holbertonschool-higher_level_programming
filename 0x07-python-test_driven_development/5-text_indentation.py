#!/usr/bin/python3
"""module text_indentation."""


def text_indentation(text):
    """function text_indentation."""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    text = text.strip()
    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in "?.:":
            print("\n")
            i += 1
            while i < len(text) and text[i] == " ":
                i += 1
            continue
        i += 1
