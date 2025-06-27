#!/usr/bin/python3
"""
Prints the id of the State matching argv[4] (safe query).
Usage: ./10-model_state_my_get.py <user> <pwd> <db> <state_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state = session.query(State).filter(State.name == sys.argv[4]).first()
        print(state.id if state else "Not found")
