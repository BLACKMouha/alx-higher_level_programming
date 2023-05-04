#!/usr/bin/python3
'''
Sends a requests to a URL passed as argument and displays the body or an error
'''

from requests import get
from requests.exceptions import HTTPError, RequestException, ConnectionError
from sys import argv


if __name__ == '__main__':
    try:
        r = get(argv[1])
        r.raise_for_status()
        print(r.text)
    except (ConnectionError, RequestException, HTTPError):
        print("Error code:", r.status_code)
