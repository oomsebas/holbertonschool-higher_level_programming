#!/usr/bin/python3
"""Task 1 count the number of lines of a file"""


def number_of_lines(filename=""):
    """Function to count lines in a file"""
    with open(filename, encoding="utf-8") as _file:
        lines = 0
        while _file.readline() != '':
            lines += 1

        return(lines)
