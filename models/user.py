#!/usr/bin/python3
"""class User"""


from models.base_model import BaseModel


class User(BaseModel):
    """ USer class inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
