#!/usr/bin/python3
'''
model_state module
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):
    '''
    Representation of a state
    '''
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
