def best_score(a_dictionary):
  
  try:
    biggest_int = max(a_dictionary, key=a_dictionary.get)
    return biggest_int
  except (AttributeError, ValueError):
    return None
