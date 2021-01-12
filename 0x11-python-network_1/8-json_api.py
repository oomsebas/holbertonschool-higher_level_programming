#!/usr/bin/python3
""" Creates a request with resques package """
import requests
from sys import argv
if __name__ == '__main__':
        if len(argv) == 2:
                q = argv[1]
        else:
                q = ""
        url1 = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url1, data={'q': q})
        try:
                text = r.json()
                id = text.get('id')
                name = text.get('name')
                if len(text) is 0 or not id or not name:
                        print("Not result")
                else:
                        print("[{}] {}".format(id, name))
        except:
                print("Not a valid JSON")
