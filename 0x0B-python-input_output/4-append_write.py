#!/usr/bin/python3
""" Task 4 append to a file"""


def append_write(filename="", text=""):
    """fiuction that appends to a file"""
    with open(filename, "a", encoding="utf-8") as _file:
        num_lines = 0
        num_lines = _file.write(text)
        return num_lines
