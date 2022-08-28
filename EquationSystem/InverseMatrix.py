# Solving Equation System Using Inverse Matrix Method


# Global Variable [Only Used To print the iteration number]
PRINT_COUNTER = 0


def inverse_matrix_method(origin_matrix, origin_vector_b):
    if not is_equation_system_valid(origin_matrix, origin_vector_b):
        return

    organize_matrix(origin_matrix, origin_vector_b)

    inverse_matrix = find_inverse(origin_matrix)

    semi_solution = multiply_matrices(inverse_matrix, origin_vector_b, False)
    vector_solution = find_final_solution(origin_matrix, origin_vector_b, semi_solution)

    print_into_file(vector_solution, 'Equation System Final Solution')

    print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, vector_solution))}')


def organize_matrix(origin_matrix, origin_vector_b):
    
    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Inserted Equation System\n')

    for i in range(len(origin_matrix)):

        max_pivot = abs(origin_matrix[i][i])

        new_pivot_row = -1

        for j in range(i + 1, len(origin_matrix)):

            if abs(origin_matrix[j][i]) > max_pivot:
                max_pivot = abs(origin_matrix[j][i])
                new_pivot_row = j

        if max_pivot != abs(origin_matrix[i][i]):
            origin_vector_b[i], origin_vector_b[new_pivot_row] = origin_vector_b[new_pivot_row], origin_vector_b[i]
            origin_matrix[i], origin_matrix[new_pivot_row] = origin_matrix[new_pivot_row], origin_matrix[i]

    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Updated Equation System')


def findInverse(matrix):
    """
    Solve the matrix into an Identity matrix, and return the inverse matrix

    :param matrix: NxN matrix
    :return: Inverse NxN matrix
    """
    # Initialize inverseMatrix into an Identity matrix
    inverseMatrix = [[1 if row == col else 0 for col in range(len(matrix))] for row in range(len(matrix))]

    # Solving matrix into an Identity matrix, and get alongside the Inverse Matrix (Lower part)
    for i in range(len(matrix)):

        # In case the pivot isn't one, we will make sure it will be
        if matrix[i][i] != 1:
            inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), i, i, 1 / matrix[i][i]), inverseMatrix, False)
            matrix = multiplyMatrix(initElementaryMatrix(len(matrix), i, i, 1 / matrix[i][i]), matrix, True)

        # In case the column under the pivot isn't zero
        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix, False)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix, True)

    # Solving matrix into an Identity matrix, and get alongside the Inverse Matrix (Upper part)
    for i in reversed(range(len(matrix))):

        # In case the column above the pivot isn't zero
        for j in reversed(range(i)):
            if matrix[j][i] != 0:
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix, False)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix, True)

    # Return the inverse matrix
    return inverseMatrix


def finalSolution(originMatrix, originVectorB, vectorSolution):
    """
    Getting the equation system components, check the accuracy of the solution, if the accuracy isn't precise
    calculate the precise solution and return it

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :param vectorSolution: Nx1 vector semi solution (not surly accurate)
    :return: Nx1 vector, the precise Equation System solution
    """
    # Solve r = Ax0 - b (Vector r represent the accuracy of the solution we found)
    vectorR = multiplyMatrix(originMatrix, vectorSolution, False)
    for i in range(len(vectorR)):
        vectorR[i][0] = vectorR[i][0] - originVectorB[i][0]

    # In case the equation system solution has round error
    if sum(list(map(sum, vectorR))) != 0:
        printIntoFile(vectorSolution, 'Equation System Solution With Round Error')

    # Update to the accurate solution
    for i in range(len(vectorSolution)):
        if abs(vectorSolution[i][0] - round(vectorSolution[i][0])) <= max(1e-09 * max(abs(vectorSolution[i][0]), abs(round(vectorSolution[i][0]))), 0):
            vectorSolution[i][0] = round(vectorSolution[i][0])

    # Return the final solution of the equation system
    return vectorSolution


def multiplyMatrix(matrixA, matrixB, isTrue):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrixA: NxM Matrix
    :param matrixB: NxM Matrix
    :param isTrue: Boolean which say if to save the matrices in a file
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zero's
    matrixC = [[0] * len(matrixB[0]) for _ in range(len(matrixA))]

    # Multiply the two matrices and store the outcome in matrixC
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    # Saving the matrices in a file
    if isTrue:

        # Global variable to follow the iteration calculation
        global PRINT_COUNTER
        PRINT_COUNTER = PRINT_COUNTER + 1

        printIntoFile(matrixA, 'Elementary Matrix')
        printIntoFile(matrixB, 'Pre Multiply Matrix')
        printIntoFile(matrixC, 'After Multiply Matrix')

    # Return the outcome matrix
    return matrixC


def initElementaryMatrix(size, row, col, value):
    """
    Initialize elementary matrix, from identity matrix, and a specific value, and return it

    :param size: Matrix size
    :param row: Row index
    :param col: Column index
    :param value: Value parameter
    :return: Return the elementary matrix
    """
    # Initialize the desire elementary matrix
    elementaryMatrix = [[1 if row == col else 0 for col in range(size)] for row in range(size)]
    elementaryMatrix[row][col] = value

    # Return the elementary matrix
    return elementaryMatrix


def determinantMatrix(matrix):
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
    determinantSum = 0

    # Loop to traverse each column of the matrix
    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        # Calling the function recursively to get determinant value of sub matrix obtained
        determinant_sub = determinantMatrix(
            [row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        # Adding the calculated determinant value of particular column matrix to total the determinantSum
        determinantSum = determinantSum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinantSum


def printIntoFile(data, message):
    """
    Printing the content into a specified file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    """
    # Open file and save the sent content
    with open('Calculation.txt', 'a+') as file:

        # In case we sent a message
        if message:
            file.write(f'{message} ({PRINT_COUNTER})\n' if PRINT_COUNTER > 0 else f'{message}\n')

        # In case we sent a data
        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('\n')
            file.write('\n')

        # Used to enhance the appearance
        if message == 'Updated Equation System' or message == 'After Multiply Matrix':
            file.write('============================================================================================\n')


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------ Inverse Matrix Method ------------------------------\n')


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Input section
    inputMatrix = [[2, 2, 2], [2, -1, 1], [-1, -1, 2]]
    inputVectorB = [[4], [-1], [-5]]

    # Running the program
    print('---------- Inverse Matrix Method ----------')
    InverseMatrix(inputMatrix, inputVectorB)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
