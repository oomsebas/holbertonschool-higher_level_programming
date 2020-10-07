#!/usr/bin/python3
"""Task 8 create a parent class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class rectangle
    """
    def __init__(self, width, height):
        """init class"""
        super().__init__()
        self.integer_validator('width', width)
        self.integer_validator('height', height)
        self.__width = width
        self.__height = height
