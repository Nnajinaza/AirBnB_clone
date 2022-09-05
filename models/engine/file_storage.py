#!/usr/bin/python3
import json
import os
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return (FileStorage.__objects)

    def new(self, obj):
        FileStorage.__objects["{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        with open("file.json", "w", encoding='utf-8') as new_file:
            new_dict = {}
            for key, value in self.__objects.items():
                new_dict[key] = value.to_dict()
            json.dump(new_dict, new_file)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as new_file:
                new_dict = json.load(new_file)
            for key, value in new_dict.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        except OSError:
            pass
