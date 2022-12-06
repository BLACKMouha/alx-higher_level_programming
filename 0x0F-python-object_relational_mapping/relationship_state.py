#!/usr/bin/python3
"""relationship_state.py"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):

    """State class definition
        Attributes:
            __tablename__ [str]: The table name of this class
            id [int]: The State id of the class
            name [str]: The State name of the class
            cities [:obj:City]: The cities belong to a State instance
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref='states', cascade='all, delete')
