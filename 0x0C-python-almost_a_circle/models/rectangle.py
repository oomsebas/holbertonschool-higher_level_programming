#!/usr/bin/python3
""" Task 2, retangle class that ihherits from Base class"""

from models.base import Base


class Rectangle(Base):
    """ class rectangle that inherits from base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(id)
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.integer_validator("x", x)
        self.integer_validator("y", y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """getter method for width object attribute"""
        return self.__width

    @property
    def height(self):
        """getter method for height object attribute"""
        return self.__height

    @property
    def x(self):
        """getter for x"""
        return self.__x

    @property
    def y(self):
        """getter for y"""
        return self.__y

    @x.setter
    def x(self, value):
        """ setter for x"""
        self.integer_validator("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        """setter for y"""
        self.integer_validator("y", value)
        self.__y = value

    @width.setter
    def width(self, value):
        """setter method for width object attribute"""
        self.integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        """setter method for height object attributte"""
        self.integer_validator("height", value)
        self.__height = value

    def integer_validator(self, name, value):
        """ integer validator return error if value es not an integer"""
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        elif value <= 0 and name not in ("x", "y"):
            raise ValueError(name + " must be > 0")
        elif value < 0 and name in ("x", "y"):
            raise ValueError(name + " must be >= 0")

    def area(self):
        """method to calculate the area of the rectangle instance"""
        return self.__width * self.__height

    def display(self):
        """prints in stdout the square with the character #"""
        print("\n" * self.__y, end="")
        for i in range(self.__height):
            print(" " * self.__x, end="")
            print("#" * self.__width, end="")
            print()

    def __str__(self):
        """representation of class Rectangle"""
        return "[" + str(self.__class__.__name__) + "] " + "(" + str(self.id)\
            + ")" + str(self.x) + "/" + str(self.y) + " - " + str(self.width)\
            + "/" + str(self.height)

    def update(self, *args, **kwargs):
        """Method update values in the object"""
        assign = ('id', 'width', 'height', 'x', 'y')
        if args:
            for key, idx in zip(assign, range(len(args))):
                exec('self.{} = {}'.format(key, args[idx]))
        else:
            for key, val in kwargs.items():
                if key in ('id', 'width', 'height', 'x', 'y'):
                    exec('self.{} = {}'.format(key, val))

    def to_dictionary(self):
        """dictionary representation of rectangle"""
        _dict = dict(self.__dict__)
        dict1 = {}
        for key, value in _dict.items():
            dict1[key.replace("_Rectangle__", "")] = value
        return dict1
