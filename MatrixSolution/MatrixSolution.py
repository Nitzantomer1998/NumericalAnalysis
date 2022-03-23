# Author: Nitzan Tomer.
# Matrix Solver.

def print_matrix(matrix):
    """
    Printing matrix

    :param matrix: Matrix NxM
    """
    # Printing the matrix
    print('[Matrix Print]')
    for row in range(len(matrix)):
        print(matrix[row])


def print_solution(vector_solution):
    """
    Print the matrix solution

    :param vector_solution: Nx1 matrix
    """
    # Printing the vector solution
    print('[Vector Solution]')
    for i in range(len(vector_solution)):
        print(chr(65 + i) + ' --> ' + str(vector_solution[i][0]))


def print_elementary_matrix(elementary_matrices):
    """
    Printing all the elementary matrices

    :param elementary_matrices: List of NxN matrices
    """
    # Printing the elementary matrices
    print('[Elementary Matrices]')
    for i in reversed(range(len(elementary_matrices))):
        print('\n[Elementary Matrix[' + str(i) + ']')
        print_matrix(elementary_matrices[i])


def organize_matrix(matrix):
    """
    Rearrange the matrix, such that the pivot in every column will be the highest

    :param matrix: NxN matrix
    :return: Return True if the matrix pivots are not Zero, and they are the highest in every column
    """
    for i in range(len(matrix)):
        max_pivot = abs(matrix[i][i])
        for j in range(i, len(matrix)):
            if abs(matrix[j][i]) > max_pivot:
                max_pivot = abs(matrix[j][i])
                matrix[i], matrix[j] = matrix[j], matrix[i]

    for i in reversed(range(len(matrix))):
        if matrix[i][i] == 0:
            matrix[i], matrix[i - 1] = matrix[i - 1], matrix[i]

    for i in range(len(matrix)):
        if matrix[i][i] == 0:
            # Return false in case arbitrary pivot is zero
            return False

    # Return true if the matrix pivots in the right order
    return True


def elementary_matrix_init(size, row, col, value):
    """
    Initialize elementary matrix, from identity matrix, and a specific value, and return it

    :param size: Matrix size
    :param row: Row index
    :param col: Column index
    :param value: Value parameter
    :return: Return the elementary matrix
    """
    # Initialize the desire elementary matrix
    elementary_matrix = [[1 if x == y else 0 for y in range(size)] for x in range(size)]
    elementary_matrix[row][col] = value

    # Saving the elementary matrix in an array
    elementary_matrix_array.append(elementary_matrix)

    # Return the elementary matrix
    return elementary_matrix


def multiply_matrix(matrix_a, matrix_b):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrix_a: NxM Matrix
    :param matrix_b: NxM Matrix
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zeros
    multiplied_matrix = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    # Multiply the two matrices and store the outcome in the new matrix
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                multiplied_matrix[i][j] = multiplied_matrix[i][j] + matrix_a[i][k] * matrix_b[k][j]

    # Return the outcome matrix
    return multiplied_matrix


def get_co_factor(m, i, j):
    return [row[: j] + row[j + 1:] for row in (m[: i] + m[i + 1:])]


def determinant_matrix(matrix):
    """
    Calculate the matrix determinant and return the result

    :param matrix: NxN Matrix
    :return: Matrix determinant
    """
    # Simple case, The matrix size is 2x2
    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    # Initialize our sum variable
    determinant_sum = 0

    # Loop to traverse each column of the matrix
    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        # Calling the function recursively to get determinant value of sub matrix obtained
        determinant_sub = determinant_matrix(get_co_factor(matrix, 0, current_column))

        # Adding the calculated determinant value of particular column matrix to total the determinant_sum
        determinant_sum = determinant_sum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinant_sum


def inverse_matrix(matrix):
    """
    Find the inverse matrix of the sent matrix and return it

    :param matrix: NxN matrix
    :return: NxN inverse matrix
    """
    if determinant_matrix(matrix):
        if organize_matrix(matrix):
            for i in range(len(matrix)):
                if matrix[i][i] != 1:
                    matrix = multiply_matrix(elementary_matrix_init(len(matrix), i, i, 1 / matrix[i][i]), matrix)
                for j in range(len(matrix)):
                    if i != j:
                        if matrix[j][i] != 0:
                            matrix = multiply_matrix(elementary_matrix_init(len(matrix), j, i, -(matrix[j][i])), matrix)

            inversed_matrix = elementary_matrix_array[0]
            for i in range(1, len(elementary_matrix_array)):
                inversed_matrix = multiply_matrix(elementary_matrix_array[i], inversed_matrix)
            return inversed_matrix

    else:
        print('Matrix Not Singular')


def gaussian_elimination(matrix, vector_b):
    """
    Solving the matrix in Gaussian Elimination method, and return the solution

    :param matrix: NxM matrix
    :param vector_b: Nx1 matrix
    :return: The vector solution
    """
    # Return the outcome matrix from multiply the reverse matrix with Vector_b
    return multiply_matrix(inverse_matrix(matrix), vector_b)


elementary_matrix_array = []
mat = [[1, -1, -2], [2, -3, -5], [-1, 3, 5]]
vector_b = [[5], [5], [5]]
vector_solution = gaussian_elimination(mat, vector_b)
print()
