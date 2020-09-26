#!/usr/bin/python3
""" script for task 0, we define a subroutine that adds two numbers and test
them using doctest module"""


def add_integer(a, b=98):
    """function that adds two integers
    Args:
    a(int): first number to be sumed
    b(int): second number to be summed

    Return:
    the adittion of a and b
    """
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    elif type(a) is not int:
        raise TypeError("a must be an integer")
    elif type(b) is not int:
        raise TypeError("b must be an integer")
    return a + b
