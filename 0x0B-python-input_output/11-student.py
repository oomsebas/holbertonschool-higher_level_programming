#!/usr/bin/python3
"""task 11 create a class"""


class Student:
    """ class student
    """
    def __init__(self, first_name, second_name, age):
        """init method"""
        self.first_name = first_name
        self.second_name = second_name
        self.age = age

    def to_json(self):
        """to json"""
        return self.__dict__
