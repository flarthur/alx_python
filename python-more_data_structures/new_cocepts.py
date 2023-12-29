#!New Cocepts

#!! Task 0
#* To get the square of a list nested in a list, use the formula below:

matrix = [
          [1, 2, 3],
          [3, 4, 5],
          [4, 5, 8]
]

print(matrix)

print([[y**2 for y in x] for x in matrix])

#!! Returning the key with the biggest value 

try:
    biggest_int = max(a_dictionary, key=a_dictionary.get)
    return biggest_int
  except (AttributeError, ValueError):
    return None
