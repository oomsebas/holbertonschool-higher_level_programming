#!/usr/bin/python3
"""Empty class Square: defines the square of a number
"""


class Square:
    """initialization method with  private class variable size"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
        if type(position[0]) is not int or type(position[1]) is not int:
            TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            TypeError("position must be a tuple of 2 positive integers")
        elif len(position) is not 2 or type(position) is not tuple:
            TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        left_pos = self.__position[0]
        print("\n" * self.__position[1], end="")
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print("#" * self.__size, end="")
            print()

    @property
    def position(self):
        """Getter for position variable"""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position private instance attribute"""
        if type(value[0]) is not int or type(value[1]) is not int:
            TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2 or type(value) is not tuple:
            TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value
