"""This is task 1"""


def is_kind_of_class(obj, a_class):
    """This returns true if the object an instance of, or if the object is an
    instance of a class that inherited from, the specified class"""
    some_class = type(obj)

    if issubclass(some_class, a_class) == True:
        return True
    else:
        return False
