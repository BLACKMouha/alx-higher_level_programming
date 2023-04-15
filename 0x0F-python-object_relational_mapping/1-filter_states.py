#!/usr/bin/python3
'''1-filter_states module
lists all states with a name starting with N fromdatabase hbtn_0e_usa
'''
if (__name__ == '__main__'):
    import MySQLdb
    from sys import argv

    if (len(argv) == 4):
        h, u, p, d = "localhost", argv[1], argv[2], argv[3]
        db = MySQLdb.connect(host=h, user=u, passwd=p, db=d, port=3306)
        cur = db.cursor()

        q = "SELECT * FROM states WHERE name LIKE 'N%'"
        cur.execute(q)

        results = cur.fetchall()
        for result in results:
            print(result)

        cur.close()
        db.close()
