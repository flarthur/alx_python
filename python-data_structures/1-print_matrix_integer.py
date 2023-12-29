def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    
    for row in matrix:
        row_length = len(row)
        for m in range(row_length):
            if m!= 0:
                print(" ", end="")
            print("{:d}".format(row[m]), end="")
        print()