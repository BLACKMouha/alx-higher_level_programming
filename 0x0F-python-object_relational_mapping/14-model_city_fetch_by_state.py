#!/usr/bin/python3
'''14-model_city_fetch_by_state module
Prints all city instance of the database
'''

if (__name__ == '__main__'):
    from sys import argv
    from model_city import City
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                      argv[2],
                                                      argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(City.id, City.name, State.name).\
        select_from(City).\
        join(State).\
        order_by(City.id)
    for st_ct in states_cities:
        print('{}: ({}) {}'.format(st_ct[2], st_ct[0], st_ct[1]))
