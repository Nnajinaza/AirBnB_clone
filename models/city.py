#!/usr/bin/python3
'''Defines class City that inherites from BaseModel'''
from models.base_model import BaseModel


class City(BaseModel):
    '''Public class attributes'''
    state_id = ""
    name = ""
