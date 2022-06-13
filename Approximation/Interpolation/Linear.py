def LinearInterpolation(pointsList, xToFind):
    """
    Interpolation for finding a Point based on the x value

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

        # In case the needed action is interpolation
        if pointsList[i][0] <= xToFind <= pointsList[i + 1][0]:

            # Print the point approximation
            print(f'Point Approximation --> ({xToFind}, {((xToFind - pointsList[i + 1][0]) * pointsList[i][1] + (pointsList[i][0] - xToFind) * pointsList[i + 1][1]) / (pointsList[i][0] - pointsList[i + 1][0])})')
