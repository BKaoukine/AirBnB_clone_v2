#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    
    cities = relationship("City", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        """Getter attribute to return list of City instances"""
        from models import storage
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
