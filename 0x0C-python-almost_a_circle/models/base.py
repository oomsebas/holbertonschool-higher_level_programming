#!/usr/bin/python3
"""Task 1 create a base class"""

import json


class Base:
    """Class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """json representation of a class"""
        if not list_dictionaries or list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        list_dictionaries = []
        for _obj_dict in list_objs:
            list_dictionaries.append(_obj_dict.to_dictionary())

        with open(cls.__name__ + ".json", "w") as _file:
                json.dump(list_dictionaries, _file)
        _file.close()

    @staticmethod
    def from_json_string(json_string):
        """the list of the JSON string representation json_string"""
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance according to **dictionary"""
        r1 = cls(5, 5, 0, 0)
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        """reads from a file and creates the intances"""
        list_obj = []
        with open(cls.__name__ + ".json", "r") as _file:
            str_json = _file.read()
        _file.close()
        dict = Base.from_json_string(str_json)
        for obj in dict:
            list_obj.append(cls.create(**obj))
        return(list_obj)
