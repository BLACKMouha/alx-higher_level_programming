#!/usr/bin/python3
"""101-relationship_states_cities_list.py"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sys import argv


if __name__ == '__main__':
    a, b, c = argv[1], argv[2], argv[3]
    conn_url = "mysql+mysqldb://{}:{}@localhost/{}".format(a, b, c)
    engine = create_engine(conn_url)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    session = Session()

    st_list = session.query(State).all()
    for st in st_list:
        print("{}: {}".format(st.id, st.name))
        ct_by_id = session.query(City).filter_by(state_id=st.id).all()
        for ct in ct_by_id:
            print("    {}: {}".format(ct.id, ct.name))
    session.close()
