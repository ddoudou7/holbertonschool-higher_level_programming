#!/usr/bin/python3
"""
Prints the first State object from the DB hbtn_0e_6_usa
(using SQLAlchemy).

Usage:
    ./8-model_state_fetch_first.py <mysql_user> <mysql_pwd> <database>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Create a session, fetch the first State and display it."""
    if len(sys.argv) != 4:
        sys.exit(1)

    user, pwd, db = sys.argv[1:4]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).order_by(State.id).first()
    print(f"{state.id}: {state.name}" if state else "Nothing")

    session.close()


if __name__ == "__main__":
    main()
