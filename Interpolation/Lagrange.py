# Finding Point Approximation Using Lagrange Method


def lagrange_interpolation_method(points_list, x_to_find):
   
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    y_value = 0

    for i in range(len(points_list)):

        l = 1

        for j in range(len(points_list)):
            if i != j:
                l = l * (x_to_find - points_list[j][0]) / (points_list[i][0] - points_list[j][0])

        y_value = y_value + l * points_list[i][1]

    print(f'Point Approximation --> ({x_to_find}, {int(y_value * 10 ** 5) / 10 ** 5})')


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
   
   
if __name__ == "__main__":
    graph_points = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    x_value = 2.5

    print('---------- Lagrange Method ----------')
    lagrange_interpolation_method(graph_points, x_value)
