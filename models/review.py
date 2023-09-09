#!/usr/bin/python3
<<<<<<< HEAD
"""Class Review that inherits from the BaseModel class"""

from models import BaseModel


class Review(BaseModel):
    """Review class"""

    place_id = ""  # string - empty string: it will be the Place.id
    user_id = ""  # string - empty string: it will be the User.id
    text = ""  # string - empty string

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
=======
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
        """Represent a review.
    Attributes:
        place_id (str): The Place id.
        user_id (str): The User id.
        text (str): The text of the review.
    """

            place_id = ""
                user_id = ""
                    text = ""
                    
>>>>>>> 40e07bb0bc8d2b22c2ecf1f76fc9790eae1e9dbc
