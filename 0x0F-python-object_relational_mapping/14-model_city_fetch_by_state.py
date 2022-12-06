#!/usr/bin/python3

"""14-model_city_fetch_by_state.py"""

from sys import argv
from model_city import Base, City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == '__main__':
    a, b, c = argv[1], argv[2], argv[3]
    conn_url = "mysql+mysqldb://{}:{}@localhost/{}".format(a, b, c)
    engine = create_engine(conn_url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    for s, c in session.query(State, City).join(City).order_by(City.id).all():
        print("{}: ({}) {}".format(s.name, c.id, c.name))
