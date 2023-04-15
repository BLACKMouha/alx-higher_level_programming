#!/usr/bin/python3
'''9-model_state_filter_a
Displays the states contains an 'a'
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

    r = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for el in r:
        print('{}: {}'.format(el.id, el.name))
