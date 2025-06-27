#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage:
    ./8-model_state_fetch_first.py <mysql_user> <mysql_pwd> <db_name>

Example:
    $ ./8-model_state_fetch_first.py root root hbtn_0e_6_usa
    1: California
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
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(user, pwd, db),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    session.close()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

if __name__ == "__main__":
    main()
