#!/usr/bin/python3
"""2-post_email module
    This script displays the body of a POST request
"""

if __name__ == '__main__':
    from sys import argv
    import urllib.request
    import urllib.parse

    url, email = argv[1], argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as res:
        body = res.read()
    print(body.decode('utf-8'))
