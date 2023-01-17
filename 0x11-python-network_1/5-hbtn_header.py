#!/usr/bin/python3
"""
5-hbtn_header module
    This scripts prints out 'X-Request-Id' of a HTTP response using the
    `requests` module
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    res = requests.get(url)
    print(res.headers.get('X-Request-Id'))