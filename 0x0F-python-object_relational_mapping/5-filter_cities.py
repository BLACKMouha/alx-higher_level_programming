#!/usr/bin/python3
'''5-filter_cities module
Lists all the cites of the state passed as argument
'''
if (__name__ == '__main__'):
    import MySQLdb
    from sys import argv

    if (len(argv) == 5):
        h, u, p, d = 'localhost', argv[1], argv[2], argv[3]
        db = MySQLdb.connect(host=h, user=u, passwd=p, db=d, port=3306)
        cur = db.cursor()

        cur.execute('''SELECT cities.name FROM cities
        WHERE cities.state_id = (SELECT id FROM states WHERE name
        = "{}") ORDER BY cities.id;'''.format(argv[4]))

        cities = cur.fetchall()

        i = 0
        for city in cities:
            print(city[0], end='')
            i += 1
            if (i < len(cities)):
                print(', ', end='')
        print()

        cur.close()
        db.close()
