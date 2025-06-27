#!/usr/bin/python3
"""
Lists all city names of the state passed as argv[4] (safe from SQL injection).

Usage:
    ./5-filter_cities.py <mysql_user> <mysql_pwd> <db_name> <state_name>

Output example (for Texas):
    Dallas, Houston, Austin
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()

    # ► Une seule execute() avec paramètre → protège contre l’injection
    cur.execute("""SELECT cities.name FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC""", (sys.argv[4],))

    cities = [row[0] for row in cur.fetchall()]
    print(", ".join(cities))

    cur.close()
    db.close()
