# Finding Point Approximation Using Linear Interpolation Method


def linear_interpolation_method(points_list, x_to_find):
    """
    Finding point based on the sent x value using Linear Interpolation Method

    :param points_list: List of points represent the points on the axis
    :param x_to_find: Axis x value that we are searching for
    """
    # if the sent inserted data isn't valid, stop the program
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    # Loop to find the nearest points to the requested one
    for i in range(len(points_list) - 1):

        # if we found the needed points
        if points_list[i][0] <= x_to_find <= points_list[i + 1][0]:

            # Calculate the point approximation
            found_y_value = ((x_to_find - points_list[i + 1][0]) * points_list[i][1] + (points_list[i][0] - x_to_find) * points_list[i + 1][1]) / (points_list[i][0] - points_list[i + 1][0])

            # Print the point approximation
            print(f'Point Approximation --> ({x_to_find}, {int(found_y_value * 10 ** 5) / 10 ** 5})')


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
    x_value = 5.5

    # Running the program
    print('---------- Linear Interpolation Method ----------')
    linear_interpolation_method(graph_points, x_value)
