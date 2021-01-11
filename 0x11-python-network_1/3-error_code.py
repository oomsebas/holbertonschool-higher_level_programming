#!/usr/bin/python3
"""
 requests header content to a page and retrives a variable
"""
import urllib.request as request
import urllib.parse as parse
import urllib.error as error
from sys import argv
if __name__ == "__main__":
    req = request.Request(argv[1])
    try:
        with request.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except error.URLError as e:
        print("Error code: {}".format(e.code))
