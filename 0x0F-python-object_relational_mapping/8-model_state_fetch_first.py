#!/usr/bin/python3
'''8-model_state_fetch_first
Displays the first state
'''
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if (__name__ == '__main__'):
    from sys import argv
    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                      argv[2],
                                                      argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    first = session.query(State).first()
    print('{}: {}'.format(first.id, first.name))
