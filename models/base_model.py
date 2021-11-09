#!/usr/bin/python3
import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """ Defin BaseModel class"""
    def __init__(self):
        """ Constructor """
        self.id = str(uuid4())
        self.created_at = datetime.today().strftime("%Y-%d-%m %H:%M:%S.%f")
        self.updated_at = datetime.today().strftime("%Y-%d-%m %H:%M:%S.%f")
     def __str__(self):
        """Return string."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
     def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
