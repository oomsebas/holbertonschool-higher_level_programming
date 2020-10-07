#!/usr/bin/python3
"""Task 7 json to a file"""


import json


def save_to_json_file(my_obj, filename):
    """function that write json to a file"""
    with open(filename, "w") as _file:
        json.dump(my_obj, _file)
