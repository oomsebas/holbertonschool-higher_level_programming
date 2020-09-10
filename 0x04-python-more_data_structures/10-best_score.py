#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    b = a_dictionary
    a = [k for k, v in b.items() if v == max(list(b.values()))]
    return (a[0])
