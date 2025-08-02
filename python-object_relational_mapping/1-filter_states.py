#!/usr/bin/python3
"""
List all states whose name starts with uppercase N.
Usage: ./1-filter_states.py <user> <password> <db>
"""
import sys
import MySQLdb


def main():
    """Connect to DB, query, print."""
    if len(sys.argv) != 4:
        sys.exit(1)

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
