#!/usr/bin/python3
"""Module theat define reviwm class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class representation of Review
        Attributes:
                place_id: empty string: it will be the Place.id
                user_id: empty string: it will be the User.id
                text: empty string
    """
    place_id = ""
    user_id = ""
    text = ""
