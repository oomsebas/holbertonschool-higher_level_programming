#!/usr/bin/python3
"""Empty class Square: defines the square of a number
"""


class Square:
    """initialization method with  private class variable size"""
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """ method that squares the size"""
        return self.__size ** 2
