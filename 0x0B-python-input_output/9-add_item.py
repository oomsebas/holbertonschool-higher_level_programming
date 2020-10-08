#!/usr/bin/python3
"""Task 9 load and write ti json file"""


from sys import argv
import json
import os.path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"
if os.path.isfile(filename):
    obj = load_from_json_file(filename)
else:
    obj = []
obj.extend(argv[1:])
save_to_json_file(obj, filename)
