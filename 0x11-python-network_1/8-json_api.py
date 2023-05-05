#!/usr/bin/python3
'''
Sends a POST requests with a letter as data to a URL both passed as arguments
then displays id and name from the JSON if any
'''

from sys import argv
import requests

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    q = argv[1] if len(argv) == 2 else ""
    r = requests.post(url, data={"q": q})
    try:
        rj = eval(r.text)
    if (type(rj) is not dict):
        print('Not a valid JSON')
    elif (not rj):
        print('No result')
    else:
        print('[{}] {}'.format(rj.get('id', None), rj.get('name', None)))
    except Exception as e:
        pass
