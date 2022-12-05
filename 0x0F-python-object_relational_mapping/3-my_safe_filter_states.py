#!/usr/bin/python3
"""3-my_safe_filter_states.py"""


if __name__ == '__main__':
    """import modules"""
    import MySQLdb
    from sys import argv

    if len(argv) >= 5:
        """Retrive passed arguments"""
        search = argv[4]

        with MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306, charset='utf8') as conn:
            with conn.cursor() as cur:
                num_rows = cur.execute("SELECT * FROM states\
                    WHERE BINARY name = %(search)s", {'search': search})
                rows = cur.fetchall()
                for row in rows:
                    print(row)
