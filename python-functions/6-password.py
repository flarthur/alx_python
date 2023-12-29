def validate_password(password):
  """This function validates the password to make sure it meets certain conditions:"""
  contain_upper = False
  contain_lower = False
  contain_digit = False
  no_space = False
  
  if len(password) < 8:
    return False
  
  for char in password:
    if char.isupper():
      contain_upper = True
    elif char.islower():
      contain_lower = True
    elif char.isdigit():
      contain_digit = True
      
    if char.isspace():
      return False
      
  return contain_upper and contain_lower and contain_digit
  