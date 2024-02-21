#!/usr/bin/python3
""" City Module for HBNB project """
from models.state import State
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = 'cities'

    name = Column("name", String(60), nullable=False, )
    state_id = Column("name", String(128), ForeignKey('states.id'), nullable=False)
