#!/usr/bin/python3
'''2-my_filter_states module
displays all values in the states table matching the states passed as argument
'''
if (__name__ == '__main__'):
    import MySQLdb
    from sys import argv

    if (len(argv) == 5):
        h, u, p, d = "localhost", argv[1], argv[2], argv[3]
        db = MySQLdb.connect(host=h, user=u, passwd=p, db=d, port=3306)
        cur = db.cursor()

        searched_state = argv[4]
        q = 'SELECT * FROM states WHERE name = "{}"'.format(searched_state)
        cur.execute(q)
        r = cur.fetchall()
        for i in r:
            print(i)

        cur.close()
        db.close()
