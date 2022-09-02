#!/usr/bin/python3
'''Create Basemodel to define all common attribute/methods'''
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    ''' Create public instance attributes

        Args:
            id: used to create a unique id for each Basemodel
            created_at: assigns the current time an instance is created
            updated_at: assigns the current time an instance is updated
    '''
    id = str(uuid4())
    created_at = datetime.now()
    updated_at = datetime.now()

    def __init__(self, *args, **kwargs):
        '''Initialize the public instance attriibutes'''
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        models.storage.new(self)

        if len(kwargs):
            for key, value in kwargs.items():
                date_string = "%Y-%m-%dT%H:%M:%S.%f"
                if key in ["created_at", "updated_at"]:
                    self.__dict__[key] = datetime.strptime(value, date_string)

                else:
                    self.__dict__[key] = value


    def __str__(self):
        '''Return details about the class'''
        return ("[{self.__class__.__name__}] ({}) {}".format(self.id, self.__dict__, self=self))

    def save(self):
        '''Is used to update the time when the object is changed'''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        '''Returns a dictionary of the key and values of the instances'''
        my_dict = self.__dict__.copy()
        my_dict['__class__'] = self.__class__.__name__
        my_dict["created_at"] = self.created_at.isoformat()
        my_dict["updated_at"] = self.updated_at.isoformat()
        return (my_dict)
