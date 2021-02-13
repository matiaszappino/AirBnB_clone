#!/usr/bin/python3
"""File Storage Class"""

import json
class FileStorage():
    """FileStorage class documentation"""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.__dict__["id"] 
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode = "w") as f:
           f.write(json.dumps(FileStorage.__objects, indent=2))

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file (__file_path)"""
        try:
            with open(FileStorage.__file_path, mode = "r") as f:
                FileStorage.__objects = json.load(f)
        except:
            pass
