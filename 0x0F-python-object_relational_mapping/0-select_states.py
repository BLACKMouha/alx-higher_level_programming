#!/usr/bin/python3
'''0-select_states module
lists all states from the database hbtn_0e_usa
'''
if (__name__ == '__main__'):
    import MySQLdb
    from sys import argv

    if (len(argv) == 4):
        h, u, p, d = "localhost", argv[1], argv[2], argv[3]
        db = MySQLdb.connect(host=h, user=u, passwd=p, db=d, port=3306)
        cur = db.cursor()

        q = "SELECT * FROM states"
        cur.execute(q)
        states = cur.fetchall()
        for state in states:
            print(state)

        cur.close()
        db.close()
