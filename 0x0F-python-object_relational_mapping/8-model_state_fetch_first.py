#!/usr/bin/python3

"""8-model_state_fetch_first.py"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2],
                                                                       argv[3])
                           )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    list_states = session.query(State).order_by(State.id).all()
    first_state = list_states[0]
    print("{}: {}".format(first_state.id, first_state.name))
