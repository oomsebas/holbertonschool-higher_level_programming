#!/usr/bin/python3
"""
 requests header content to a page and retrives a variable
"""
import urllib.request as request
from sys import argv
if __name__ == "__main__":
    req = request.Request(argv[1])
    with request.urlopen(req) as response:
        print(response.headers.get("X-Request-Id"))
