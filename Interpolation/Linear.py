def LinearInterpolation(pointsList, xToFind):
    """
    Interpolation for finding startAt Point based on the x value

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    """
    if len(pointsList) < 2:
        print('Error, Interpolation demand minimum of two points')
        return

    if xToFind < pointsList[0][0] or xToFind > pointsList[-1][0]:
        print('The wanted point is not suitable for interpolation method')
        return

    for i in range(len(pointsList) - 1):

        if pointsList[i][0] <= xToFind <= pointsList[i + 1][0]:

            print(f'Point Approximation --> ({xToFind}, {int(((xToFind - pointsList[i + 1][0]) * pointsList[i][1] + (pointsList[i][0] - xToFind) * pointsList[i + 1][1]) / (pointsList[i][0] - pointsList[i + 1][0]) * 10 ** 5) / 10 ** 5})')


if __name__ == "__main__":

    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    xValue = 5.5

    print('---------- Linear Method ----------')
    LinearInterpolation(graphPoints, xValue)