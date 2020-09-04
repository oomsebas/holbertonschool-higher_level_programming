#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':

    if len(argv) == 1:
        print("0 arguments.")

    else:
        print("{} arguments:".format(len(argv) - 1))
        for index, args in enumerate(argv[1:], 1):
                print("{}: {}".format(index, argv[index]))
