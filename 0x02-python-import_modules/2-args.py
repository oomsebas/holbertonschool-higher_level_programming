#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':

    lenght = len(argv) - 1
    if lenght == 0:
        print("0 arguments.")
    elif lenght == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv) - 1))

    for index, args in enumerate(argv[1:], 1):
        print("{}: {}".format(index, argv[index]))
