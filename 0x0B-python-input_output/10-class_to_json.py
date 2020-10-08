#!/usr/bin/python3
"""Task 10 class to json"""


to_json_string = __import__('5-to_json_string').to_json_string


def class_to_json(obj):
    """function that turn objet dict to json"""
    return (to_json_string(obj.__dict__))
