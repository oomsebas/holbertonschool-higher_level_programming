#!/usr/bin/python3
"""task 3 write to a file"""


def write_file(filename="", text=""):
    """function that writes to a file"""
    lines_wrote = 0
    with open(filename, "w", encoding="UTF-8") as _file:
        lines_wrote = _file.write(text)
        return lines_wrote
