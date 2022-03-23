# Author: Nitzan Tomer.
# Matrix Solver.


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


def gaussian_Elimination():
    """
    Solving linear equation in LU Gaussian Elimination method, and return the solution

    """
    # Initialize the matrix, and vector_B
    origin_Matrix, vector_B = init_Matrix()

    # In case the matrix has one solution
    if determinant_Matrix(origin_Matrix):

        # Getting matrix U and matrix_L
        matrix_U = find_U(origin_Matrix)
        matrix_L = matrix_Temp[0]

        # Solve Ly = B
        vector_Y = forward_Substitution(matrix_L, vector_B)

        # Solve Ux = y
        vector_X = back_Substitution(matrix_U, vector_Y)

        # Getting the inverse matrix
        inverse_U = negative_Matrix(matrix_U)
        inverse_L = negative_Matrix(matrix_L)

        # Getting the solution accuracy
        solution_Precision = cond_A(origin_Matrix, multiply_Matrix(inverse_U, inverse_L, False))
        print('Solution Precision --> ' + str(solution_Precision))

        # Return Vector solution
        return vector_X


def find_U(matrix):
    """
    Solve the matrix into an Upper matrix, and return it

    :param matrix: NxN matrix
    :return: Upper NxN matrix
    """

    # Solving matrix into an Upper matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix = multiply_Matrix(init_Elementary_Matrix(len(matrix), j, i, -(matrix[j][i]) / matrix[i][i]), matrix, True)

    # Return the Upper matrix
    return matrix


def forward_Substitution(lower_Matrix, vector_B):
    """
    Solve Ly = B, and return the vector y

    :param lower_Matrix: NxN lower matrix
    :param vector_B: Nx1 vector B
    :return: Nx1 vector solution
    """
    # Initialize vector_Y
    vector_Y = [[0.0 for col in range(1)] for row in range(len(lower_Matrix))]

    # Solve Ly = B
    for i in range(len(lower_Matrix)):
        vector_Y[i][0] = vector_B[i][0]
        for j in range(i):
            vector_Y[i][0] = vector_Y[i][0] - lower_Matrix[i][j] * vector_Y[j][0]
        vector_Y[i][0] = vector_Y[i][0] / lower_Matrix[i][i]

    # Return vector solution
    return vector_Y


def back_Substitution(upper_Matrix, vector_Y):
    """
    Solve Ux = y, and return the vector x

    :param upper_Matrix: NxN upper matrix
    :param vector_Y: Nx1 vector Y
    :return: Nx1 vector solution
    """
    # Initialize vector_X
    vector_X = [[0.0 for col in range(1)] for row in range(len(upper_Matrix))]
    vector_X[len(upper_Matrix) - 1][0] = vector_Y[len(upper_Matrix) - 1][0] / upper_Matrix[len(upper_Matrix) - 1][len(upper_Matrix) - 1]

    # Solve Ux = y
    for i in range(len(upper_Matrix) - 2, -1, -1):
        sum = vector_Y[i][0]
        for j in range(i + 1, len(upper_Matrix)):
            sum = sum - upper_Matrix[i][j] * vector_X[j][0]
        vector_X[i][0] = sum / upper_Matrix[i][i]

    # Return vector solution
    return vector_X


def cond_A(matrix, inverse_Matrix):
    """
    Return the Precision of the matrix

    :param matrix: NxN matrix
    :param inverse_Matrix: The inverse of matrix
    :return: Matrix sulotion precision
    """
    return inf_Norm(inverse_Matrix) * inf_Norm(matrix)


def inf_Norm(matrix):
    """
    Return the Max Norm of the matrix

    :param matrix: NxN matrix
    :return: Infinity norm of the matrix
    """
    norm = 0
    for i in range(len(matrix[0])):
        sum_Row = 0
        for j in range(len(matrix)):
            sum_Row = sum_Row + abs(matrix[i][j])
        norm = max(sum_Row, norm)
    return norm


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
    """
    print('[Initialize Matrix]')
    for row in range(size):
        for col in range(size):
            matrix[row][col] = float(input(f'Matrix[{row}][{col}] Value --> '))

        # Initialize vector solution according to the user
        vector_B[row][0] = float(input(f'Vector_B[{row}] Value --> '))
        print()
    """
    matrix = [[1.0, 1.0, -1.0], [1.0, -2.0, 3.0], [2.0, 3.0, 1.0]]
    vector_B = [[4.0], [-6.0], [7.0]]

    # Return the user linear equation
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
    elementary_Matrix = [[1.0 if row == col else 0.0 for col in range(size)] for row in range(size)]
    elementary_Matrix[row][col] = value

    # Building Matrix_L
    matrix_Temp[0][row][col] = -value

    # Return the elementary matrix
    return elementary_Matrix


def determinant_Matrix(matrix):
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
        determinant_sub = determinant_Matrix([row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        # Adding the calculated determinant value of particular column matrix to total the determinant_sum
        determinant_sum = determinant_sum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinant_sum


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


def negative_Matrix(matrix):
    """
    Return the inverse matrix

    :param matrix: NxN matrix
    :return: Inverse matrix
    """
    # Initialize inverse_Matrix to identity matrix
    inverse_Matrix = [[1.0 if row == col else 0.0 for col in range(len(matrix))] for row in range(len(matrix))]

    # Change the matrix, into -(matrix) but identity
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if i != j:
                inverse_Matrix[i][j] = - matrix[i][j]

    # Return the inverse matrix
    return inverse_Matrix


def driver():
    vector_solution = gaussian_Elimination()
    print(vector_solution)


elementary_Matrix_List = []
current_Matrix = []
final_Matrix = []
matrix_Temp = []
driver()

