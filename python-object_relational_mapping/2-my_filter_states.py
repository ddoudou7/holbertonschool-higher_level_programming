#!/usr/bin/python3
"""
Lists all State rows where name matches the argument from DB hbtn_0e_0_usa.

Usage:
    ./2-my_filter_states.py <mysql_user> <mysql_pwd> <db_name> "<state_name>"
Example:
    ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona"
    (2, 'Arizona')
"""
import sys
import MySQLdb


def main():
    """
    Connects to MySQL on localhost:3306 using provided credentials,
    queries the states whose name matches the user input, and prints each row.
    """
    if len(sys.argv) != 5:
        return
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
