#!/usr/bin/python3
"""
Lists all rows of table `states` from DB hbtn_0e_0_usa (ordered by id ASC).

Usage:
    ./0-select_states.py <mysql_user> <mysql_pwd> <db_name>
Example output:
    (1, 'California')
    (2, 'Arizona')
"""
import sys
import MySQLdb


def main():
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
