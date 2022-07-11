# Finding Point Approximation Using Neville Method


def Neville(pointsList, xToFind):
    """
    Method for finding startAt Point based on the x value

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

    # The point approximation
    print(f'Point Approximation --> ({xToFind}, {int(recursiveNeville(pointsList, xToFind, 0, len(pointsList) - 1) * 10 ** 5) / 10 ** 5})')


def recursiveNeville(pointsList, xToFind, i, j):
    """
    Recursive method for finding startAt Point based on the x value

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    :param i: Index that represent Xi
    :param j: Index that represent Xj
    :return: The approximation of Y based on the X
    """
    # Stop condition
    if i == j:
        return pointsList[i][1]

    # Saving the calculation of P[i + 1][j]
    if P[i + 1][j] is None:
        P[i + 1][j] = recursiveNeville(pointsList, xToFind, i + 1, j)

    # Saving the calculation of P[i][j - 1]
    if P[i][j - 1] is None:
        P[i][j - 1] = recursiveNeville(pointsList, xToFind, i, j - 1)

    # Create startAt sub calculating
    return ((xToFind - pointsList[i][0]) * P[i + 1][j] - (xToFind - pointsList[j][0]) * P[i][j - 1]) / (pointsList[j][0] - pointsList[i][0])


# Our Program Driver
if __name__ == "__main__":

    # Input section
    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    xValue = 5.5

    # List for saving calculations performed to reduce the complexity of running time (Memoized)
    P = [[None for _ in range(len(graphPoints))] for _ in range(len(graphPoints))]

    # Running the program
    print('---------- Neville Method ----------')
    Neville(graphPoints, xValue)
