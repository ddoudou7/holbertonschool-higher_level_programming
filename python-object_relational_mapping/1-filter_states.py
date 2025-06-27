#!/usr/bin/python3
"""
Lists all State rows whose name starts with 'N' from the database hbtn_0e_0_usa.
Usage: ./1-filter_states.py <mysql_user> <mysql_pwd> <db_name>
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name LIKE BINARY 'N%' "
                "ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
