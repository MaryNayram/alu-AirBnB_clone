#!/usr/bin/python3
<<<<<<< HEAD
"""Class representing a user"""
=======
"""Defines the User class."""
>>>>>>> 40e07bb0bc8d2b22c2ecf1f76fc9790eae1e9dbc
from models.base_model import BaseModel


class User(BaseModel):
<<<<<<< HEAD
    """Details of a user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    """def __init__(self, *args, **kwargs):
        Initialize a User instance
        super().__init__(*args, **kwargs)"""
=======
        """Represent a User.
    Attributes:
        email (str): The email of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """

            email = ""
                password = ""
                    first_name = ""
                        last_name = ""
                        
>>>>>>> 40e07bb0bc8d2b22c2ecf1f76fc9790eae1e9dbc
