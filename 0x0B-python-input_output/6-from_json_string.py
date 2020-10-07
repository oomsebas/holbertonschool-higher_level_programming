#!/usr/bin/python3
"""Task 6 from str to json"""


import json


def from_json_string(my_str):
    """function that converts form Json string to data object"""
    return json.loads(my_str)
