#!/usr/bin/python3
"""
Deletes all State objects whose name contains the letter 'a'
from the DB hbtn_0e_6_usa.
Usage: ./13-model_state_delete_a.py <mysql_user> <mysql_pwd> <db_name>
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
        for state in session.query(State).filter(State.name.like("%a%")):
            session.delete(state)
        session.commit()
