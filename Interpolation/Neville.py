# Finding Point Approximation Using Neville Interpolation Method


def neville_interpolation_method(points_list, x_to_find):
    """
    Finding point based on the sent x value using Neville Interpolation Method

    :param points_list: List of points represent the points on the axis
    :param x_to_find: Axis x value that we are searching for
    """
    # if the sent inserted data isn't valid, stop the program
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    # The Y approximation value based on the x value
    y_value = recursive_neville(points_list, x_to_find, 0, len(points_list) - 1)

    # Print the point approximation
    print(f'Point Approximation --> ({x_to_find}, {int(y_value * 10 ** 5) / 10 ** 5})')


def recursive_neville(points_list, x_to_find, i, j):
    """
    Recursive method for finding a Point based on the x value

   :param points_list: List of points represent the points on the axis
    :param x_to_find: Axis x value that we are searching for
    :param i: Index that represent Xi
    :param j: Index that represent Xj
    :return: The approximation of Y based on the X
    """
    # Stop condition
    if i == j:
        return points_list[i][1]

    # Saving the calculation of P[i + 1][j]
    if P[i + 1][j] is None:
        P[i + 1][j] = recursive_neville(points_list, x_to_find, i + 1, j)

    # Saving the calculation of P[i][j - 1]
    if P[i][j - 1] is None:
        P[i][j - 1] = recursive_neville(points_list, x_to_find, i, j - 1)

    # Create a sub calculating for P[i][j]
    return ((x_to_find - points_list[i][0]) * P[i + 1][j] - (x_to_find - points_list[j][0]) * P[i][j - 1]) / (points_list[j][0] - points_list[i][0])


def is_inserted_data_valid(points_list, x_to_find):
    """
    Checking if the inserted points list and search value is valid, and return accordingly

    :param points_list: List of points represent the points on the axis
    :param x_to_find: Axis x value that we are searching for
    :return: True if the sent data valid, else False
    """
    # if there's not enough points
    if len(points_list) < 2:
        print('Error: Interpolation Demand Minimum Of Two Points')
        return False

    # if the request point approximation is out of range for interpolation
    if x_to_find < points_list[0][0] or x_to_find > points_list[-1][0]:
        print('Error: The Requested Point Is Not Suitable For Interpolation Method')
        return False

    # Returning true (inserted data is valid)
    return True


# The Program Driver
if __name__ == "__main__":

    # Input section
    graph_points = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    x_value = 2.5

    # List for saving calculations performed to reduce the complexity of running time (Memoized)
    P = [[None for _ in range(len(graph_points))] for _ in range(len(graph_points))]

    # Running the program
    print('---------- Neville Interpolation Method ----------')
    neville_interpolation_method(graph_points, x_value)
