#!/usr/bin/python3
# task3

import uuid
from datetime import datetime


class BaseModel:
    """ clasa baseModel"""

    def __init__(self, my_number=None, name=None):
        """init"""

        self.my_number = my_number
        self.name = name
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ instance strrr"""

        return f"[{self.name}] ({self.id}) {self.__dict__}"

    def save(self):
        """ instance save"""

        self.updated_at = datetime.now()

    def to_dict(self):
        """ instance dic"""

        delta = self.__dict__.copy()
        delta['__class__'] = self.name
        delta['created_at'] = self.created_at.isoformat()
        delta['updated_at'] = self.updated_at.isoformat()
        self.__dict__
        return delta
