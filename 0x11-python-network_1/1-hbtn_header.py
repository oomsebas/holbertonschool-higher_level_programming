#!/usr/bin/python3
""" request header content to a page """
import urllib.request
from sys import argv
req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    html2 = response.info()
res = html2.get("X-Request-Id")
print(res)
