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
