#!/usr/bin/python3
def best_score(a_dictionary):
    a = None
    if a_dictionary:
        a = max(a_dictionary, key=a_dictionary.get)
    return a
