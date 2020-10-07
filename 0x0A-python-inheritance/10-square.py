#!/usr/bin/python3
"""Task 8 create a parent class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class
    """
    def __init__(self, size):
        """constructor of Square"""
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)
