for tens in range(10):
  for ones in range(tens + 1, 10):
    print("{}{}".format(tens, ones), end=", " if ones != 9 or tens != 8 else "\n")