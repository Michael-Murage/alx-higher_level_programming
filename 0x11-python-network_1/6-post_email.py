#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request
 to the passed URL with the email as a parameter, and
 finally displays the body of the response.
"""


if __name__ == '__main__':
    from sys import argv
    from requests import post

    res = post(argv[1], data={email: argv[2]})
    print(res.text)
