#!/usr/bin/python3
"""Task 8 create a parent class"""


class BaseGeometry:
    """create a parent class"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ integer validator return error if value es not an integer

        Args:
        name(string): name of the variable
        value(int): value to check
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """class rectangle"""
    def __init__(self, width, height):
        """init class"""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__heigth = height
