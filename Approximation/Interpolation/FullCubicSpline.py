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