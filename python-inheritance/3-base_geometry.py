"""Task 3"""


class BaseGeometryMeta(type):
    """Meta Class for BAseGeometry"""

    def __dir__(self):
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr


class BaseGeometry(metaclass=BaseGeometryMeta):
    """This is a BaseGeometry Class"""

    def __dir__(self):
        attributes = super().__dir__()
        used_attr = [att for att in attributes if att != "__init_subclass__"]
        return used_attr
