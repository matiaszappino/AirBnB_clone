#!/usr/bin/python3
"""User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """User Class Documentation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
