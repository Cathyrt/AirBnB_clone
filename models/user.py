#!/usr/bin/python3
"""
User creation class
"""
from models.base_model import BaseModel


class User(BaseModel):
    """Defines attributes for user creation"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        if args and type(args[0]) is dict:
            BaseModel.__init__(self, args[0])
        else:
            BaseModel.__init__(self)
