#!/usr/bin/python3
"""Doc"""
import json
import os

import models
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """store the information of airbnb"""

    __file_path = 'file.json'
    __objects = {}    # saving the existing instances
    classes = {'BaseModel': BaseModel,
               'User': User}

    def all(self):
        """return __object dictionary"""
        self.reload()
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""

        key = "{}.{}".format(type(obj).__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""

        with open(FileStorage.__file_path, "w") as f:
            d = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(d, f)
            f.close()

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ;
            otherwise, do nothing. If the file does not exist, no exception should be raised)
        """

        if not os.path.isfile(FileStorage.__file_path):
            return
        with open(FileStorage.__file_path, "r") as f:
            obj_dict = json.load(f)
            for k, v in obj_dict.items():
                FileStorage.__objects[k] = BaseModel(**v)
            f.close()
