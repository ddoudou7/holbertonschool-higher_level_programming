#!/usr/bin/python3
"""
Lists all cities of hbtn_0e_4_usa in ascending order by cities.id.
Output format : (id, city_name, state_name)
Usage: ./4-cities_by_state.py <mysql_user> <mysql_pwd> <db_name>
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

    # ► une seule execute()      ↓↓↓ jointure + tri
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   ORDER BY cities.id ASC""")

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
