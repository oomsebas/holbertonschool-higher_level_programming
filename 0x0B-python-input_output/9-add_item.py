#!/usr/bin/python3

from sys import argv
import json
import os.path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    _list = load_from_json_file(filename)
else:
    _list = []
_list.extend(argv[1:])
save_to_json_file(_list, "additem.json")
