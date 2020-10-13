#!/usr/bin/python3
""" Task 10 class for square inherits from rectangle class"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Class that defines a square inherits from Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """Setter method for size"""
        return self.width

    @size.setter
    def size(self, value):
        """Getter method for size"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update method to attribute"""
        assign = ('id', 'size', 'x', 'y')
        if args:
            for key, idx in zip(assign, range(len(args))):
                exec('self.{} = {}'.format(key, args[idx]))
        else:
            for key, val in kwargs.items():
                if key in ('id', 'size', 'x', 'y'):
                    exec('self.{} = {}'.format(key, val))

    def to_dictionary(self):
        """object to dictionary represntation"""
        dict2 = {}
        dict2  = super().to_dictionary()
        del dict2['height']
        dict2['size'] = dict2.pop('width')
        return dict2

    def __str__(self):
        """representation method"""
        return "[" + str(self.__class__.__name__) + "] " + "(" + str(self.id) + ") " + str(self.x) + "/" + str(self.y) + " - " + str(self.width)
