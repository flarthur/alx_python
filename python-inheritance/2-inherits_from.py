"""This is task 1"""


def inherits_from(obj, a_class):
    """t returns True if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class ; otherwise False
    """
    some_class = type(obj)

    return issubclass(some_class, a_class) and some_class is not a_class
