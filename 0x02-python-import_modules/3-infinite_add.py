#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':

    args = 0
    for i in argv[1:]:
        args = args + int(i)
    print(args)
