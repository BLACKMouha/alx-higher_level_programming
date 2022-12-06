#!/usr/bin/python3
"""model_city.py"""


from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """Definition of the City class"""
    __tablename__ = 'cities'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
