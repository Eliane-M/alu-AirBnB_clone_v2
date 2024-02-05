#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Table, ForeignKey
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """defines the table for amenities"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = Table(
        "place_amenity", Base.metadata,
        Column('place_id',
               String(60),
               ForeignKey('places.id'),
               primary_key=True,
               nullable=False),
        Column('amenity_id',
               String(60),
               ForeignKey('amenities.id'),
               primary_key=True,
               nullable=False)
    )