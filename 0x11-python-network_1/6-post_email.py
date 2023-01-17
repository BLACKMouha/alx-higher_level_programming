#!/usr/bin/python3
"""
6-post_email module
    This scripts prints out the body of a POST HTTP response using the
    `requests` module
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    email = argv[2]
    res = requests.post(url, data={'email': email})
    print(res.text)
