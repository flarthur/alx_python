"""Task 6"""
BaseGeometry = __import__("5-base_geometry").BaseGeometry

# class BaseGeometryMeta(type):
#     """Meta Class for BAseGeometry"""

#     def __dir__(self):
#         attributes = super().__dir__()
#         used_attr = [att for att in attributes if att != "__init_subclass__"]
#         return used_attr


# class BaseGeometry(metaclass=BaseGeometryMeta):
#     """BaseGeometry Class"""

#     def __dir__(self) -> None:
#         """This will control inherited attribute access"""
#         attributes = super().__dir__()
#         used_attr = [att for att in attributes if att != "__init_subclass__"]
#         return used_attr

#     def area(self):
#         raise Exception("area() is not implemented")

#     def integer_validator(self, name, value):
#         if not isinstance(value, int):
#             raise TypeError("{} must be an integer".format(name))
#         elif value <= 0:
#             raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle SubClass"""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
