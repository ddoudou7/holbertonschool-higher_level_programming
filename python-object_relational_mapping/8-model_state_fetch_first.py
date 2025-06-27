#!/usr/bin/python3
"""
Prints the first State object (id asc) from the DB hbtn_0e_6_usa.
Usage: ./8-model_state_fetch_first.py <mysql_user> <mysql_pwd> <db_name>
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
        state = session.query(State).order_by(State.id).first()
        if state is None:
            print("Nothing")
        else:
            print(f"{state.id}: {state.name}")
