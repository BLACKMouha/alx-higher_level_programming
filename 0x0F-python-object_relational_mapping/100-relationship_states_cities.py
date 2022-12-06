#!/usr/bin/python3

"""100-relationship_states_cities.py"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import Base, City, State


if __name__ == '__main__':
    a, b, c = argv[1], argv[2], argv[3]
    conn_url = "mysql+mysqldb://{}:{}@localhost/{}".format(a, b, c)
    engine = create_engine(conn_url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name='California')
    session.add(new_state)
    session.commit()
    cal_st_id = session.query(State).filter_by(name='California').first().id
    sfr_ct = City(state_id=cal_st_id, name='San Francisco')
    session.add(sfr_ct)
    session.commit()
