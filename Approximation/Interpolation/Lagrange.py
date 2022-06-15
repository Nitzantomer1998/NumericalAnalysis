def Lagrange(pointsList, xToFind):
    """
    Method for finding a Point based on the x value

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    """
    if len(pointsList) < 2:
        print('Error, Interpolation demand minimum of two points')
        return

    if xToFind < pointsList[0][0] or xToFind > pointsList[-1][0]:
        print('The wanted point is not suitable for interpolation method')
        return

    yToFind = 0

    for i in range(len(pointsList)):

        L = 1

        for j in range(len(pointsList)):

            if i != j:
                L = L * (xToFind - pointsList[j][0]) / (pointsList[i][0] - pointsList[j][0])

        yToFind = yToFind + L * pointsList[i][1]

    print(f'Point Approximation --> ({xToFind}, {int(yToFind * 10 ** 5) / 10 ** 5})')