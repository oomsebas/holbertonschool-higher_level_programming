#!/usr/bin/python3
""" request header content to a page """
from sys import argv
import urllib.request
req = urllib.request.Request(argv[1])
with urllib.request.urlopen(req) as response:
    html2 = response.info()
res = html2.get("X-Request-Id")
print(res)
