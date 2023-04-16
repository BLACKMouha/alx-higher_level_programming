#!/usr/bin/python3
'''10-model_state_my_get
Displays the state passed as argument
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

    the_state = argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()

    r = session.query(State).filter(State.name == the_state).first()
    if (r is not None):
        print(r.id)
    else:
        print('Not found')
