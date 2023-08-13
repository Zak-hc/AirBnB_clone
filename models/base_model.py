#!/usr/bin/python3
"""def base
    by zak
"""


import uuid
from datetime import datetime


class BaseModel:
    """Initialize a new BaseModel instance.

    Args:
        my_number (int): An optional integer value.
        name (str): An optional string value.
    """
    def __init__(self, my_number=None, name=None):
        """init"""
        if name is not None and my_number is not None:
            self.my_number = my_number
            self.name = name
        else:
            self.my_number = None
            self.name = None
        self.updated_at = datetime.now()
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()

    def __str__(self):
        """Return strrr"""

        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """Update attribute save"""

        self.updated_at = datetime.now()
        from .__init__ import storage
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Convert the BaseModel instance to a dictionary.

        Returns:
            dict: A dictionary representation of the BaseModel instance.
        """
        delta = self.__dict__.copy()
        delta['__class__'] = type(self).__name__
        if self.created_at is not None:
            delta['created_at'] = self.created_at.isoformat()
        if self.updated_at is not None:
            delta['updated_at'] = self.updated_at.isoformat()
        if self.id is not None:
            delta['id'] = self.id
        return delta
