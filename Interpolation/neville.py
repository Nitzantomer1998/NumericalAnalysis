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

    # Number of points in the list
    n = len(points_list)

    # Initialize the list to store the interpolated values
    P = [0] * n

    # Assign the y-values of the points to the first column of P
    for i in range(n):
        P[i] = points_list[i][1]

    # Integer for counting the iterations
    counter = 0

    # Iterate through the number of points
    for k in range(1, n):
        # Iterate through the individual points
        for i in range(n - k):
            counter += 1

            # Use the Neville interpolation formula to calculate the new value of P[i]
            P[i] = ((x_to_find - points_list[i + k][0]) * P[i] - (x_to_find - points_list[i][0]) * P[i + 1]) / (
                    points_list[i][0] - points_list[i + k][0])

            # Save the calculation
            print_into_file([counter, x_to_find, P[i]], None)

    # The Y approximation value based on the x value
    y_value = P[0]

    # Save the point approximation
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
        file.write('------------------------------- Neville Interpolation Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}\n'.format('Iteration', 'X', 'P[I]'))


# The Program Driver
if __name__ == "__main__":
    # Reset the calculation file
    reset_file()
    # Input section
    graph_points = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    x_value = 2.5

    # Running the program
    print('---------- Neville Interpolation Method ----------')
    neville_interpolation_method(graph_points, x_value)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
