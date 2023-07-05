#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    q = argv[1] or ""
    res = post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json = res.json()
        if json == {}:
            print('No result')
        else:
            print('[{}] {}'.format(json.get('id'), json.get('name')))
    except ValueError:
        print('Not a valid JSON')
