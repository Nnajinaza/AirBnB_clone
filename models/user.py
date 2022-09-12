#!/usr/bin/python3
''' A class user that inherites from BaseModel'''
from models.base_model import BaseModel
import models


class User(BaseModel):
    '''Public class attributes'''
    email = ""
    passworrd = ""
    first_name = ""
    last_name = ""
