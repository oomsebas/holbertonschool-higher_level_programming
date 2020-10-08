#!/usr/bin/python3
"""Task 10 class to json"""


import json


def class_to_json(obj):
    """function that turn objet dict to json"""
    return (json.dumps(obj.__dict__))
