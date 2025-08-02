#!/usr/bin/python3
"""Lists all states that start with uppercase N from the database."""

import sys
import MySQLdb


def main():
    """Connect, query, print results."""
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
        "SELECT * FROM states "
        "WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
