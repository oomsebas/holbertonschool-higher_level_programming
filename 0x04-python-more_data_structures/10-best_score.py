#!/usr/bin/python3
def best_score(a_dictionary):
    a = None
    if a_dictionary is None:
        a = max(a_dictionary, key=a_dictionary.get)
    return a
