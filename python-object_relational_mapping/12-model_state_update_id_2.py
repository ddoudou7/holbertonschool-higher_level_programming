#!/usr/bin/python3
"""
Updates the name of the State object with id = 2 to “New Mexico”.
Usage:
    ./12-model_state_update_id_2.py <mysql_user> <mysql_pwd> <db_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        state = session.query(State).get(2)          # id = 2
        if state:
            state.name = "New Mexico"
            session.commit()
