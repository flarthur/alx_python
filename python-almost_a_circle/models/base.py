"""Base Module

Defines the Base class for creating objects with unique IDs.
"""


class Base:
    """Base Class

    Creates objects with unique IDs.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base object.

        Args:
            id (int, optional): Optional ID for the object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
