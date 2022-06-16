def Neville(pointsList, xToFind):
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

    print(f'Point Approximation --> ({xToFind}, {int(recursiveNeville(pointsList, xToFind, 0, len(pointsList) - 1) * 10 ** 5) / 10 ** 5})')


def recursiveNeville(pointsList, xToFind, i, j):
    """
    Recursive method for finding a Point based on the x value

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    :param i: Index that represent Xi
    :param j: Index that represent Xj
    :return: The approximation of Y based on the X
    """
    if i == j:
        return pointsList[i][1]

    if P[i + 1][j] is None:
        P[i + 1][j] = recursiveNeville(pointsList, xToFind, i + 1, j)

    if P[i][j - 1] is None:
        P[i][j - 1] = recursiveNeville(pointsList, xToFind, i, j - 1)

    return ((xToFind - pointsList[i][0]) * P[i + 1][j] - (xToFind - pointsList[j][0]) * P[i][j - 1]) / (
                pointsList[j][0] - pointsList[i][0])


if __name__ == "__main__":
    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    xValue = 2.5

    P = [[None for _ in range(len(graphPoints))] for _ in range(len(graphPoints))]

    print('---------- Neville Method ----------')
    Neville(graphPoints, xValue)