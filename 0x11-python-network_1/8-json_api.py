#!/usr/bin/python3
""" Creates a request with resques package """
import requests
from sys import argv
if __name__ == '__main__':
        if len(argv) <= 1 or len(argv[1]) is 0:
                dict1 = {'q': ''}
        else:
                dict1 = {'q': argv[1]}
        url = 'http://f29444c84915.87bf5168.hbtn-cod.io:5000/search_user'
        url1 = 'http://0.0.0.0:5000/search_user'
        r = requests.post(url1, data=dict1)
        try:
                text = r.json()
                id = text.get('id')
                name = text.get('name')
                if len(text) is 0 or not id or not name:
                        print("Not result")
                else:
                        print("[{}] {}".format(id, name))
        except ValueError:
                print("Not a valid JSON")
