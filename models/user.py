#!/usr/bin/python3
''' A class user that inherites from BaseModel'''
from models.base_model import BaseModel


class User(BaseModel):
    '''Public class attributes'''
    email = ""
    passworrd = ""
    first_name = ""
    last_name = ""
