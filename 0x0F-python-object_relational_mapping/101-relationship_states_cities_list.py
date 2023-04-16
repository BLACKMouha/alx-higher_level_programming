#!/usr/bin/python3
'''101-relationship_states_cities_list module
List all states and their corresponding cities
'''

if (__name__ == '__main__'):
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                      argv[2],
                                                      argv[3])
    engine = create_engine(url, pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    all_states = session.query(State).order_by(State.id)

    for state in all_states:
        print('{}: {}'.format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))
