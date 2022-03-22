# Author: Nitzan Tomer.
# Matrix Solver.


def gaussian_Elimination():
    """
    Solving linear equation in LU Gaussian Elimination method

    """
    # Initialize matrices and vectors
    origin_Matrix, vector_B = init_Matrix()

    # Getting matrix U and matrix_L
    matrix_U = find_U(origin_Matrix)
    matrix_L = matrix_Temp[0]

    # Now find solution for matrix_L (Ly = B)
    # matrix_L solution

    # Solve Ly = B
    vector_Y = [[0.0], [0.0], [0.0]]
    vector_Y[0][0] = vector_B[0][0] / matrix_L[0][0]
    vector_Y[1][0] = (vector_B[1][0] - vector_Y[0][0] * matrix_L[1][0]) / matrix_L[1][1]
    vector_Y[2][0] = (vector_B[2][0] - (vector_Y[0][0] * matrix_L[2][0] + vector_Y[1][0] * matrix_L[2][1])) / matrix_L[2][2]

    # Solve Ux = y
    vector_X = [[0.0], [0.0], [0.0]]
    vector_X[2][0] = vector_Y[2][0] / matrix_U[2][2]
    vector_X[1][0] = (vector_Y[1][0] - vector_X[2][0] * matrix_U[1][2]) / matrix_U[1][1]
    vector_X[0][0] = (vector_Y[0][0] - (vector_X[2][0] * matrix_U[0][2] + vector_X[1][0] * matrix_U[0][1])) / matrix_U[0][0]
    # Return the solution vector
    return vector_X


def init_Matrix():
    """
    Initialize user linear equations, and return them

    :return: NxN matrix, and Nx1 vector B
    """
    # Asking for matrix size
    size = int(input('Matrix Size --> '))

    # Initialize matrix to zero's
    matrix = [[0.0 for col in range(size)] for row in range(size)]

    # Initialize matrix_L to matrix Unit
    matrix_Temp.append([[1.0 if row == col else 0.0 for col in range(size)] for row in range(size)])

    # Initialize vector_B to zero's
    vector_B = [[0.0 for col in range(1)] for row in range(size)]

    # Initialize matrix according to the user
    print('[Initialize Matrix]')
    for row in range(size):
        for col in range(size):
            matrix[row][col] = float(input(f'Matrix[{row}][{col}] Value --> '))

        # Initialize vector solution according to the user
        vector_B[row][0] = float(input(f'Vector_B[{row}] Value --> '))
        print()

    # Return
    return matrix, vector_B


def init_Elementary_Matrix(size, row, col, value):
    """
    Initialize elementary matrix, from identity matrix, and a specific value, and return it

    :param size: Matrix size
    :param row: Row index
    :param col: Column index
    :param value: Value parameter
    :return: Return the elementary matrix
    """
    # Initialize the desire elementary matrix
    elementary_Matrix = [[1 if row == col else 0 for col in range(size)] for row in range(size)]
    elementary_Matrix[row][col] = value

    # Building Matrix_L
    matrix_Temp[0][row][col] = -value

    # Return the elementary matrix
    return elementary_Matrix


def multiply_Matrix(matrix_A, matrix_B, flag):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrix_A: NxM Matrix
    :param matrix_B: NxM Matrix
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zeros
    matrix_C = [[0.0] * len(matrix_B[0]) for row in range(len(matrix_A))]

    # Multiply the two matrices and store the outcome in matrix_C
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B[0])):
            for k in range(len(matrix_B)):
                matrix_C[i][j] = matrix_C[i][j] + matrix_A[i][k] * matrix_B[k][j]

    # Adding the matrices to the right lists
    if flag:
        elementary_Matrix_List.append(matrix_A)
        current_Matrix.append(matrix_B)
        final_Matrix.append(matrix_C)

    # Return the outcome matrix
    return matrix_C


def find_U(matrix):
    """
    Solve the matrix into an Upper matrix, and return it

    :param matrix: NxN matrix
    :return: Upper NxN matrix
    """
    # Solving matrix into an Upper matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                matrix = multiply_Matrix(init_Elementary_Matrix(len(matrix), j, i, -(matrix[j][i]) / matrix[i][i]), matrix, True)

    # Return the Upper matrix
    return matrix


def print_gaussian_elimination(elementary_matrices, current_matrices, outcome_matrices):
    """
    Printing all the LU Gaussian Elimination process

    :param elementary_matrices: List of NxN matrices
    :param current_matrices: List of NxN matrices
    :param outcome_matrices: List of NxN matrices
    """
    for i in range(len(elementary_matrices)):
        print('\n[Iterator Number --> ' + str(i) + ']')
        for j in range(len(elementary_matrices[i])):
            if j == 1:
                print(str(elementary_matrices[i][j]) + ' X ' + str(current_matrices[i][j]) + ' = ' + str(outcome_matrices[i][j]))

            else:
                print(str(elementary_matrices[i][j]) + ' ' + str(current_matrices[i][j]) + '  ' + str(outcome_matrices[i][j]))


def driver():
    vector_solution = gaussian_Elimination()
    print_gaussian_elimination(elementary_Matrix_List, current_Matrix, final_Matrix)
    print(vector_solution)


elementary_Matrix_List = []
current_Matrix = []
final_Matrix = []
matrix_Temp = []
driver()

