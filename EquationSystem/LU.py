# Solving Equation System Using LU Decomposition Method


# Global Variable [Only Used To print the iteration number]
PRINT_COUNTER = 0


def LU(originMatrix, originVectorB):
    """
    Solving equation system in the LU Decomposition method

    :param originMatrix: NxN Matrix
    :param originVectorB: Nx1 Vector
    """
    # Check if the matrix is Quadratic matrix, and check if the vector is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Organize the matrix pivots
            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            # Getting the Lower, and Upper matrices of our equation system
            upperMatrix, lowerMatrix = findLU(originMatrix)

            # Solve Ly = B
            vectorSolutionY = forwardSubstitution(lowerMatrix, originVectorB)

            # Solve Ux = y (Getting the equation system solution)
            vectorSolutionX = finalSolution(originMatrix, originVectorB, backSubstitution(upperMatrix, vectorSolutionY))

            # Saving the equation system final solution
            printIntoFile(vectorSolutionX, 'Equation System Final Solution')
            print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, vectorSolutionX))}')

        # According message In case there is more or less than one solution
        else:
            printIntoFile(None, 'This is a Singular matrix')
            print('This is a Singular matrix')

    # In case the input equation system isn't meet the demands
    else:
        printIntoFile(None, "The input equation system isn't match")
        print("The input equation system isn't match")


def organizeMatrix(originMatrix, originVectorB):
    """
    Taking care that the pivot in the every row will be the highest possible, and return the updated equation system

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :return: The updated equation system
    """
    # Saving the equation system the user gave
    EquationSystem = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [EquationSystem[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(EquationSystem, 'Inserted Equation System')

    # Loop to get the highest pivots possible
    for i in range(len(originMatrix)):

        # Variable to store the highest value for the pivot
        maxPivot = abs(originMatrix[i][i])

        # Variable to store the new pivot row
        pivotRow = -1

        # Searching the highest potential Pivot for originMatrix[i][i]
        for j in range(i + 1, len(originMatrix)):

            # In case there's a higher pivot (on the Column[i])
            if abs(originMatrix[j][i]) > maxPivot:
                maxPivot = abs(originMatrix[j][i])
                pivotRow = j

        # In case there was a higher pivot, change the matrix so the Pivot will be the maximum
        if maxPivot != abs(originMatrix[i][i]):
            originVectorB[i], originVectorB[pivotRow] = originVectorB[pivotRow], originVectorB[i]
            originMatrix[i], originMatrix[pivotRow] = originMatrix[pivotRow], originMatrix[i]

    # Saving the equation system after changing rows/cols
    EquationSystem = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [EquationSystem[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(EquationSystem, 'Updated Equation System')

    # Return the updated equation system
    return originMatrix, originVectorB

def findLU(upperMatrix):
    """
    Solve the matrix into an Upper matrix, and Lower matrix

    :param upperMatrix: NxN matrix of the equation system
    :return: Upper matrix, and Lower matrix
    """
    # Initialize Lower Matrix into an Identity matrix
    lowerMatrix = [[1 if row == col else 0 for col in range(len(upperMatrix))] for row in range(len(upperMatrix))]

    # Solving matrix into an Upper matrix, and Lower matrix
    for i in range(len(upperMatrix)):
        for j in range(i + 1, len(upperMatrix)):
            if upperMatrix[j][i] != 0:
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
    vectorY = [[0 for _ in range(1)] for _ in range(len(lowerMatrix))]

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
    vectorX = [[0 for _ in range(1)] for _ in range(len(upperMatrix))]
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
    Getting the equation system components, check the accuracy of the solution, if the accuracy isn't precise
    calculate the precise solution and return it

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :param vectorSolution: Nx1 vector semi solution (not surly accurate)
    :return: Nx1 vector, the precise equation system solution
    """
    # Solve r = Ax0 - b (Vector r represent the accuracy of the solution we found)
    vectorR = multiplyMatrix(originMatrix, vectorSolution, False)
    for i in range(len(vectorR)):
        vectorR[i][0] = vectorR[i][0] - originVectorB[i][0]

    # In case the equation system solution has round error
    if sum(list(map(sum, vectorR))) != 0:
        printIntoFile(vectorSolution, 'Equation System Solution With Round Error')

    # Update to the correct solution
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
