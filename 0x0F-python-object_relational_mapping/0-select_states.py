#!/usr/bin/python3
'''0-select_states.py'''

if __name__ == '__main__':
    import MySQLdb
    from sys import argv

    if len(argv) >= 4:
        username = argv[1]
        password = argv[2]
        dbname = argv[3]

        conn = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=dbname,
            port=3306,
            charset='utf8')

        cur = conn.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id ASC")
        rows = cur.fetchall()

        for row in rows:
            print("{}".format(row))

        cur.close()
        conn.close()
