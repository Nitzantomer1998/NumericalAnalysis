# Author: Nitzan Tomer.
# Matrix Solution.

def print_matrix(matrix):
    """
    Printing matrix

    :param matrix: Matrix NxM
    """
    for row in range(len(matrix)):
        print(matrix[row])


def elementary_matrix_init(size, row, col, value):
    """
    Initialize elementary matrix

    :param size: Matrix size
    :param row: Row index
    :param col: Column index
    :param value: Value parameter
    :return: Return the elementary matrix
    """
    matrix = [[1 if x == y else 0 for y in range(size)] for x in range(size)]
    matrix[row][col] = value

    # Saving the elementary matrix
    elementary_matrix_list.append(matrix)
    return matrix


def multiply_matrix(elementary_matrix, origin_matrix):
    """
    Multiplying two matrices and return the outcome matrix

    :param elementary_matrix: NxN Matrix
    :param origin_matrix: NxN Matrix
    :return: New NxN matrix
    """
    multiplied_matrix = [[0] * len(origin_matrix[0]) for _ in range(len(elementary_matrix))]

    for i in range(len(elementary_matrix)):
        for j in range(len(origin_matrix[0])):
            for k in range(len(origin_matrix)):
                multiplied_matrix[i][j] = multiplied_matrix[i][j] + elementary_matrix[i][k] * origin_matrix[k][j]
    return multiplied_matrix


def matrix_organized(matrix):
    """
    Rearrange the matrix, such that the pivot in every column will be the highest

    :param matrix: NxN matrix
    """
    for i in range(len(matrix)):
        max_pivot = matrix[i][i]
        for j in range(i, len(matrix)):
            if matrix[j][i] > max_pivot:
                max_pivot = matrix[j][i]
                matrix[i], matrix[j] = matrix[j], matrix[i]

    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            return False

    return True


def getcofactor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]


def determinant_matrix(matrix):
    """python program to find
    # determinant of matrix.

    # defining a function to get the
    # minor matrix after excluding
    # i-th row and j-th column.
    """
    # if given matrix is of order 2*2 then simply return det value by cross multiplying elements of matrix.
    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    determinant_sum = 0

    # loop to traverse each column of matrix a.
    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        # calling the function recursily to
        # get determinant value of
        # sub matrix obtained.
        sub_det = determinant_matrix(getcofactor(mat, 0, current_column))

        # adding the calculated determinant
        # value of particular column
        # matrix to total Sum.
        determinant_sum += (sign * matrix[0][current_column] * sub_det)

    # returning the final Sum
    return determinant_sum


def inverse_matrix(matrix):
    if determinant_matrix(matrix):
        matrix_organized(matrix)
        for i in range(len(matrix)):
            if matrix[i][i] != 1:
                matrix = multiply_matrix(elementary_matrix_init(len(matrix), i, i, 1 / matrix[i][i]), matrix)
            for j in range(len(matrix)):
                if i != j:
                    if matrix[j][i] != 0:
                        matrix = multiply_matrix(elementary_matrix_init(len(matrix), j, i, -(matrix[j][i])), matrix)

"""
elementary_matrix_list = []
mat = [[1, -1, -2], [2, -3, -5], [-1, 3, 5]]
inverse_matrix(mat)
for i in range(len(elementary_matrix_list)):
    print_matrix(elementary_matrix_list[i])
    print()
"""
matrix = [[1, 3, -2], [2, 10, -5], [-1, 3, 0]]
if matrix_organized(matrix):
    print_matrix(matrix)

else:
    print("someone went wrong")
