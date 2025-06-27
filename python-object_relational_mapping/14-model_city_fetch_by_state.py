#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
in the format: <state name>: (<city id>) <city name>.
Usage:
    ./14-model_city_fetch_by_state.py <mysql_user> <mysql_pwd> <db_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
from model_city import City

def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    user, pwd, db = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine(
        f"mysql+mysqldb://{user}:{pwd}@localhost:3306/{db}",
        pool_pre_ping=True
    )
    # Charge les métadonnées (import Base avant)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    # Jointure City → State, tri par City.id
    results = session.query(City, State) \
                     .join(State, City.state_id == State.id) \
                     .order_by(City.id) \
                     .all()

    for city, state in results:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()

if __name__ == "__main__":
    main()
