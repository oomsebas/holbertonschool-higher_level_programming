#!/usr/bin/python
"""Task 0 read a file and print to stdout"""


def read_file(filename=""):
    """Function that reads a file"""
    with open(filename, encoding="UTF-8") as Myfile:
        print(Myfile.read(), end='')
