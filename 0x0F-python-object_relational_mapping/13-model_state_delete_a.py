#!/usr/bin/python3
'''13-model_state_delete_a module
Deletes all states containing an 'a'
'''


if (__name__ == '__main__'):
    from sys import argv
    from model_state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                      argv[2],
                                                      argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state_to_delete = session.query(State).filter(State.name.like('%a%'))
    for state in state_to_delete:
        session.delete(state)
    session.commit()
