#!/usr/bin/python3
"""
Prints the State.id of the State object with the name passed as argument
from the database hbtn_0e_6_usa. Safe from SQL injection.

Usage:
    ./10-model_state_my_get.py <mysql_user> <mysql_pwd> <db_name> <state_name>

If the state is not found, prints "Not found".
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 5:
        sys.exit(1)

    user, pwd, db, target = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).filter(State.name == target).first()
    session.close()

    if result:
        print(result.id)
    else:
        print("Not found")

if __name__ == "__main__":
    main()
