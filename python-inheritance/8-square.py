"""Task 6"""
Rectangle = __import__("7-rectangle").Rectangle


class BaseGeometryMeta(type):
    """Meta Class for BAseGeometry"""

    def __dir__(self):
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr


class BaseGeometry(metaclass=BaseGeometryMeta):
    """BaseGeometry Class"""

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not type(value) is int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


# class Rectangle(BaseGeometry):
#     """Rectangle SubClass"""

#     def __init__(self, width, height):
#         self.integer_validator("width", width)
#         self.integer_validator("height", height)
#         self.__width = width
#         self.__height = height

#     def __str__(self):
#         return "[Rectangle] {}/{}".format(self.__width, self.__height)

#     def area(self):
#         return self.__width * self.__height


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
        super().__init__(size, size)
