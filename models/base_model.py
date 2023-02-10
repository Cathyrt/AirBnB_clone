#!/usr/bin/python3
"""
BaseModel Module
"""
from datetime import datetime
import uuid
from models.engine.file_storage import FileStorage

storage = FileStorage()

class BaseModel():
    """ BaseModel class """

    def __init__(self, *args, **kwargs):
        """ initializes instance attributes """
        time = '%Y-%m-%dT%H:%M:%S.%f'
        dict_found = 0
        if kwargs:
            for item in kwargs:
                dict_found = 1
                if item != '__class__':
                    if item == 'created_at' or item == 'updated_at':
                        kwargs[item] = datetime.strptime(kwargs[item], time)
                    setattr(self, item, kwargs[item])
        if dict_found == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models.__init__ import storage
            storage.new(self)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        from models.__init__ import storage
        storage.save()

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
