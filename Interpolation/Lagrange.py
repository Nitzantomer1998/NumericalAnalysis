def Lagrange(pointsList, xToFind):
    """
    Method for finding startAt Point based on the x value

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

    # The point approximation
    print(f'Point Approximation --> ({xToFind}, {int(yToFind * 10 ** 5) / 10 ** 5})')


if __name__ == "__main__":

    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    xValue = 5.5

    print('---------- Lagrange Method ----------')
    Lagrange(graphPoints, xValue)
