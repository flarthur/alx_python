"""This is a square module"""
class Square:
  """This class represents a square"""
  def __init__(self, size=0):
    """Initialize the square with the given size"""
    self.__size = size
    
    if not type(size) is int:
      raise TypeError("size must be an integer")
    elif size < 0:
      raise ValueError("size must be >= 0")
      
