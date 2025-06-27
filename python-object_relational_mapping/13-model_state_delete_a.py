#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
Usage:
    ./13-model_state_delete_a.py <mysql_user> <mysql_pwd> <db_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f'mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}',
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Supprime tous les états dont name contient 'a'
    session.query(State)\
           .filter(State.name.contains('a'))\
           .delete(synchronize_session='fetch')
    session.commit()

    session.close()

if __name__ == "__main__":
    main()
