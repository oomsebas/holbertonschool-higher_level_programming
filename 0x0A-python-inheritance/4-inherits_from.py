#!/usr/bin/python3
"""Task 4 determine a subclas has direct or indirect attributes"""


def inherits_from(obj, a_class):
    """Write a function that returns True if the object is an instance
    of a class that inherited (directly or indirectly) from the
    specified class ; otherwise False."""
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
