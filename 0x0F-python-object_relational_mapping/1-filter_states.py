#!/usr/bin/python3

import MySQLdb
from sys import argv

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
cur.execute("SELECT * FROM states WHERE name LIKE 'N%'")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
