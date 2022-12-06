#!/usr/bin/python3

"""102-relationship_cities_states_list.py"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City, State


if __name__ == '__main__':
    a, b, c = argv[1], argv[2], argv[3]
    conn_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(a, b, c)
    engine = create_engine(conn_url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    ct_objs = session.query(City, State).join(State).order_by(City.id).all()
    for ct in ct_objs:
        print("{}: {} -> {}".format(ct.City.id, ct.City.name, ct.State.name))

    session.close()
