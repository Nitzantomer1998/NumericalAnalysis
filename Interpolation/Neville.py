def Neville(pointsList, xToFind):
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

    print(f'Point Approximation --> ({xToFind}, {int(recursiveNeville(pointsList, xToFind, 0, len(pointsList) - 1) * 10 ** 5) / 10 ** 5})')