"""Square Class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """properties inherited from parent class"""
        super().__init__(size, size, x, y, id)
        self.width = size
        self.height = size
        self.x = x
        self.y = y

    """making size accessible for getter/setter"""

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")
        self.width = value
        self.height = value

    """To override __str__ method"""

    def __str__(self):
        """__"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
