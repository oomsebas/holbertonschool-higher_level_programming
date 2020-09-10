#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_cpy = {}
    for k, v in sorted(a_dictionary.items()):
        print("{}: {}".format(k, v))
