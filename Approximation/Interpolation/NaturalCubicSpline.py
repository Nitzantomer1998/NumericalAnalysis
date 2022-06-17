def NaturalCubicSpline(pointsList, xToFind):
    """
    Method for finding a Point based on the x value

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    """
    if len(pointsList) < 4:
        print('Error, Cubic Interpolation demand minimum of four points')
        return

    if xToFind < pointsList[0][0] or xToFind > pointsList[-1][0]:
        print('The wanted point is not suitable for interpolation method')
        return

    h = [pointsList[1][0] - pointsList[0][0]]
    lam = [0]
    u = [0]
    d = [0]

    for i in range(1, len(pointsList) - 1):

        h.append(pointsList[i + 1][0] - pointsList[i][0])
        lam.append(h[i] / (h[i - 1] + h[i]))
        d.append((6 / (h[i - 1] + h[i])) * ((pointsList[i + 1][1] - pointsList[i][1]) / h[i] - (pointsList[i][1] - pointsList[i - 1][1]) / h[i - 1]))
        u.append(1 - lam[i])

    h.append(0)
    lam.append(0)
    u.append(0)
    d.append(0)

    for i in range(len(pointsList) - 1):

        if pointsList[i][0] <= xToFind <= pointsList[i + 1][0]:

            finalMatrix = [[0 for _ in range(len(pointsList) - 2)] for _ in range(len(pointsList) - 2)]
            finalVector = [[d[row + 1] for _ in range(1)] for row in range(len(pointsList) - 2)]

            for j in range(len(pointsList) - 3):
                for k in range(len(pointsList) - 3):
                    if j == k:
                        finalMatrix[j][j] = 2
                        finalMatrix[j + 1][k] = u[j + 2]
                        finalMatrix[j][k + 1] = lam[j + 1]
            finalMatrix[-1][-1] = 2

            equationSolution = InverseMatrix(finalMatrix, finalVector)

            vectorSolution = [[0] for _ in range(len(pointsList))]
            for j in range(1, len(pointsList) - 1):
                vectorSolution[j] = equationSolution[j - 1]

            s = ((pointsList[i + 1][0] - xToFind) ** 3 * vectorSolution[i][0] + (xToFind - pointsList[i][0]) ** 3 * vectorSolution[i + 1][0]) / (6 * h[i]) + ((pointsList[i + 1][0] - xToFind) * pointsList[i][1] + (xToFind - pointsList[i][0]) * pointsList[i + 1][1]) / h[i] - (((pointsList[i + 1][0] - xToFind) * vectorSolution[i][0] + (xToFind - pointsList[i][0]) * vectorSolution[i + 1][0]) * h[i]) / 6
            print(f'Point Approximation --> ({xToFind}, {int(s * 10 ** 5) / 10 ** 5})')
            return
