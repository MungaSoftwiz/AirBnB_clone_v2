#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')
    else:
        name = ""

    @property
    def cities(self):
        """ Method returns the list of City instances with
        state_id equals to current State.id
        """
        from models import storage
        cities_lst = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                cities_lst.append(city)
        return cities_lst
