#!/usr/bin/python3
""" Creates a request to an API  to an url page and return a json"""
if __name__ == '__main__':
    import requests
    from sys import argv
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
        if len(text) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")
