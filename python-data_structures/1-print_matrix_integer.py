def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(*("{:d}".format(num) for num in row), sep=" ")