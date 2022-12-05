#!/usr/bin/python3
"""3-my_safe_filter_states.py"""


if __name__ == '__main__':
    """import modules"""
    import MySQLdb
    from sys import argv

    if len(argv) >= 4:
        """Retrive passed arguments"""

        with MySQLdb.connect(host='localhost', user=argv[1], passwd=argv[2],
                             db=argv[3], port=3306, charset='utf8') as conn:
            with conn.cursor() as cur:
                num_rows = cur.execute("SELECT cities.id, cities.name,\
                                        states.name FROM cities\
                                        INNER JOIN states\
                                        ON states.id = cities.state_id\
                                        ORDER BY cities.id;")
                rows = cur.fetchall()
                for row in rows:
                    print(row)
