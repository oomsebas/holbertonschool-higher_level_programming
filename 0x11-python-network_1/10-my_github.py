#!/usr/bin/python3
""" Authentication in git hub wit url request """
if __name__ == "__main__":
    import requests
    from sys import argv

    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get('id'))
