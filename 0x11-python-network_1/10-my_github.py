#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses
 the GitHub API to display your id
"""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    res = get('https://api.github.com/user', auth=(argv[1], argv[2]))
    if res.status_code >= 400:
        print('None')
    else:
        print(res.json().get('id'))
