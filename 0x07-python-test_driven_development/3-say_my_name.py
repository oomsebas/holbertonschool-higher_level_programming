#!/usr/bin/python3
"""Module that prints  My name  is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Function that prints My name is <first name> <last name>

    Args:
        first_name (str): The first name to print.
        last_name (str): The last name to print.

    Returns:
       None
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
