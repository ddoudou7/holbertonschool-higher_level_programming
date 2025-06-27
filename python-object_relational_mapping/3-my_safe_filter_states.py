#!/usr/bin/python3
"""
Safely lists all rows in `states` whose name matches the argument.
Usage: ./3-my_safe_filter_states.py <mysql_user> <mysql_pwd> <db_name> <state>
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3]
    )
    cur = db.cursor()

    # requête paramétrée : protège contre l'injection SQL
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)          # tuple pour MySQLdb
    )
    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
