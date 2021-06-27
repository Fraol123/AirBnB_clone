#!/usr/bin/python3
"""Module that define the state class"""
from models.base_model import BaseModel


class State(BaseModel):
    """class the represent state
    Attribute:
            name(str): name of the state
    """
    name = ""
