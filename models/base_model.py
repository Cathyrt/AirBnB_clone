#!/usr/bin/python3
"""Defines the BaseModel class."""
from datetime import datetime
import uuid
import models


class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ initializes instance attributes """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionary containing all keys/values of __dict__
        of the instance + the class name in the key __class__
        """
        newdict = self.__dict__.copy()
        newdict.update({'__class__': self.__class__.__name__})
        if hasattr(self, 'updated_at'):
            newdict.update({'updated_at': str(self.updated_at.isoformat())})
        newdict.update({'created_at': str(self.created_at.isoformat())})
        return newdict

    def __str__(self):
        """ prints [<class name>] (<self.id>) <self.__dict__> """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)
