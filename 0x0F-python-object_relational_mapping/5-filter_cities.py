#!/usr/bin/python3
"""Module."""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT c.name FROM cities AS c
                   INNER JOIN states AS s
                   ON c.state_id = s.id
                   WHERE s.name = %s
                   ORDER BY c.id ASC
                """, (argv[4],))
    query_rows = cur.fetchall()
    l = []
    for i in query_rows:
        l.append(i[0])
    print(*l, sep=", ")
    cur.close()
    conn.close()
