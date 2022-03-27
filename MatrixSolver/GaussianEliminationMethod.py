# Matrix Solver in Gaussian Elimination Method

# Global Variable [Only Used To print the iteration number]
MATRIX_COUNT = 0


def printIntoFile(data, message, isTrue):
    """
    Printing the data and the message content into a specified file

    :param data: Data from a user
    :param message: Message that contain the data subject
    :param isTrue: Boolean parameter, which help to navigate to the right section
    """
    # Our Global Variable To Count The Iteration Number
    global MATRIX_COUNT

    # In Case We Are Running A New Linear Equation, It will erase the lase one
    if MATRIX_COUNT == 0:
        file = open('GaussianElimination.txt', 'w')
        file.close()

    # Open the file and save the data
    with open('GaussianElimination.txt', 'a+') as file:
        # In case we are in an iteration solution
        if isTrue:
            # In case we are printing new calculation
            if MATRIX_COUNT % 3 == 0:
                file.write('==========================================================================================')

            # Saving the matrix in the file
            file.write('\n' + str(message) + ' [' + str(MATRIX_COUNT) + ']\n')
            for i in range(len(data)):
                for j in range(len(data[0])):
                    objectData = '{: ^22}'.format(data[i][j])
                    file.write(objectData)
                file.write('\n')

            # Increase Our Global Iteration Counter Variable
            MATRIX_COUNT = MATRIX_COUNT + 1

        # Our Solution Data
        else:
            # In case we are printing the solution accuracy
            file.write('==============================================================================================')
            file.write('\n[' + str(message) + ']\n')
            file.write(str(data))
            file.write('\n')


def gaussianElimination():
    """
    Solving linear equation in Gaussian Elimination method

    """
    # Initialize the matrix, and vectorB
    originMatrix, vectorB = initMatrix()

    # Check if the matrix is Quadratic matrix, and check if vectorB is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(vectorB) == len(originMatrix) and len(vectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Getting the inverse matrix of originMatrix, and the fixed vectorB
            inverseMatrix, vectorB = findInverse(originMatrix, vectorB)

            # Getting the accuracy of the solution
            solutionPrecision = matrixCond(originMatrix, inverseMatrix)

            # Saving the matrix solution
            printIntoFile(vectorB, 'Matrix Solution', True)
            printIntoFile(solutionPrecision, 'Solution Accuracy Rate', False)

        # According message In case there is more or less than one solution
        else:
            print('This Is A Singular Matrix')

    # In case the input Linear Equation isn't meet the demands
    else:
        print("The Input Linear Equation Isn't Match")


def findInverse(matrix, vector):
    """
    Solve the matrix into an Identity matrix, updating the vector of the matrix, and return the inverse matrix of matrix

    :param matrix: NxN matrix
    :param vector: Nx1 vector solution of the matrix
    :return: Inverse NxN matrix, the inverse matrix of matrix
    """
    # Initialize inverseMatrix into an Identity matrix
    inverseMatrix = [[1.0 if row == col else 0.0 for col in range(len(matrix))] for row in range(len(matrix))]

    # Solving matrix into an Upper matrix
    for i in range(len(matrix)):
        # Calling function to reArrange the matrix, and the vector
        matrix, vector = checkPivotColumn(matrix, vector, i)

        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                # Multiply into an Upper matrix, updating matrix vector as well, and keep the inverseMatrix updated
                vector = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), vector, False)
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix, False)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix, True)

    # Solving matrix into a Lower matrix
    for i in reversed(range(len(matrix))):
        for j in reversed(range(i)):
            # Multiply into a Lower matrix, updating matrix vector as well, and keep the inverseMatrix updated
            if matrix[j][i] != 0:
                vector = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), vector, False)
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix, False)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix, True)

    # Return the inverse matrix, and the updated solution vector of the matrix
    return inverseMatrix, vector


def checkPivotColumn(matrix, vector, index):
    """
    Taking care that the pivot in the column [index] will be the highest one, and return the updated matrix and vector

    :param matrix: NxN matrix
    :param vector: Nx1 vector solution of the matrix
    :param index: Column index
    :return: The updated matrix and vector
    """
    # Variable to store the max pivot in specific column
    maxPivot = abs(matrix[index][index])

    # Variable to store the new pivot row
    pivotRow = 0

    for j in range(index + 1, len(matrix)):
        # In case there's a higher pivot
        if abs(matrix[j][index]) > maxPivot:
            # Store the new highest pivot, and his row
            maxPivot = abs(matrix[j][index])
            pivotRow = j

    # In case there was a higher pivot, change between the matrix rows
    if maxPivot != abs(matrix[index][index]):
        # Initialize elementary matrix to swap the matrix rows
        elementaryMatrix = [[1.0 if x == y else 0.0 for y in range(len(matrix))] for x in range(len(matrix))]
        elementaryMatrix[index], elementaryMatrix[pivotRow] = elementaryMatrix[pivotRow], elementaryMatrix[index]

        # Changed the Matrix and the vector Rows
        matrix = multiplyMatrix(elementaryMatrix, matrix, True)
        vector = multiplyMatrix(elementaryMatrix, vector, False)

    # In case the pivot isn't one, we will make sure it will be one
    if matrix[index][index] != 1:
        vector = multiplyMatrix(initElementaryMatrix(len(matrix), index, index, 1 / matrix[index][index]), vector, False)
        matrix = multiplyMatrix(initElementaryMatrix(len(matrix), index, index, 1 / matrix[index][index]), matrix, True)

    # Return the updated matrix and vector
    return matrix, vector


def matrixCond(matrix, inverseMatrix):
    """
    Multiply the max norm of the origin and inverse matrix, and return its solution accuracy

    :param matrix: NxN matrix
    :param inverseMatrix: NxN inverse matrix of matrix
    :return: Matrix solution precision
    """
    return infinityNorm(matrix) * infinityNorm(inverseMatrix)


def infinityNorm(matrix):
    """
    Return the Max Norm of the matrix

    :param matrix: NxN matrix
    :return: Infinity norm of the matrix
    """
    norm = 0
    for i in range(len(matrix[0])):
        sumRow = 0
        for j in range(len(matrix)):
            sumRow = sumRow + abs(matrix[i][j])
        norm = max(sumRow, norm)

    # Return the max norm
    return norm


def multiplyMatrix(matrixA, matrixB, isTrue):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrixA: NxM Matrix
    :param matrixB: NxM Matrix
    :param isTrue: Boolean which decide if to save the matrices in a file
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zero's
    matrixC = [[0.0] * len(matrixB[0]) for _ in range(len(matrixA))]

    # Multiply the two matrices and store the outcome in matrixC
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    # Saving the matrices in the right lists
    if isTrue:
        # Saving the matrices in a file
        printIntoFile(matrixA, 'Elementary Matrix', True)
        printIntoFile(matrixB, 'Pre Multiply Matrix', True)
        printIntoFile(matrixC, 'After Multiply Matrix', True)

    # Return the outcome matrix
    return matrixC


def initMatrix():
    """
    Initialize user linear equations, and return them

    :return: NxN matrix, and Nx1 vector B
    """
    # Initialize Linear Equation from the user
    matrix = [[0.913, 0.659], [0.457, 0.330]]
    vectorB = [[0.254], [0.127]]

    # Return the user linear equation
    return matrix, vectorB


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
    elementary_Matrix = [[1.0 if row == col else 0.0 for col in range(size)] for row in range(size)]
    elementary_Matrix[row][col] = value

    # Return the elementary matrix
    return elementary_Matrix


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
        determinant_sub = determinantMatrix([row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        # Adding the calculated determinant value of particular column matrix to total the determinantSum
        determinantSum = determinantSum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinantSum


# Calling our matrix solver main
gaussianElimination()
