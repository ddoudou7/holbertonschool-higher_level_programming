#!/usr/bin/python3
"""
Takes a state name as argument and lists all cities of that state
from the database hbtn_0e_4_usa.

Usage:
    ./5-filter_cities.py <mysql_user> <mysql_pwd> <db_name> <state_name>
"""
import sys
import MySQLdb

def main():
    if len(sys.argv) != 5:
        sys.exit(1)

    user, pwd, db, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=db,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT c.name "
        "FROM cities c "
        "JOIN states s ON c.state_id = s.id "
        "WHERE s.name = %s "
        "ORDER BY c.id ASC",
        (state,)
    )
    rows = cur.fetchall()
    if rows:
        print(", ".join(r[0] for r in rows))
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
