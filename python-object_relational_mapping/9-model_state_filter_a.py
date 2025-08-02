#!/usr/bin/python3
"""
Lists all State objects whose name contains the letter 'a'
from the DB hbtn_0e_6_usa (SQLAlchemy).

Usage:
    ./9-model_state_filter_a.py <mysql_user> <mysql_pwd> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Create a session, query states containing 'a' and print them."""
    if len(sys.argv) != 4:
        sys.exit(1)

    user, pwd, db = sys.argv[1:4]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = (session.query(State)
              .filter(State.name.contains('a'))
              .order_by(State.id))

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    main()
