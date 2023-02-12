#!/usr/bin/python3
"""Module base_model

This Module contains a definition for BaseModel Class
"""

import uuid
from datetime import datetime


class BaseModel:
    """BaseModel Class"""

    def __init__(self):
        """__init__ method & instantiation of class Basemodel

        Args:
            *args.
            **kwargs (dict): Key/value pairs
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update updated_at with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        returns a dictionary containing all
        keys/values of __dict__ of the instance
        """
        cdict = self.__dict__.copy()
        cdict["created_at"] = self.created_at.isoformat()
        cdict["updated_at"] = self.updated_at.isoformat()
        cdict["__class__"] = self.__class__.__name__
        return cdict

    def __str__(self) -> str:
        """should print/str representation of the BaseModel instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
