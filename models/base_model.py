#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ Defin BaseModel class"""
    def __init__(self, *args, **kwargs):
        if(len(kwargs) == 0):
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)
            models.storage.save()
        else:
            kwargs["created_at"] = datetime.strptime(kwargs["created_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            kwargs["updated_at"] = datetime.strptime(kwargs["updated_at"],
                                                     "%Y-%m-%dT%H:%M:%S.%f")
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])

    def __str__(self):
        """Returns String"""
        class_name = self.__class__.__name__
        return"[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """
        Update and save
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        returns a dictionnaire
        """
        dict = dict(**self.__dict__)
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = self.created_at.isoformat()
        dict["updated_at"] = self.updated_at.isoformat()
        return dic
