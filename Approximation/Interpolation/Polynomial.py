def Polynomial(pointsList, xToFind):
    """
    Method for finding approximation of the wanted point

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    """
    if len(pointsList) < 2:
        print('Error, Interpolation demand minimum of two points')
        return

    if xToFind < pointsList[0][0] or xToFind > pointsList[-1][0]:
        print('The wanted point is not suitable for interpolation method')
        return

    matrix = [[pointsList[row][0] ** col for col in range(len(pointsList))] for row in range(len(pointsList))]
    vectorB = [[pointsList[row][1] for _ in range(1)] for row in range(len(pointsList))]

    vectorSolution = LU(matrix, vectorB)

    if any(vectorSolution) is None:
        print('Error, The equation system solver failed')
        return

    yApproximation = 0

    for i in range(len(vectorSolution)):
        yApproximation = yApproximation + vectorSolution[i][0] * (xToFind ** i)

    print(f'Point Approximation --> ({xToFind}, {int(yApproximation * 10 ** 5) / 10 ** 5})')


def LU(originMatrix, originVectorB):
    """
    Solving equation system in the LU Decomposition method

    :param originMatrix: NxN Matrix
    :param originVectorB: Nx1 Vector
    """
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            upperMatrix, lowerMatrix = findLU(originMatrix)

            vectorSolutionY = forwardSubstitution(lowerMatrix, originVectorB)

            vectorSolutionX = finalSolution(originMatrix, originVectorB, backSubstitution(upperMatrix, vectorSolutionY))

            return vectorSolutionX

        else:
            print('This is a Singular matrix')
            return None

    else:
        print("The input equation system isn't match")
        return None


def organizeMatrix(originMatrix, originVectorB):
    """
    Taking care that the pivot in the every row will be the highest possible, and return the updated equation system

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :return: The updated equation system
    """
    for i in range(len(originMatrix)):

        maxPivot = abs(originMatrix[i][i])

        pivotRow = -1

        for j in range(i + 1, len(originMatrix)):

            if abs(originMatrix[j][i]) > maxPivot:
                maxPivot = abs(originMatrix[j][i])
                pivotRow = j

        # In case there was a higher pivot, change the matrix so the Pivot will be the maximum
        if maxPivot != abs(originMatrix[i][i]):
            originVectorB[i], originVectorB[pivotRow] = originVectorB[pivotRow], originVectorB[i]
            originMatrix[i], originMatrix[pivotRow] = originMatrix[pivotRow], originMatrix[i]

    return originMatrix, originVectorB


def findLU(upperMatrix):
    """
    Solve the matrix into an Upper matrix, and Lower matrix

    :param upperMatrix: NxN matrix of the equation system
    :return: Upper matrix, and Lower matrix
    """
    lowerMatrix = [[1 if row == col else 0 for col in range(len(upperMatrix))] for row in range(len(upperMatrix))]

    for i in range(len(upperMatrix)):
        for j in range(i + 1, len(upperMatrix)):
            if upperMatrix[j][i] != 0:
                lowerMatrix[j][i] = upperMatrix[j][i] / upperMatrix[i][i]
                upperMatrix = multiplyMatrix(initElementaryMatrix(len(upperMatrix), j, i, - upperMatrix[j][i] / upperMatrix[i][i]), upperMatrix)

    return upperMatrix, lowerMatrix


def forwardSubstitution(lowerMatrix, vectorB):
    """
    Solve Ly = B, and return the vector y

    :param lowerMatrix: NxN lower matrix
    :param vectorB: Nx1 vector B
    :return: Nx1 vector solution
    """
    vectorY = [[0 for _ in range(1)] for _ in range(len(lowerMatrix))]

    for i in range(len(lowerMatrix)):
        vectorY[i][0] = vectorB[i][0]
        for j in range(i):
            vectorY[i][0] = vectorY[i][0] - lowerMatrix[i][j] * vectorY[j][0]
        vectorY[i][0] = vectorY[i][0] / lowerMatrix[i][i]

    return vectorY


def backSubstitution(upperMatrix, vectorY):
    """
    Solve Ux = y, and return the vectorX

    :param upperMatrix: NxN upper matrix
    :param vectorY: Nx1 vector Y
    :return: Nx1 vector solution
    """
    vectorX = [[0 for _ in range(1)] for _ in range(len(upperMatrix))]
    vectorX[-1][0] = vectorY[-1][0] / upperMatrix[-1][-1]

    for i in range(len(upperMatrix) - 2, -1, -1):
        rowSum = vectorY[i][0]
        for j in range(i + 1, len(upperMatrix)):
            rowSum = rowSum - upperMatrix[i][j] * vectorX[j][0]
        vectorX[i][0] = rowSum / upperMatrix[i][i]

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
    vectorR = multiplyMatrix(originMatrix, vectorSolution)
    for i in range(len(vectorR)):
        vectorR[i][0] = vectorR[i][0] - originVectorB[i][0]

    for i in range(len(vectorSolution)):
        if abs(vectorSolution[i][0] - round(vectorSolution[i][0])) <= max(1e-09 * max(abs(vectorSolution[i][0]), abs(round(vectorSolution[i][0]))), 0):
            vectorSolution[i][0] = round(vectorSolution[i][0])

    return vectorSolution


def multiplyMatrix(matrixA, matrixB):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrixA: NxM Matrix
    :param matrixB: NxM Matrix
    :return: NxM matrix
    """
    matrixC = [[0] * len(matrixB[0]) for _ in range(len(matrixA))]

    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

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
    elementaryMatrix = [[1 if row == col else 0 for col in range(size)] for row in range(size)]
    elementaryMatrix[row][col] = value

    return elementaryMatrix


def determinantMatrix(matrix):
    """
    Calculate the matrix determinant and return the result

    :param matrix: NxN Matrix
    :return: Matrix determinant
    """
    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    determinantSum = 0

    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        determinant_sub = determinantMatrix(
            [row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        determinantSum = determinantSum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinantSum


if __name__ == "__main__":

    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]

    xValue = 2.5

    print('---------- Polynomial Method ----------')
    Polynomial(graphPoints, xValue)
    