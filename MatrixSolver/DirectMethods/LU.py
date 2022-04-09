# Solving Linear Equation In The LU Decomposition Method


# Global Variable [Only Used To print the iteration number]
MATRIX_COUNT = -2


def printIntoFile(data, message, isTrue=True):
    """
    Printing the data and the message content into a specified file

    :param data: Data is a list representing matrix or vector
    :param message: Message is a String representing the data explanation
    :param isTrue: If True, The Linear Equation is valid, else False
    """
    # Our Global Variable To Count The Iteration Number
    global MATRIX_COUNT

    # In Case We Are Running A New Linear Equation Calculation, It will erase the lase one
    if MATRIX_COUNT == -2:
        file = open('LU_Calculation.txt', 'w')
        file.close()

    # Open the file and save the data
    with open('LU_Calculation.txt', 'a+') as file:

        # In case the Linear Equation is valid
        if isTrue:

            # In case we are printing new calculation
            if MATRIX_COUNT % 3 == 0:
                file.write('==========================================================================================')

            # Saving the Linear Equation input, and the updated one
            if MATRIX_COUNT < 0:
                file.write(str(message) + '\n')
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        objectData = '{: ^22}'.format(data[i][j])
                        file.write(objectData)
                    file.write('\n')
                file.write('\n')

            # Saving the calculation of the Linear Equation
            elif MATRIX_COUNT > -1:
                file.write('\n' + str(message) + ' [' + str(MATRIX_COUNT // 3 + 1) + ']\n')
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        objectData = '{: ^22}'.format(data[i][j])
                        file.write(objectData)
                    file.write('\n')

        # In case Linear Equation is not valid
        else:
            file.write('\n' + str(message) + '\n')

        # Increase Our Global Iteration Counter Variable
        MATRIX_COUNT = MATRIX_COUNT + 1


def LU_DecompositionMethod():
    """
    Solving linear equation in the LU Decomposition method

    """
    # Initialize the matrix, and vectorB
    originMatrix, originVectorB = initMatrix()

    # Check if the matrix is Quadratic matrix, and check if the vector is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Organize the matrix pivots
            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            # Getting the Lower, and Upper matrices of our Linear Equation
            upperMatrix, lowerMatrix = findLU(originMatrix)

            # Solve Ly = B
            vectorSolutionY = forwardSubstitution(lowerMatrix, originVectorB)

            # Solve Ux = y (Getting the Linear Equation solution)
            vectorSolutionX = finalSolution(originMatrix, originVectorB, backSubstitution(upperMatrix, vectorSolutionY))

            # Saving the Linear Equation final solution
            printIntoFile(vectorSolutionX, 'Linear Equation Final Solution')

        # According message In case there is more or less than one solution
        else:
            printIntoFile(None, 'This Is A Singular Matrix', False)

    # In case the input Linear Equation isn't meet the demands
    else:
        printIntoFile(None, "The Input Linear Equation Isn't Match", False)


def organizeMatrix(originMatrix, originVectorB):
    """
    Taking care that the pivot in the every row will be the highest possible, and return the updated Linear Equation

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :return: The updated Linear Equation
    """
    # Saving the Linear Equation the user gave
    LinearEquation = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [LinearEquation[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(LinearEquation, '[User Input Linear Equation]')

    # Iteration variable
    i = 0
    while i < len(originMatrix):
        # Variable to store the highest value for the pivot
        maxPivot = abs(originMatrix[i][i])

        # Variable to store the new pivot row
        pivotRow = 0

        # Variable to store the new pivot column
        pivotCol = 0

        # Searching for the highest Pivot in originMatrix[i][i]
        for j in range(i + 1, len(originMatrix)):

            # In case there's a higher pivot (on the Column[i])
            if abs(originMatrix[j][i]) > maxPivot:
                # Store the new highest pivot, and his row
                maxPivot = abs(originMatrix[j][i])
                pivotRow = j
                pivotCol = 0

            # In case there's a higher pivot (on the Row[i])
            if abs(originMatrix[i][j]) > maxPivot:
                # Store the new highest pivot, and his column
                maxPivot = abs(originMatrix[i][j])
                pivotCol = j
                pivotRow = 0

        # In case there was a higher pivot, change the matrix so the Pivot will be the maximum
        if maxPivot != abs(originMatrix[i][i]):

            # In case the highest pivot is on the Rows
            if pivotRow > pivotCol:
                # Changed the Matrix and the vector Rows
                originVectorB[i], originVectorB[pivotRow] = originVectorB[pivotRow], originVectorB[i]
                originMatrix[i], originMatrix[pivotRow] = originMatrix[pivotRow], originMatrix[i]

            # In case the highest pivot is on the Columns
            else:
                # Changed the Matrix Columns
                for i in range(len(originMatrix)):
                    originMatrix[i][i], originMatrix[i][pivotCol] = originMatrix[i][pivotCol], originMatrix[i][i]

                # In case changing Columns made a higher pivot on row
                i = i - 1

        # Next iteration
        i = i + 1

        # Saving the Linear Equation after changing
        LinearEquation = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
        [LinearEquation[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
        printIntoFile(LinearEquation, '[Updated Linear Equation]')

    # Return the updated Linear Equation
    return originMatrix, originVectorB


def findLU(upperMatrix):
    """
    Solve the matrix into an Upper matrix, and Lower matrix

    :param upperMatrix: NxN matrix of the Linear Equation
    :return: Upper matrix, and Lower matrix
    """
    # Initialize Lower Matrix into an Identity matrix
    lowerMatrix = [[1.0 if row == col else 0.0 for col in range(len(upperMatrix))] for row in range(len(upperMatrix))]

    # Solving matrix into an Upper matrix, and Lower matrix
    for i in range(len(upperMatrix)):
        for j in range(i + 1, len(upperMatrix)):
            if upperMatrix[j][i] != 0.0:
                # Multiply into an Upper matrix, and updating the Lower matrix
                lowerMatrix[j][i] = upperMatrix[j][i] / upperMatrix[i][i]
                upperMatrix = multiplyMatrix(initElementaryMatrix(len(upperMatrix), j, i, - upperMatrix[j][i] / upperMatrix[i][i]), upperMatrix, True)

    # Return Upper matrix, and Lower matrix
    return upperMatrix, lowerMatrix


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


def finalSolution(originMatrix, originVectorB, vectorSolution):
    """
    Getting the Linear equation components, check the accuracy of the solution, if the accuracy isn't precise
    calculate the precise solution and return it

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :param vectorSolution: Nx1 vector semi solution (not surly accurate)
    :return: Nx1 vector, the precise Linear Equation solution
    """
    # Solve r = Ax0 - b
    # Vector r represent the accuracy of the solution we found
    vectorR = multiplyMatrix(originMatrix, vectorSolution, False)
    for i in range(len(vectorR)):
        vectorR[i][0] = vectorR[i][0] - originVectorB[i][0]

    # In case the Linear Equation solution, has round error
    if sum(list(map(sum, vectorR))) != 0.0:
        printIntoFile(vectorSolution, 'Linear Equation Solution With Round Error')

    # Update to the correct solution
    for i in range(len(vectorSolution)):
        # In case of round error
        if abs(vectorSolution[i][0] - round(vectorSolution[i][0])) <= max(1e-09 * max(abs(vectorSolution[i][0]), abs(round(vectorSolution[i][0]))), 0.0):
            vectorSolution[i][0] = round(vectorSolution[i][0])

    # Return the final solution of the Linear Equation
    return vectorSolution


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
        printIntoFile(matrixA, 'Elementary Matrix')
        printIntoFile(matrixB, 'Pre Multiply Matrix')
        printIntoFile(matrixC, 'After Multiply Matrix')

    # Return the outcome matrix
    return matrixC


def initMatrix():
    """
    Initialize user Linear Equations, and return them

    :return: NxN matrix, and Nx1 vector B
    """
    # Initialize Linear Equation from the user
    matrix = [[2, 2, 2], [2, -1, 1], [-1, -1, 2]]
    vectorB = [[4], [-1], [-5]]

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
        determinant_sub = determinantMatrix(
            [row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        # Adding the calculated determinant value of particular column matrix to total the determinantSum
        determinantSum = determinantSum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinantSum


LU_DecompositionMethod()
