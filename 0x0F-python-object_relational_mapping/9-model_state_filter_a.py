#!/usr/bin/python3

"""9-model_state_filter_a.py"""

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
    for state in session.query(State).filter(State.name.contains('a')):
        print("{}: {}".format(state.id, state.name))
