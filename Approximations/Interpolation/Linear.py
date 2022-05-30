# Finding Point Approximation Using Linear Method


def Linear(pointsList, xToFind):
    """
    Method for finding a Point based on the x value

    :param pointsList: List of point represent the points on the graph
    :param xToFind: value on the axis X, that we are searching for
    """
    pass

# Our Program Driver
if __name__ == "__main__":

    # Graph of points (Got to be in rising X)
    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]

    # The X value of the wanted point approximation
    xValue = 2.5

    print('---------- Linear Method ----------')
    Linear(graphPoints, xValue)
