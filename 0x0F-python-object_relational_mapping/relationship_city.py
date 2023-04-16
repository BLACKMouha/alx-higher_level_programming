#!/usr/bin/python3
'''model_city module
Contains the City class definition
'''

from relationship_state import Base, State
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker


class City(Base):
    '''Representation of a city'''

    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
