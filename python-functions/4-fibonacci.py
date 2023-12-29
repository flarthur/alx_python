def fibonacci_sequence(n):
  """This function will print the fibonacci sequence to the value of n"""
  if n <= 0:
        return []

  f_list = [0]
  a, b = 0, 1
  while len(f_list) < n:
    f_list.append(b)
    a, b = b, a + b

  return f_list