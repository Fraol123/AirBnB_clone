#!/usr/bin/python3
"""Module that Define city class"""
from models.base_model import BaseModel


class City(BaseModel):
    """class the represent city
    Attribute:
        state_id (str): The state id.
        name (str): The name of the city.
    """
    name = ""
    state_id = ""
