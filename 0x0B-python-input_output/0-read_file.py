#!/usr/bin/python3
"""Task 0 read a file and print to stdout"""


def read_file(filename=""):
    """Function that reads a file"""
    with open(filename, encoding="utf-8") as Myfile:
        for line in Myfile:
            print(line, end='')
