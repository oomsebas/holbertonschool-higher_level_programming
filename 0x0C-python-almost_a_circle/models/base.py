#!/usr/bin/python3
"""Task 1 create a base class"""

import json
import os
import csv


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
        if not list_dictionaries:
            return "[]"
        if (type(list_dictionaries) != list or
           not all(type(x) == dict for x in list_dictionaries)):
            raise TypeError("list_dictionaries must be a list of dictionaries")
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        list_dictionaries = []
        if list_objs is None or list_objs == []:
            string_dictionary = "[]"
        else:
            for _obj_dict in list_objs:
                list_dictionaries.append(_obj_dict.to_dictionary())
            string_dictionary = Base.to_json_string(list_dictionaries)
        with open(cls.__name__ + ".json", "w") as _file:
                _file.write(string_dictionary)
        _file.close()

    @staticmethod
    def from_json_string(json_string):
        """the list of the JSON string representation json_string"""
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """creates an instance according to **dictionary"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """reads from a file and creates the intances"""
        list_obj = []
        if os.path.exists(cls.__name__ + ".json"):
            with open(cls.__name__ + ".json", "r") as _file:
                str_json = _file.read()
                _file.close()
                _dict = Base.from_json_string(str_json)
                for obj in _dict:
                    list_obj.append(cls.create(**obj))
        return(list_obj)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """JSON string representation of list_objs to a file"""
        list_dictionaries = []
        if list_objs is None or list_objs == []:
            string_dictionary = "[]"
        else:
            for _obj_dict in list_objs:
                list_dictionaries.append(_obj_dict.to_dictionary())
            string_dictionary = Base.to_json_string(list_dictionaries)
        with open(cls.__name__ + ".csv", "w") as _file:
                _file.write(string_dictionary)
        _file.close()

    @classmethod
    def load_from_file_csv(cls):
        """reads from a file and creates the intances"""
        list_obj = []
        if os.path.exists(cls.__name__ + ".csv"):
            with open(cls.__name__ + ".csv", "r") as _file:
                str_csv = _file.read()
                _file.close()
                _dict = Base.from_json_string(str_csv)
                for obj in _dict:
                    list_obj.append(cls.create(**obj))
        return(list_obj)
