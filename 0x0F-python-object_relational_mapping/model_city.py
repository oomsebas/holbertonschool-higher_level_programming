#!/usr/bin/python3
""" Write a python file that contains the class definition of a State """
from sqlalchemy import Table, Column, Integer, ForeignKey, String
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
        """ Class for the State table """
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True, nullable=False,
                    autoincrement=True, unique=True)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
