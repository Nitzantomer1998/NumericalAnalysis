# Finding Point Approximation Using Linear Interpolation Method


def LinearInterpolation(pointsList, xToFind):
    """
    Interpolation for finding a Point based on the x value

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    """
    # In case we can't perform interpolation
    if len(pointsList) < 2:
        print('Error, Interpolation demand minimum of two points')
        return

    # In case we can't perform interpolation
    if xToFind < pointsList[0][0] or xToFind > pointsList[-1][0]:
        print('The wanted point is not suitable for interpolation method')
        return

    # Loop to find the nearest points to the wanted one
    for i in range(len(pointsList) - 1):

        # In case the needed action is interpolation
        if pointsList[i][0] <= xToFind <= pointsList[i + 1][0]:

            # Print the point approximation
            print(f'Point Approximation --> ({xToFind}, {int(((xToFind - pointsList[i + 1][0]) * pointsList[i][1] + (pointsList[i][0] - xToFind) * pointsList[i + 1][1]) / (pointsList[i][0] - pointsList[i + 1][0]) * 10 ** 5) / 10 ** 5})')


# Our Program Driver
if __name__ == "__main__":

    # Input section
    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    xValue = 2.5

    # Running the program
    print('---------- Linear Method ----------')
    LinearInterpolation(graphPoints, xValue)
