#!/usr/bin/python3
""" request content to a pagae """
import urllib.request
import sys
req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    html2 = response.headers
res = html2.get("X-Request-Id")
print(res)
