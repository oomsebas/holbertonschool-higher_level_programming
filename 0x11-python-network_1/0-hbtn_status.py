#!/usr/bin/python3
""" request content to a pagae """
import shutil
import tempfile
import urllib.request
req = urllib.request.Request('https://intranet.hbtn.io/status')
with urllib.request.urlopen(req) as response:
    html2 = response.read()
print("Body response:")
print("\t- type: {}".format((type(html2))))
print("\t- content: {}".format(html2))
print("\t- utf8 content: {}".format(html2.decode('utf-8')))
