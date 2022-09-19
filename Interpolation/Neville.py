# Finding Point Approximation Using Neville Method


def neville_interpolation_method(points_list, x_to_find):
    
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    y_value = recursive_neville(points_list, x_to_find, 0, len(points_list) - 1)

    print(f'Point Approximation --> ({x_to_find}, {int(y_value * 10 ** 5) / 10 ** 5})')


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
