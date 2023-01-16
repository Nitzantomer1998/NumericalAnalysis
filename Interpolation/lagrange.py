# Finding Point Approximation Using Lagrange Interpolation Method


def lagrange_interpolation_method(points_list, x_to_find):
    """
    Finding point based on the sent x value using Lagrange Interpolation Method

    :param points_list: List of points represent the points on the axis
    :param x_to_find: Axis x value that we are searching for
    """
    # if the sent inserted data isn't valid, stop the program
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    # The Y approximation value based on the x value
    y_value = 0

    # The accurate rate of Y approximation
    y_accurate = 0

    # Loop for calculating the Y approximation value
    for i in range(len(points_list)):

        # Calculate Li(x)
        l = 1

        # Inner loop to calculate the Li(x) result
        for j in range(len(points_list)):
            if i != j:
                l = l * (x_to_find - points_list[j][0]) / (points_list[i][0] - points_list[j][0])

        # Calculate the approximation of Y in the current I iteration
        y_value = y_value + l * points_list[i][1]

        # Calculate the accurate rate of Y approximation
        y_accurate = y_accurate + l

        # Save the calculation
        print_into_file([i + 1, x_to_find, y_value, y_accurate], None)

    # Save the calculation
    print_into_file(None, f'Point Approximation --> ({x_to_find}, {int(y_value * 10 ** 5) / 10 ** 5})')

    # Print the point approximation
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


def print_into_file(data, message):
    """
    Printing the content into the calculation file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    """
    # Open file and save the sent content
    with open('..\\Calculation.txt', 'a+') as file:

        # if we sent a message
        if message:
            file.write('\n{: ^25}\n'.format(message))
            file.write('--------------------------------------------------------------------------------------------\n')

        # if we sent a data
        if data:
            for i in range(len(data)):
                file.write('{: ^25}'.format(float(data[i])))
            file.write('\n')


def reset_file():
    """
    Resetting the calculation file

    """
    with open('..\\Calculation.txt', 'w') as file:
        file.write('------------------------------- Lagrange Interpolation Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}{: ^25}\n'.format('Iteration', 'X', 'Y', 'Y Accurate Rate'))


# The Program Driver
if __name__ == "__main__":
    # Reset the calculation file
    reset_file()

    # Input section
    graph_points = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    x_value = 2.5

    # Running the program
    print('---------- Lagrange Interpolation Method ----------')
    lagrange_interpolation_method(graph_points, x_value)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
