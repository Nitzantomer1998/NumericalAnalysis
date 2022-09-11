# Finding Point Approximation Using Linear Interpolation Method


def linear_interpolation_method(points_list, x_to_find):
    
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    for i in range(len(points_list) - 1):

        if points_list[i][0] <= x_to_find <= points_list[i + 1][0]:

            found_y_value = ((x_to_find - points_list[i + 1][0]) * points_list[i][1] + (points_list[i][0] - x_to_find) * points_list[i + 1][1]) / (points_list[i][0] - points_list[i + 1][0])

            print(f'Point Approximation --> ({x_to_find}, {int(found_y_value * 10 ** 5) / 10 ** 5})')

            
def is_inserted_data_valid(points_list, x_to_find):
    
    if len(points_list) < 2:
        print('Error: Interpolation Demand Minimum Of Two Points')
        return False

    if x_to_find < points_list[0][0] or x_to_find > points_list[-1][0]:
        print('Error: The Requested Point Is Not Suitable For Interpolation Method')
        return False

    return True


if __name__ == "__main__":

    graph_points = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    x_value = 5.5

    print('---------- Linear Interpolation Method ----------')
    linear_interpolation_method(graph_points, x_value)

