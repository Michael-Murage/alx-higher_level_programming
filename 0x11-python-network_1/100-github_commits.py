#!/usr/bin/python3
"""
Takes 2 arguments in order to solve this challenge:
Please list 10 commits (from the most recent to oldest)
 of the repository “rails” by the user “rails”
You must use the GitHub API, here is the documentation
 https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


if __name__ == '__main__':
    from sys import argv
    from requests import get

    res = get('https://api.github.com/repos/{}/{}/commits'
        .format(argv[2], argv[1]))
    if res.status_code >= 400:
        print('None')
    else:
        for commit in res.json()[:10]:
            print('{}: {}'
                .format(
                    commit.get('sha'), 
                    commit.get('commit')
                        .get('author')
                        .get('name')
                )
            )
