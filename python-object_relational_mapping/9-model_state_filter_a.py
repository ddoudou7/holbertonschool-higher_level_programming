#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from hbtn_0e_6_usa.

Usage:
    ./9-model_state_filter_a.py <mysql_user> <mysql_pwd> <db_name>

Example:
    $ ./9-model_state_filter_a.py root root hbtn_0e_6_usa
    1: California
    2: Arizona
    3: Texas
    5: Nevada
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State)\
                        .filter(State.name.contains('a'))\
                        .order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()

if __name__ == "__main__":
    main()
