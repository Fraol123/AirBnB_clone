#!/usr/bin/python3
"""Module that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """class the represent state
    Attributes:
    city_id: empty string: it will be the City.id
    user_id: empty string: it will be the User.id
    name:  empty string
    description: empty string
    number_rooms: integer - 0
    number_bathrooms: integer - 0
    max_guest: integer - 0
    price_by_night: integer - 0
    latitude: float - 0.0
    longitude: float - 0.0
    amenity_ids: list of str - empty list:
    it will be the list of Amenity.id later
    """
    name = ""
    city_id = ""
    user_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
