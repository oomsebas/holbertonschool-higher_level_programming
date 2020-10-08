#!/usr/bin/python3
"""read and write a json object"""
from sys import argv
import json
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

_list = []
try:
    _list = load_from_json_file("additem.json")

except FileNotFoundError:
    save_to_json_file(_list, "additem.json")

finally:
    _list = load_from_json_file("additem.json")
    for item in range(1, len(argv)):
        _list.append(argv[item])

        save_to_json_file(_list, "additem.json")
