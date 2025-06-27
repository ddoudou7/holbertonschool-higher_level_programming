#!/usr/bin/python3
"""
Lists all cities of a given state from the database hbtn_0e_4_usa.

Usage:
    ./5-filter_cities.py <mysql_user> <mysql_pwd> <db_name> <state_name>

Example:
    $ ./5-filter_cities.py root root hbtn_0e_4_usa Texas
    Dallas, Houston, Austin
"""
import sys
import MySQLdb

def main():
    """Connects to MySQL and prints cities of the given state."""
    if len(sys.argv) != 5:
        sys.exit(1)
    user, pwd, db_name, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=db_name
    )
    cur = db.cursor()
    sql = ("SELECT cities.name "
           "FROM cities "
           "JOIN states ON cities.state_id = states.id "
           "WHERE states.name = %s "
           "ORDER BY cities.id ASC")
    cur.execute(sql, (state,))
    rows = cur.fetchall()
    if rows:
        print(", ".join(r[0] for r in rows))
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
