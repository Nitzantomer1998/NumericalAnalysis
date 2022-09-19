# Finding Point Approximation Using Neville Method


def neville_interpolation_method(points_list, x_to_find):
    
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    y_value = recursive_neville(points_list, x_to_find, 0, len(points_list) - 1)

    print(f'Point Approximation --> ({x_to_find}, {int(y_value * 10 ** 5) / 10 ** 5})')


def recursive_neville(points_list, x_to_find, i, j):
    
    if i == j:
        return points_list[i][1]

    if P[i + 1][j] is None:
        P[i + 1][j] = recursive_neville(points_list, x_to_find, i + 1, j)

    if P[i][j - 1] is None:
        P[i][j - 1] = recursive_neville(points_list, x_to_find, i, j - 1)

    return ((x_to_find - points_list[i][0]) * P[i + 1][j] - (x_to_find - points_list[j][0]) * P[i][j - 1]) / (points_list[j][0] - points_list[i][0])


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
    x_value = 2.5

    P = [[None for _ in range(len(graph_points))] for _ in range(len(graph_points))]

    print('---------- Neville Interpolation Method ----------')
    neville_interpolation_method(graph_points, x_value)
