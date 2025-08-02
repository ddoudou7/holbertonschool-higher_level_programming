#!/usr/bin/python3
"""
List every city with its state from the DB hbtn_0e_4_usa.

Usage: ./4-cities_by_state.py <user> <password> <db>
"""

import sys
import MySQLdb


def main():
    """Connect, query once, print rows."""
    if len(sys.argv) != 4:
        sys.exit(1)

    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute(
        ("SELECT cities.id, cities.name, states.name "
         "FROM cities JOIN states ON cities.state_id = states.id "
         "ORDER BY cities.id ASC")
    )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
