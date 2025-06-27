#!/usr/bin/python3
"""
Takes a state name as argument and lists all its cities in hbtn_0e_4_usa.

Usage:
    ./5-filter_cities.py <mysql_user> <mysql_pwd> <db_name> <state_name>
"""
import sys
import MySQLdb

def main():
    if len(sys.argv) != 5:
        sys.exit(1)

    user, pwd, db_name, state = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pwd,
        db=db_name,
        charset="utf8",
        use_unicode=True
    )
    cur = conn.cursor()
    cur.execute(
        "SELECT cities.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (state,)
    )
    rows = cur.fetchall()
    conn.close()

    if rows:
        print(", ".join(r[0] for r in rows))

if __name__ == "__main__":
    main()
