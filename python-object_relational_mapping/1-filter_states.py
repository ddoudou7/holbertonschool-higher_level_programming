#!/usr/bin/python3
"""
Lists all State rows where name starts with 'N' from DB hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <mysql_user> <mysql_pwd> <db_name>

Example:
    ./1-filter_states.py root root hbtn_0e_0_usa
    (4, 'New York')
    (5, 'Nevada')
"""
import sys
import MySQLdb


def main():
    """Connects to MySQL, queries states where name LIKE 'N%', prints each row."""
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
