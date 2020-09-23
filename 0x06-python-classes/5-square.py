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

    @property
    def size(self):
        """Get the size class variable"""
        return self.__size * 1

    @size.setter
    def size(self, value):
        """Set a private class variable"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        """print the area"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()
