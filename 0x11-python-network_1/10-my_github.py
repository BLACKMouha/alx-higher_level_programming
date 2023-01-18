#!/usr/bin/python3
"""10-my_github module
    This script takes GitHub credentials (username and password) and uses the
    GitHub API to display the id
"""


if __name__ == '__main__':
    from sys import argv
    from requests import get
    from requests.auth import HTTPBasicAuth

    url = 'https://api.github.com/user'
    auth = HTTPBasicAuth(argv[1], argv[2])
    res = get(url, auth=auth)
    print(res.json().get('id'))
