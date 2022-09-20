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


# Our Program Driver
if __name__ == "__main__":

    # Input section
    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    xValue = 5.5

    # Running the program
    print('---------- Lagrange Method ----------')
    Lagrange(graphPoints, xValue)
