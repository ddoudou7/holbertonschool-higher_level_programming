#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa (SQLAlchemy).
Usage: ./7-model_state_fetch_all.py <user> <password> <db>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Create session, query all State objects, print them."""
    if len(sys.argv) != 4:
        sys.exit(1)

    user, pwd, db = sys.argv[1:4]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
