#!/usr/bin/python3
"""Task 7 create a parent class"""


class BaseGeometry():
    """create a parent class
    """
    def area(self):
        """ empty class"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator return error if value es not an integer

        Args:
        name(string): name of the variable
        value(int): value to check
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0:
            raise ValueError(name + " must be greater than 0")
