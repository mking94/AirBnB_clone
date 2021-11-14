#!/usr/bin/python3
"""
Base module is the base class for all other classes
"""
from datetime import datetime
import uuid
import models.engine.file_storage
import models


class BaseModel():
    """
    BaseModule
    id: string - assign with an uuid when an instance is created
    created_at: datetime - assign with the current datetime
    updated_at: datetime - assign with the current datetime
    and it will be updated every time you change your object
    """

    f = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        """
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, BaseModel.f)
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        string representation
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id,
                                     self.__dict__)

    def save(self):
        """
        save function
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        change to dictionary
        """
        dict = self.__dict__
        dict["created_at"] = datetime.now().isoformat()
        dict["updated_at"] = datetime.now().isoformat()
        dict["__class__"] = str(type(self).__name__)

        return dict
