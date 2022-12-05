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
    first_state = session.query(State).filter_by(id=1).first()
    print("{}: {}".format(first_state.id, first_state.name))
