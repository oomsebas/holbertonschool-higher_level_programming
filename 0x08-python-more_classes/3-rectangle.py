#!/usr/bin/pyhton3
""" Create a empty class for a rectangle"""


class Rectangle:
    """ Class rectangle"""
    def __init__(self, width=0, height=0):
        """init method"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Method that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Method that returns the perimeter of the rectangle"""
        return 2 * (self.__width + self.__height)

    def __str__(self):
        square = ""
        for i in range(self.__height - 1):
            square += (self.__width * "#") + "\n"
        square += (self.__width * "#")
        return square
