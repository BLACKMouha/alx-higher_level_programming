#!/usr/bin/python3
"""2-my_filter_states.py"""


if __name__ == '__main__':
    """import modules"""
    import MySQLdb
    from sys import argv

    if len(argv) >= 5:
        """Retrieve passed arguments"""
        username = argv[1]
        password = argv[2]
        dbname = argv[3]
        search = argv[4]

        """Establish connection to the database"""
        conn = MySQLdb.connect(
                host='localhost',
                user=username,
                passwd=password,
                db=dbname,
                port=3306,
                charset='utf8')

        """Create the cursor instance"""
        cur = conn.cursor()
        """SQL query that list all states beginning with 'N'"""
        query = "SELECT * FROM states WHERE BINARY name='{}'".format(search)

        cur.execute(query)

        rows = cur.fetchall()
        """Printing rows"""
        for row in rows:
            print(row)

        """Over the game!"""
        cur.close()
        conn.close()
