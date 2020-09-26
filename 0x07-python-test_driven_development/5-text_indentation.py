#!/usr/bin/python3
"""Task 5 text indentation"""


def text_indentation(text):
    """Write a function that prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text(str): The text string to make the indentation.

    Return:
       None
    """
    prev = 0
    if type(text) is not str:
        raise TypeError("text must be a string")
    for num, i in enumerate(text):
        if (i == '.' or i == ':' or i == '?') and num != len(text):
            print(text[prev: num + 1].strip())
            print()
            prev = num + 1
    print(text[prev:num + 1].strip(), end="")
