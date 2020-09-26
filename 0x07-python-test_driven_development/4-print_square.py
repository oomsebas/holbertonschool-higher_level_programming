#!/usr/bin/python3
"""Task 3 Write a function that prints a square with the character #."""


def print_square(size):
    """Function that sqaures with the character #

    Args:
       size(int): the size of the columns and row

    Return:
       None
    """
    square = Square(size)
    square.my_print()


class Square:
    """initialization method with  private class variable size"""
    def __init__(self, size):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

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
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            return

        for i in range(self.__size):
                print(self.__size * "#", end="")
                print()
