#!/usr/bin/python3
"""Defines a user module"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represent a user
    Attributes:
            email(str) - email of user
            password(str) - password of a user
            first_name(str) - first name of user
            last_name(str) - last_name of User
            """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
