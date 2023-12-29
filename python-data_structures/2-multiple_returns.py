def multiple_returns(sentence):
  
  result = ()
  length = len(sentence)
  
  if length >= 1:
    first = sentence[0]
    result = (length, first)
    return result
  
  else:
    first = None
    length = 0
    result = (length, first) 
    return result
  