#!/usr/bin/python3
"""
Changes the name of the State object with id = 2 to "New Mexico"
in the database hbtn_0e_6_usa.
Usage:
    ./12-model_state_update_id_2.py <mysql_user> <mysql_pwd> <db_name>
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

    # Récupère l'État avec id=2 et modifie son nom
    state = session.query(State).get(2)
    if state:
        state.name = "New Mexico"
        session.commit()

    session.close()

if __name__ == "__main__":
    main()
