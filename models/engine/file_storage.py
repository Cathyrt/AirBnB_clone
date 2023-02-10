#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """Represent an abstracted storage engine.
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in __objects obj with key <obj_class_name>.id"""
        ocname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(ocname, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objdict = {}
        for key, val in odict.items():
            objdict[key] = val.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects, if it exists."""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for i, o in objdict.items():
                    if i not in FileStorage.__objects:
                        cls_name = o["__class__"]
                        if cls_name == "Place":
                            self.new(eval("Place(**o)"))
                        elif cls_name == "State":
                            self.new(eval("State(**o)"))
                        elif cls_name == "City":
                            self.new(eval("City(**o)"))
                        elif cls_name == "Amenity":
                            self.new(eval("Amenity(**o)"))
                        elif cls_name == "Review":
                            self.new(eval("Review(**o)"))
                        elif cls_name == "User":
                            self.new(eval("User(**o)"))
                        elif cls_name == "BaseModel":
                            self.new(eval("BaseModel(**o)"))
        except FileNotFoundError:
            pass
