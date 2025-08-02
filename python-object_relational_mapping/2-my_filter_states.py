#!/usr/bin/python3
"""Filter states by user input (exact name match, case-sensitive)."""

import sys
import MySQLdb


def main():
    """Connect, query by exact name, print rows."""
    if len(sys.argv) != 5:
        sys.exit(1)

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db.cursor()
    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])
    )
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
