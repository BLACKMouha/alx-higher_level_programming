#!/usr/bin/python3

"""9-model_state_filter_a.py"""

from sys import argv
from sqlalchemy import create_engine, select
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                                       argv[2],
                                                                       argv[3])
                           )

    Base.metadata.create_all(engine)
    q = select(State.__table__).where(State.__table__.c.name.like('%a%'))
    states_containing_a = engine.execute(q)

    for state in states_containing_a:
        print("{}: {}".format(state.id, state.name))
