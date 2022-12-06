#!/usr/bin/python3

"""13-model_state_delete_a.py"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    a, b, c = argv[1], argv[2], argv[3]
    conn_url = "mysql+mysqldb://{}:{}@localhost/{}".format(a, b, c)
    engine = create_engine(conn_url)
    Session = sessionmaker(bind=engine)

    session = Session()
    stds = session.query(State).filter(State.name.contains('a'))
    for std in stds:
        session.delete(std)
    session.commit()
