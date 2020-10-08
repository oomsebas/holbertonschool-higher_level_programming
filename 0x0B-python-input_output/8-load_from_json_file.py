#!/usr/bin/python3
"""Task 7 json to a file"""


import json


def load_from_json_file(filename):
    """function that write json to a file"""
    with open(filename, encoding='utf-8') as _file:
        return json.load(_file)
