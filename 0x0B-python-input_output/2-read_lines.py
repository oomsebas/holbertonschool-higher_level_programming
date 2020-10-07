#!/usr/bin/pyhton3
"""Task 2 read lines"""


def read_lines(filename="", nb_lines=0):
    """function to read a number of lines"""
    with open(filename, encoding="UTF-8") as _file:
        if nb_lines <= 0:
            for line in _file:
                print(line, end='')
        else:
            for line in range(nb_lines):
                print(_file.readline(), end='')
