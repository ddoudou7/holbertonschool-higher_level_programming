#!/usr/bin/python3
"""
Safely filter states by exact name (case-sensitive).

Usage: ./3-my_safe_filter_states.py <user> <password> <db> <state>
"""

import sys
import MySQLdb


def main():
    """Connect, query with parameter binding, print matching rows."""
    if len(sys.argv) != 5:
        sys.exit(1)

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
