#!/usr/bin/python3
<<<<<<< HEAD
"""Class State that inherits from the BaseModel class"""

from models import BaseModel


class State(BaseModel):
    """State class"""

    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
=======
"""Defines the State class."""
from models.base_model import BaseModel


class State(BaseModel):
        """Represent a state.
    Attributes:
        name (str): The name of the state.
    """

            name = ""
            
>>>>>>> 40e07bb0bc8d2b22c2ecf1f76fc9790eae1e9dbc
