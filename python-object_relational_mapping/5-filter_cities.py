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
    query = (
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cur.execute(query, (state,))
    rows = cur.fetchall()
    if rows:
        print(", ".join([r[0] for r in rows]))
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
