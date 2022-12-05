#!/usr/bin/python3
"""5-filter_cities.py"""


if __name__ == '__main__':
    """import modules"""
    import MySQLdb
    from sys import argv

    if len(argv) == 5:
        """Retrieve passed arguments"""
        search = argv[4]

        with MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306, charset='utf8') as conn:
            with conn.cursor() as cur:
                """Retrieve all cities of a state"""
                num_rows = cur.execute("SELECT cities.name FROM cities\
                                       INNER JOIN states\
                                       ON states.id = cities.state_id\
                                       WHERE states.name = %(search)s\
                                       ORDER BY cities.id;",
                                       {'search': search})
                rows = cur.fetchall()
                for i in range(len(rows)):
                    print(rows[i][0], end='')
                    if (i != len(rows) - 1):
                        print(', ', end='')
                print()
