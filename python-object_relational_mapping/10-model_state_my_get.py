#!/usr/bin/python3
"""
Prints the id of the State object whose name is passed as argument,
from the DB hbtn_0e_6_usa (safe from SQL-injection).

Usage:
    ./10-model_state_my_get.py <mysql_user> <mysql_pwd> <database> <state_name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Query for the state by name and print its id (or Not found)."""
    if len(sys.argv) != 5:
        sys.exit(1)

    user, pwd, db, target = sys.argv[1:5]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == target).first()
    print(state.id if state else "Not found")

    session.close()


if __name__ == "__main__":
    main()
