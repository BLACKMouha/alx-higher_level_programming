#!/usr/bin/python3
'''12-model_state_update_id_2 module
Updates a state
'''

if (__name__ == '__main__'):
    from sys import argv
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import State

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                      argv[2],
                                                      argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    the_state = session.query(State).filter(State.id == 2).first()
    the_state.name = 'New Mexico'
    session.commit()
