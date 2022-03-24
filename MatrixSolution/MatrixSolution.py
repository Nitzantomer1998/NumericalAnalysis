# Author: Nitzan Tomer.
# Matrix Solver.


def multiplyMatrix(matrixA, matrixB, isTrue):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrixA: NxM Matrix
    :param matrixB: NxM Matrix
    :param isTrue: boolean which decide if save matrices in a list
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zeros
    matrixC = [[0.0] * len(matrixB[0]) for _ in range(len(matrixA))]

    # Multiply the two matrices and store the outcome in matrixC
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    # Saving the matrices in the right lists
    if isTrue:
        elementaryMatrixList.append(matrixA)
        preFinalMatrixList.append(matrixB)
        finalMatrixList.append(matrixC)

    # Return the outcome matrix
    return matrixC


def gaussianElimination():
    """
    Solving linear equation in LU Gaussian Elimination method

    """
    # Initialize the matrix, vectorB. and matrixL
    originMatrix, vectorB, matrixL = initMatrix()

    # In case the matrix has one solution
    if determinantMatrix(originMatrix):

        # Getting matrix U and matrixL
        matrixU, vectorB, matrixL = findU(originMatrix, vectorB, matrixL)

        # Solve Ly = B
        vectorY = forwardSubstitution(matrixL, vectorB)

        # Solve Ux = y
        vectorX = backSubstitution(matrixU, vectorY)

        # Getting the inverse LU matrices
        inverseU = inverseLU(matrixU)
        inverseL = inverseLU(matrixL)

        # Getting the solution accuracy
        solutionPrecision = matrixCond(originMatrix, multiplyMatrix(inverseU, inverseL, False))

        print('***********************')
        print('Solution Precision --> ' + str(solutionPrecision))
        print('***********************')

        # Showing the matrix solution
        print(vectorX)


def findU(matrix, vector, lowerMatrix):
    """
    Solve the matrix into an Upper matrix, updating the Lower matrix, and adjust the vector solution accordingly

    :param matrix: NxN matrix
    :param vector: Nx1 vector solution of the matrix
    :param lowerMatrix: NxN matrix
    :return: Upper NxN matrix, updated lowerMatrix
    """

    # Solving matrix into an Upper matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            # Updating the lower matrix
            lowerMatrix[j][i] = matrix[j][i] / matrix[i][i]

            # Multiply into an upper matrix, and apply it on vector solution as well
            vector = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, -(matrix[j][i]) / matrix[i][i]), vector, False)
            matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, -(matrix[j][i]) / matrix[i][i]), matrix, True)

    # Return the Upper matrix, the adjust vector of the matrix, and lower matrix
    return matrix, vector, lowerMatrix


def forwardSubstitution(lowerMatrix, vectorB):
    """
    Solve Ly = B, and return the vector y

    :param lowerMatrix: NxN lower matrix
    :param vectorB: Nx1 vector B
    :return: Nx1 vector solution
    """
    # Initialize vectorY
    vectorY = [[0.0 for _ in range(1)] for _ in range(len(lowerMatrix))]

    # Solve Ly = B
    for i in range(len(lowerMatrix)):
        vectorY[i][0] = vectorB[i][0]
        for j in range(i):
            vectorY[i][0] = vectorY[i][0] - lowerMatrix[i][j] * vectorY[j][0]
        vectorY[i][0] = vectorY[i][0] / lowerMatrix[i][i]

    # Return vector solution
    return vectorY


def backSubstitution(upperMatrix, vectorY):
    """
    Solve Ux = y, and return the vectorX

    :param upperMatrix: NxN upper matrix
    :param vectorY: Nx1 vector Y
    :return: Nx1 vector solution
    """
    # Initialize vectorX
    vectorX = [[0.0 for _ in range(1)] for _ in range(len(upperMatrix))]
    vectorX[len(upperMatrix) - 1][0] = vectorY[len(upperMatrix) - 1][0] / upperMatrix[len(upperMatrix) - 1][len(upperMatrix) - 1]

    # Solve Ux = y
    for i in range(len(upperMatrix) - 2, -1, -1):
        rowSum = vectorY[i][0]
        for j in range(i + 1, len(upperMatrix)):
            rowSum = rowSum - upperMatrix[i][j] * vectorX[j][0]
        vectorX[i][0] = rowSum / upperMatrix[i][i]

    # Return vector solution
    return vectorX


def matrixCond(matrix, inverseMatrix):
    """
    Return the Precision of the matrix

    :param matrix: NxN matrix
    :param inverseMatrix: The inverse matrix of matrix
    :return: Matrix solution precision
    """
    return infNorm(inverseMatrix) * infNorm(matrix)


def infNorm(matrix):
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


def inverseLU(matrix):
    """
    Return the inverse matrix of LU

    :param matrix: NxN matrix
    :return: LU Inverse matrix
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


def initMatrix():
    """
    Initialize user linear equations, and return them

    :return: NxN matrix, and Nx1 vector B
    """
    # Asking for matrix size
    size = int(input('Matrix Size --> '))

    # Initialize matrix to zero's
    matrix = [[0.0 for _ in range(size)] for _ in range(size)]

    # Initialize vectorB to zero's
    vectorB = [[0.0 for _ in range(1)] for _ in range(size)]

    # Initialize matrixL to matrix Unit
    matrixL = [[1.0 if row == col else 0.0 for col in range(size)] for row in range(size)]

    # Initialize matrix from the user
    print('[Initialize Matrix]')
    for row in range(size):
        for col in range(size):
            matrix[row][col] = float(input(f'Matrix[{row}][{col}] Value --> '))

        # Initialize vector solution according to the user
        vectorB[row][0] = float(input(f'Vector_B[{row}] Value --> '))
        print()

    # Return the user linear equation, and matrixL
    return matrix, vectorB, matrixL


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
    determinant_sum = 0

    # Loop to traverse each column of the matrix
    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        # Calling the function recursively to get determinant value of sub matrix obtained
        determinant_sub = determinantMatrix([row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        # Adding the calculated determinant value of particular column matrix to total the determinant_sum
        determinant_sum = determinant_sum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinant_sum


def print_gaussian_elimination(elementaryList, preFinalList, finalList):
    """
    Printing all the LU Gaussian Elimination process

    :param elementaryList: List of NxN matrices
    :param preFinalList: List of NxN matrices
    :param finalList: List of NxN matrices
    """
    for i in range(len(elementaryList)):
        print('\n[Iterator Number --> ' + str(i) + ']')
        for j in range(len(elementaryList[i])):
            if j == 1:
                print(str(elementaryList[i][j]) + ' X ' + str(preFinalList[i][j]) + ' = ' + str(finalList[i][j]))

            else:
                print(str(elementaryList[i][j]) + ' ' + str(preFinalList[i][j]) + '  ' + str(finalList[i][j]))


elementaryMatrixList = []
preFinalMatrixList = []
finalMatrixList = []
gaussianElimination()
