#!/usr/bin/python3
"""
Lists all State rows where name matches the argument from DB hbtn_0e_0_usa,
using a parameterized query to prevent SQL injection.

Usage:
    ./3-my_safe_filter_states.py <mysql_user> <mysql_pwd> <db_name> "<state_name>"

Example:
    ./3-my_safe_filter_states.py root root hbtn_0e_0_usa "Arizona"
    (2, 'Arizona')
"""
import sys
import MySQLdb

def main():
    """Connect to MySQL, safely query by name, print each row."""
    if len(sys.argv) != 5:
        sys.exit(1)

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8",
        use_unicode=True
    )
    cur = db.cursor()
    # Parameterized query, pas de format() direct
    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(sql, (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
