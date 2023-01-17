#!/usr/bin/python3
"""
7-error_code module
    This scripts prints out the body of a POST HTTP response and handle error
    code using the
    `requests` module
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    res = requests.post(url)
    if (int(res.status_code) >= 400):
        print('Error: {}'.format(res.status_code))
    else:
        print(res.text)
