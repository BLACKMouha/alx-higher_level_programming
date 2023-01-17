#!/usr/bin/python3
"""hbtn_header module
    This script displays the value of `X-Request-Id` of a given address
"""
if __name__ == '__main__':
    from sys import argv
    import urllib.request

    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        x_req_id = res.getheader('X-Request-Id')
    print(x_req_id)
