# Finding Point Approximation Using Lagrange Method


def Lagrange(pointsList, xToFind):
    """
    Method for finding a Point based on the x value

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

    # The Y approximation of the point x
    yToFind = 0

    # Loop to find Y approximation
    for i in range(len(pointsList)):

        # Calculate Li(x)
        L = 1

        # Loop to calculate the Li(x) result
        for j in range(len(pointsList)):

            if i != j:
                L = L * (xToFind - pointsList[j][0]) / (pointsList[i][0] - pointsList[j][0])

        # Calculate the approximation of Y in the current I iteration
        yToFind = yToFind + L * pointsList[i][1]

    # The point approximation
    print(f'Point Approximation --> ({xToFind}, {int(yToFind * 10 ** 5) / 10 ** 5})')


# Our Program Driver
if __name__ == "__main__":

    # Input section
    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    xValue = 2.5

    # Running the program
    print('---------- Lagrange Method ----------')
    Lagrange(graphPoints, xValue)
