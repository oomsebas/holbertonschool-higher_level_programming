#!/usr/bin/python3
"""
 requests header content to a page and retrives a variable
"""
import urllib.request as request
import urllib.parse as parse
from sys import argv
if __name__ == "__main__":
    values = {'email': argv[2]}
    data = parse.urlencode(values).encode('utf-8')
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
