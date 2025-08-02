#!/usr/bin/python3
"""
Add the State object “Louisiana” to hbtn_0e_6_usa
and print its newly assigned id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Create a session, add Louisiana and print its id."""
    if len(sys.argv) != 4:
        sys.exit(1)

    user, pwd, db = sys.argv[1:4]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)

    session.close()


if __name__ == "__main__":
    main()
