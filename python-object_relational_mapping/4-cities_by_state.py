#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.

Usage:
    ./4-cities_by_state.py <mysql_user> <mysql_pwd> <db_name>
Example:
    ./4-cities_by_state.py root root hbtn_0e_4_usa
    (1, 'San Francisco', 'California')
    ...
"""
import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        sys.exit(1)
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
