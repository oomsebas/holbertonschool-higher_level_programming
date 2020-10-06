#!/usr/bin/pyhton3
""" Task 2 determine a exact instance"""


def is_same_class(obj, a_class):
    """ functions that determines if an obj is exact instance
    of a_class

    Args:
    obj: object to be determined
    a_class: the class to compare"""
    if type(obj) ==  a_class:
        return True
    else:
        return False
