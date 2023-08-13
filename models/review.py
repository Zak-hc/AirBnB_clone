#!/usr/bin/python3
"""
Define a review model
"""
from .base_model import BaseModel


class Review(BaseModel):
    """
    Review an objects
    """
    user_id = ""
    place_id = ""
    text = ""
