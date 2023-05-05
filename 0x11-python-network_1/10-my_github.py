#!/usr/bin/python3
'''
Takes GitHub credentials and displays the id
'''

if __name__ == '__main__':
    from requests import get, post
    from requests.auth import HTTPBasicAuth
    from sys import argv

    user, token = argv[1], argv[2]
    basic = HTTPBasicAuth(user, token)
    url = 'https://api.github.com/user'
    headers = {}
    headers['X-GitHub-Api-Version'] = '2022-11-28'
    r = post(url, headers=headers, auth=basic)
    j = eval(r.text.replace('false', 'False').replace('true', 'True')
                   .replace('null', 'None'))
    print(j.get('id', None))
