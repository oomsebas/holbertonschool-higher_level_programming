#!/usr/bin/python3
"""Task 3 determine class and parent"""


def is_kind_of_class(obj, a_class):
    """Write a function that returns True if the object is an instance
    of, or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False."""
    return isinstance(obj, a_class)
