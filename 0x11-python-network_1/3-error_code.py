#!/usr/bin/python3
"""3-error_code module
    This script displays the body of a request and handles HTTP errors too.
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    from urllib.error import HTTPError

    url = argv[1]
    req = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(req) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print('Error code:', e.code)
