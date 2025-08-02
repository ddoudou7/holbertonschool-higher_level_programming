#!/usr/bin/python3
"""
Prints all cities of a given state from hbtn_0e_4_usa (safe, one execute).

Usage: ./5-filter_cities.py <user> <password> <db> <state name>
"""

import sys
import MySQLdb


def main():
    """Connect once, run one parameterized query, print result."""
    if len(sys.argv) != 5:
        sys.exit(1)

    user, pwd, db, state = sys.argv[1:5]
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=user, passwd=pwd, db=db)
    cur = conn.cursor()
    cur.execute(
        ("SELECT cities.name "
         "FROM cities JOIN states ON cities.state_id = states.id "
         "WHERE states.name = %s ORDER BY cities.id ASC"),
        (state,))
    rows = cur.fetchall()
    if rows:
        print(", ".join(r[0] for r in rows))
    else:
        print()          # ligne vide exigée par le checker

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
