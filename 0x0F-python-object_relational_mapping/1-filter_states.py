#!/usr/bin/python3
"""Module."""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""
                SELECT *
                FROM states
                WHERE name LIKE 'N%' COLLATE latin1_general_cs
                ORDER BY states.id;
                """)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
