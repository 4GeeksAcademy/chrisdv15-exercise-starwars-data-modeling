import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, DECIMAL, String, DateTime, ARRAY 
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Favorite(Base):
    __tablename__ = 'favorite'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))


class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(Integer)
    mass = Column(Integer)
    hair_color = Column(String(20))
    skin_color = Column(String(20))
    eyes_color = Column(String(20))
    birth_year = Column(String(20))
    gender= Column(String(20))
    created = Column(DateTime)
    edited = Column(DateTime)
    howeworld = Column(String(250))
    url = Column(String(250))
    
class Planet(Base):
    __tablename__ = 'planet'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Integer)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(20))
    population = Column(Integer)
    climate = Column(String(20))
    terrain = Column(String(20))
    surface_water = Column(String)
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String)

class Vehicle(Base):
    __tablename__ = 'vehicle'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    model = Column(String)
    manufacturer = Column(String)
    cost_in_credits = Column(Integer)
    length = Column(DECIMAL(20,1))
    crew = Column(Integer)
    passengers = Column(Integer)
    max_atmosphering_speed = Column(Integer)
    cargo_capacity = Column(Integer)
    consumable = Column(String(20))
    films = Column(ARRAY(String))
    pilots = Column(ARRAY(String))
    created = Column(DateTime)
    edited = Column(DateTime)
    url = Column(String)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
