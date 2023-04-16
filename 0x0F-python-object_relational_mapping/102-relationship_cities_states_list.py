#!/usr/bin/python3
'''102-relationship_cities_states_list module
List all cities with their state
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

    all_cities = session.query(City).order_by(City.id)

    for city in all_cities:
        print('{}: {} -> {}'.format(city.id, city.name, city.state.name))
