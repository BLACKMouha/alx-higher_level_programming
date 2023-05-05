#!/usr/bin/python3
'''
Sends a POST requests with a letter as data to a URL both passed as arguments
then displays id and name from the JSON if any
'''

from requests import post
from requests.exceptions import JSONDecodeError
from sys import argv

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) == 2 else ""
    try:
        r = post(url, data={"q": q})
        r.raise_for_status()
        rj = r.json()
        if (not rj):
            print('No result')
        else:
            print('[{}] {}'.format(rj.get('id', None), rj.get('name', None)))
    except JSONDecodeError:
        print('Not a valid JSON')
