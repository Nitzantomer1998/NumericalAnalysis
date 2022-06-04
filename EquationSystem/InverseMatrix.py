# Solving Equation System Using Inverse Matrix Method


# Global Variable [Only Used To print the iteration number]
PRINT_COUNTER = 0


def InverseMatrix(originMatrix, originVectorB):
    """
    Solving equation system in the Inverse Matrix method

    :param originMatrix: NxN Matrix
    :param originVectorB: Nx1 Vector
    """
    # Check if the matrix is Quadratic matrix, and check if the vector is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Organize the matrix pivots
            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            # Getting the inverse matrix of originMatrix
            inverseMatrix = findInverse(originMatrix)

            # Getting the Equation System solution
            vectorSolution = finalSolution(originMatrix, originVectorB, multiplyMatrix(inverseMatrix, originVectorB, False))

            # Saving the Equation System final solution
            printIntoFile(vectorSolution, 'Equation System Final Solution')
            print(f'Equation System Solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, vectorSolution))}')

        # According message In case there is more or less than one solution
        else:
            printIntoFile(None, 'This is a Singular matrix')
            print('This is a Singular matrix')

    # In case the input Equation System isn't meet the demands
    else:
        printIntoFile(None, "The input Equation System isn't match")
        print("The input Equation System isn't match")


def organizeMatrix(originMatrix, originVectorB):
    """
    Taking care that the pivot in the every row will be the highest possible, and return the updated Equation System

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :return: The updated Equation System
    """
    # Saving the Equation System the user gave
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

    # Saving the Equation System after changing rows/cols
    EquationSystem = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [EquationSystem[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(EquationSystem, 'Updated Equation System')

    # Return the updated Equation System
    return originMatrix, originVectorB


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
            if matrix[j][i] != 0.0:
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
    Getting the Equation System components, check the accuracy of the solution, if the accuracy isn't precise
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

    # In case the Equation System solution has round error
    if sum(list(map(sum, vectorR))) != 0.0:
        printIntoFile(vectorSolution, 'Linear Equation Solution With Round Error')

    # Update to the accurate solution
    for i in range(len(vectorSolution)):
        if abs(vectorSolution[i][0] - round(vectorSolution[i][0])) <= max(1e-09 * max(abs(vectorSolution[i][0]), abs(round(vectorSolution[i][0]))), 0.0):
            vectorSolution[i][0] = round(vectorSolution[i][0])

    # Return the final solution of the Equation System
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
    matrixC = [[0.0] * len(matrixB[0]) for _ in range(len(matrixA))]

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
