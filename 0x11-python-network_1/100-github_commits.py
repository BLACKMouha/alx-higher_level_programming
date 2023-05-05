#!/usr/bin/python3
'''
Takes GitHub credentials and displays the id
'''

if __name__ == '__main__':
    from sys import argv
    from requests import get
    from requests.auth import HTTPBasicAuth

    repo_name, owner = argv[1], argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo_name)
    headers = {}
    headers['X-GitHub-Api-Version'] = '2022-11-28'
    r = get(url, headers=headers)
    j = eval(r.text.replace('false', 'False').replace('true', 'True')
                   .replace('null', 'None'))
    i = 0
    for c in j:
        print(c.get('sha', None), end=': ')
        print(c.get('commit', None).get('author', None).get('name', None))
        i += 1
        if (i == 10):
            break
