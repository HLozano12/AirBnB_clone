#!/usr/bin/python3
"""Doc"""
import json
import os

import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """store the information of airbnb"""

    __file_path = 'file.json'
    __objects = {}    # saving the existing instances
    classes = ['BaseModel', 'User', 'State', 'City', 'Amenity',
               'Place', 'Review']

    def all(self):
        """return __object dictionary"""
        return FileStorage.__objects

    def count(self, arg):
        """return the number of __object keys"""

        list_of_strings = []
        for key, val in models.storage.all().items():
            if arg in key.split("."):
                list_of_strings.append(str(val))
        return len(list_of_strings)

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        # key = "{}.{}".format(self.__class__.__name__, obj.id)
        # FileStorage.__objects[key] = obj
        self.__objects.update({"{}.{}".format(type(obj).__name__,
                                              obj.id): obj})
        # print(type(obj))

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(FileStorage.__file_path, "w") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)

    def reload(self):
        """deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file does not exist,
        no exception should be raised)
        """

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            obj_dict = json.load(f)
            for k, v in obj_dict.items():
                if 'User' in k.split("."):
                    FileStorage.__objects[k] = User(**v)
                if 'BaseModel' in k.split("."):
                    FileStorage.__objects[k] = BaseModel(**v)
                if 'State' in k.split("."):
                    FileStorage.__objects[k] = State(**v)
                if 'City' in k.split("."):
                    FileStorage.__objects[k] = City(**v)
                if 'Place' in k.split("."):
                    FileStorage.__objects[k] = Place(**v)
                if 'Amenity' in k.split("."):
                    FileStorage.__objects[k] = Amenity(**v)
                if 'Review' in k.split("."):
                    FileStorage.__objects[k] = Review(**v)
