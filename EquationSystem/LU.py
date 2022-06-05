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
