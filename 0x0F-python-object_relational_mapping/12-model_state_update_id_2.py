#!/usr/bin/python3

"""12-model_state_update_id_2.py"""


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

    state_to_change = session.query(State).filter(State.id=='2').first()
    state_to_change.name = 'New Mexico'
    session.commit()
    session.close()
