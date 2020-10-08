#!/usr/bin/python3
"""task 11 create a class"""


class Student:
    def __init__(self, first_name, last_name, age):
        """init method"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to json"""
        dict = {}
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        if all(isinstance(s, str) for s in attrs):
            for inst in attrs:
                dict[inst] = self.__dict__.get(inst)
            return dict
        else:
            return self.__dict__
