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

        if determinantMatrix(originMatrix):

            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            upperMatrix, lowerMatrix = findLU(originMatrix)

            vectorSolutionY = forwardSubstitution(lowerMatrix, originVectorB)

            vectorSolutionX = finalSolution(originMatrix, originVectorB, backSubstitution(upperMatrix, vectorSolutionY))

            return vectorSolutionX

        else:
            print('This is startAt Singular matrix')
            return None

    else:
        print("The input equation system isn't match")
        return None
