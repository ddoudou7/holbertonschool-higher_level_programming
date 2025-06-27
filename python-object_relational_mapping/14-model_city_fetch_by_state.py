#!/usr/bin/python3
"""
Prints all City objects, ordered by cities.id, in the format:
<state name>: (<city id>) <city name>
Usage:
    ./14-model_city_fetch_by_state.py <mysql_user> <mysql_pwd> <db_name>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    with Session(engine) as session:
        rows = (session.query(State.name, City.id, City.name)
                      .join(City)
                      .order_by(City.id)
                      .all())

        for state_name, city_id, city_name in rows:
            print(f"{state_name}: ({city_id}) {city_name}")
