#!/usr/bin/python3
""" list repositories of a user using github API"""
if __name__ == '__main__':
    import requests
    from sys import argv
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(argv[2], argv[1]))
    commits = r.json()
    for commit in commits[0:10]:
        print(commit.get('sha'), end=": ")
        author = commit['commit']['author'].get('name')
        print(author)
