#!/usr/bin/python3
"""Task 8 create a parent class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle
    """
    def __init__(self, width, height):
        """init class"""
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
        super().__init__()

    def area(self):
        """ empty class"""
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] " + str(self.__width) + "/" + str(self.__height))


class Square(Rectangle):
    """ Square class
    """
    def __init__(self, size):
        """constructor of Square"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size * self.__size
