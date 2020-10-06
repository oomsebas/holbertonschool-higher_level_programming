#!/usr/bin/python3
"""Task 1, write a class myList that inherits from lists"""


class MyList(list):
    """Definition of a class Mylist which inherits from list"""

    def print_sorted(self):
        """ function that prints a sorted list"""
        print(sorted(self))
