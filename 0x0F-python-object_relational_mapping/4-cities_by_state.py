#!/usr/bin/python3

if (__name__ == '__main__'):
    import MySQLdb
    from sys import argv

    if (len(argv) == 4):
        h, u, p, d = 'localhost', argv[1], argv[2], argv[3]
        db = MySQLdb.connect(host=h, user=u, passwd=p, db=d, port=3306)
        cur = db.cursor()

        cur.execute('''SELECT cities.id, cities.name, states.name FROM cities
                INNER JOIN states ON states.id = cities.state_id
                ORDER BY id ASC''')
        cities = cur.fetchall()
        for city in cities:
            print(city)

        cur.close()
        db.close()
