#!/usr/bin/python3
"""relationship_city.py"""

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):

    """
    State class
        Attributes:
            __tablename__ (str): The table name of the class
            id (int): The State id of the class
            name (str): The State name of the class
            cities (:obj:`City`): The Cities belongs to State
    """
    __tablename__ = 'cities'
    __table_args = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
