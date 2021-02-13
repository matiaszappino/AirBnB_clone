#!/usr/bin/python3
"""Base Class"""


from uuid import uuid4
from datetime import datetime
import json
from models import storage

class BaseModel():
    """Base Class description"""

    def __init__(self, *args, **kwargs):
        """Initialization function"""
        self.id = str(uuid4())
        self.created_at = datetime.today().isoformat()
        self.updated_at = datetime.today().isoformat()
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    current = datetime.strptime(value, time_format)
                    self.__dict__[key] = current
                    continue
                self.__dict__[key] = value
        else:
            storage.new(self)
            
    def __str__(self):
        """Method that returns ..."""
        return ("[{}] ({}) {}".format(self.__class__.__name__,
                                      self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at"""
        current = datetime.today()
        self.updated_at = current.isoformat()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of the instance"""
        new_dict = {}
        new_dict["__class__"] = self.__class__.__name__
        for key, value in self.__dict__.items():
            if self.__dict__[key] is None:
                continue
            new_dict[key] = value
        return new_dict