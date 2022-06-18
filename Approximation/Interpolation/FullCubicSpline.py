def FullCubicSpline(pointsList, xToFind, leftDerivative, rightDerivative):
    """
    Method for finding a Point based on the x value

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    :param leftDerivative: Left domain segment derivative
    :param rightDerivative: Right domain segment derivative
    """
    if len(pointsList) < 4:
        print('Error, Cubic Interpolation demand minimum of four points')
        return

    if xToFind < pointsList[0][0] or xToFind > pointsList[-1][0]:
        print('The wanted point is not suitable for interpolation method')
        return

    h = [pointsList[1][0] - pointsList[0][0]]
    lam = [1]
    u = [0]
    d = [6 / h[0] * ((pointsList[1][1] - pointsList[0][1]) / h[0] - leftDerivative)]

    for i in range(1, len(pointsList) - 1):

        h.append(pointsList[i + 1][0] - pointsList[i][0])
        lam.append(h[i] / (h[i - 1] + h[i]))
        u.append(1 - lam[i])
        d.append(6 / (h[i - 1] + h[i]) * ((pointsList[i + 1][1] - pointsList[i][1]) / h[i] - (pointsList[i][1] - pointsList[i - 1][1]) / h[i - 1]))

    h.append(0)
    lam.append(0)
    u.append(1)
    d.append(6 / h[-2] * (rightDerivative - (pointsList[-1][1] - pointsList[-2][1]) / h[0]))

    for i in range(len(pointsList) - 1):

        if pointsList[i][0] <= xToFind <= pointsList[i + 1][0]:

            finalMatrix = [[0 for _ in range(len(pointsList))] for _ in range(len(pointsList))]
            finalVector = [[d[row] for _ in range(1)] for row in range(len(pointsList))]

            for j in range(len(pointsList) - 1):
                for k in range(len(pointsList) - 1):
                    if j == k:
                        finalMatrix[j][j] = 2
                        finalMatrix[j + 1][k] = u[j + 1]
                        finalMatrix[j][k + 1] = lam[j]
            finalMatrix[-1][-1] = 2

            vectorSolution = InverseMatrix(finalMatrix, finalVector)

            s = ((pointsList[i + 1][0] - xToFind) ** 3 * vectorSolution[i][0] + (xToFind - pointsList[i][0]) ** 3 * vectorSolution[i + 1][0]) / (6 * h[i]) + ((pointsList[i + 1][0] - xToFind) * pointsList[i][1] + (xToFind - pointsList[i][0]) * pointsList[i + 1][1]) / h[i] - (((pointsList[i + 1][0] - xToFind) * vectorSolution[i][0] + (xToFind - pointsList[i][0]) * vectorSolution[i + 1][0]) * h[i]) / 6
            print(f'Point Approximation --> ({xToFind}, {int(s * 10 ** 5) / 10 ** 5})')
            return


def InverseMatrix(originMatrix, originVectorB):
    """
    Solving equation system in the Inverse Matrix method

    :param originMatrix: NxN Matrix
    :param originVectorB: Nx1 Vector
    """
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(
            originVectorB[0]) == 1:

        if determinantMatrix(originMatrix):

            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            inverseMatrix = findInverse(originMatrix)

            vectorSolution = finalSolution(originMatrix, originVectorB, multiplyMatrix(inverseMatrix, originVectorB))

            return vectorSolution

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

        if maxPivot != abs(originMatrix[i][i]):
            originVectorB[i], originVectorB[pivotRow] = originVectorB[pivotRow], originVectorB[i]
            originMatrix[i], originMatrix[pivotRow] = originMatrix[pivotRow], originMatrix[i]

    return originMatrix, originVectorB


def findInverse(matrix):
    """
    Solve the matrix into an Identity matrix, and return the inverse matrix

    :param matrix: NxN matrix
    :return: Inverse NxN matrix
    """
    inverseMatrix = [[1 if row == col else 0 for col in range(len(matrix))] for row in range(len(matrix))]

    for i in range(len(matrix)):

        if matrix[i][i] != 1:
            inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), i, i, 1 / matrix[i][i]), inverseMatrix)
            matrix = multiplyMatrix(initElementaryMatrix(len(matrix), i, i, 1 / matrix[i][i]), matrix)

        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix)

    for i in reversed(range(len(matrix))):

        for j in reversed(range(i)):
            if matrix[j][i] != 0:
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix)

    return inverseMatrix
