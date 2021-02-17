#!/usr/bin/python3
"""File Storage Class"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage():
    """FileStorage class documentation"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.__dict__["id"]
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        dict_obj = {}
        '''FileStorage.__objects = {"User.9324398432": "Puntero Al objeto"}
        dict_obj[User.9324398432] = {"__class__": User, ...}'''
        for key, val in FileStorage.__objects.items():
            dict_obj[key] = val.to_dict()
        with open(FileStorage.__file_path, mode="w") as f:
            f.write(json.dumps(dict_obj, indent=2))

    def reload(self):
        '''Method to deserializes a JSON file to an attribute __objects'''
        classes = {'BaseModel': BaseModel, 'User': User,
                   'State': State, 'City': City, 'Amenity': Amenity,
                   'Place': Place, 'Review': Review}
        fs = FileStorage.__objects
        try:
            with open('{}'.format(FileStorage.__file_path), 'r') as File:
                objs = json.load(File)
                for key in objs:
                    fs[key] = classes[objs[key]['__class__']](**objs[key])
                '''Objects[key] = User.9324398432
                Objects[key]['__class__'] = "User"
                classes["User"](**objects[User.9324398432])
                User(**object[User.9324398432])'''
        except FileNotFoundError:
            pass
