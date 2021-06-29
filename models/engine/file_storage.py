#!/usr/bin/python3
"""Defines the FileStorage class."""
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.state import State


class FileStorage:
    """Represent an abstracted storage engine
        Attributes:
            __file_path: string - path to the JSON file (ex: file.json)
            __objects: dictionary - empty but will store all object
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns dictionary object"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        cname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(cname, obj.id)] = obj

    def save(self):
        """ serializes __objects to the JSON file"""
        odict = FileStorage.__objects
        # json takes input as a dict mainly so we convert it to dict
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as j:
            json.dump(objdict, j)

    def reload(self):
        """deserializes the JSON file to __objects if exists"""
        try:
            with open(FileStorage.__file_path) as f:
                objdict = json.load(f)
                for o in objdict.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    # after evaluating unpack dict(**)
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return
