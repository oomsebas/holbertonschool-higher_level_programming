#!/usr/bin/python3
""" Creates a request with resques package """
import requests
from sys import argv
if __name__ == '__main__':
        if len(argv) is 1:
                dict1 = {'q': ""}
        else:
                dict1 = {'q': argv[1]}
        url = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url, data=dict1)
        try:
                text = r.json()
                if len(text) is 0:
                        print("Not result")
                else:
                        print("[{}] {}".format(text.get('id'),
                                               text.get('name')))
        except ValueError:
                print("Not a valid JSON")
