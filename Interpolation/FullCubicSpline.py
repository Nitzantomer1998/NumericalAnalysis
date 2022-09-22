# Finding Point Approximation Using Full Cubic Spline Interpolation Method


def full_cubic_spline_interpolation(points_list, x_to_find, derivative_values):
   
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    h, lam, u, d = build_data_table(points_list, derivative_values)

    for i in range(len(points_list) - 1):

        if points_list[i][0] <= x_to_find <= points_list[i + 1][0]:

            built_matrix = [[0 for _ in range(len(points_list))] for _ in range(len(points_list))]
            built_vector = [[d[row] for _ in range(1)] for row in range(len(points_list))]

            for j in range(len(points_list) - 1):
                for k in range(len(points_list) - 1):
                    if j == k:
                        built_matrix[j][j] = 2
                        built_matrix[j + 1][k] = u[j + 1]
                        built_matrix[j][k + 1] = lam[j]

            built_matrix[-1][-1] = 2

            vector_solution = lower_upper_decomposition_method(built_matrix, built_vector)

            if any(vector_solution) is None:
                print('Error: Equation System Failed To Find A Solution')
                return

            y_value = ((points_list[i + 1][0] - x_to_find) ** 3 * vector_solution[i][0] + (x_to_find - points_list[i][0]) ** 3 * vector_solution[i + 1][0]) / (6 * h[i]) + ((points_list[i + 1][0] - x_to_find) * points_list[i][1] + (x_to_find - points_list[i][0]) * points_list[i + 1][1]) / h[i] - (((points_list[i + 1][0] - x_to_find) * vector_solution[i][0] + (x_to_find - points_list[i][0]) * vector_solution[i + 1][0]) * h[i]) / 6

            print(f'Point Approximation --> ({x_to_find}, {int(y_value * 10 ** 5) / 10 ** 5})')

            
def lower_upper_decomposition_method(origin_matrix, origin_vector_b):
    
    if not is_equation_system_valid(origin_matrix, origin_vector_b):
        return None

    organize_matrix(origin_matrix, origin_vector_b)

    upper_matrix, lower_matrix = find_lower_upper(origin_matrix)

    lower_vector_solution = forward_substitution(lower_matrix, origin_vector_b)

    vector_solution = back_substitution(upper_matrix, lower_vector_solution)
    final_vector_solution = find_final_solution(origin_matrix, origin_vector_b, vector_solution)

    return final_vector_solution


def organize_matrix(origin_matrix, origin_vector_b):
    
    for i in range(len(origin_matrix)):

        max_pivot = abs(origin_matrix[i][i])

        new_pivot_row = -1

        for j in range(i + 1, len(origin_matrix)):

            if abs(origin_matrix[j][i]) > max_pivot:
                max_pivot = abs(origin_matrix[j][i])
                new_pivot_row = j

        if max_pivot != abs(origin_matrix[i][i]):
            origin_vector_b[i], origin_vector_b[new_pivot_row] = origin_vector_b[new_pivot_row], origin_vector_b[i]
            origin_matrix[i], origin_matrix[new_pivot_row] = origin_matrix[new_pivot_row], origin_matrix[i]

def find_lower_upper(upper_matrix):
    
    lower_matrix = [[1.0 if row == col else 0 for col in range(len(upper_matrix))] for row in range(len(upper_matrix))]

    for i in range(len(upper_matrix)):
        for j in range(i + 1, len(upper_matrix)):
            if upper_matrix[j][i] != 0:
                lower_matrix[j][i] = upper_matrix[j][i] / upper_matrix[i][i]

                elementary_matrix = build_elementary_matrix(len(upper_matrix))
                elementary_matrix[j][i] = - upper_matrix[j][i] / upper_matrix[i][i]

                upper_matrix = multiply_matrices(elementary_matrix, upper_matrix)

    return upper_matrix, lower_matrix


def forward_substitution(lower_matrix, vector_b):
    
    vector_y = [[0 for _ in range(1)] for _ in range(len(lower_matrix))]

    for i in range(len(lower_matrix)):
        vector_y[i][0] = vector_b[i][0]
        for j in range(i):
            vector_y[i][0] = vector_y[i][0] - lower_matrix[i][j] * vector_y[j][0]
        vector_y[i][0] = vector_y[i][0] / lower_matrix[i][i]

    return vector_y
   

def back_substitution(upper_matrix, vector_y):
    
    vector_x = [[0 for _ in range(1)] for _ in range(len(upper_matrix))]
    vector_x[-1][0] = vector_y[-1][0] / upper_matrix[-1][-1]

    for i in range(len(upper_matrix) - 2, -1, -1):
        row_sum = vector_y[i][0]
        for j in range(i + 1, len(upper_matrix)):
            row_sum = row_sum - upper_matrix[i][j] * vector_x[j][0]
        vector_x[i][0] = row_sum / upper_matrix[i][i]

    return vector_x

   
def finalSolution(originMatrix, originVectorB, vectorSolution):
    """
    Getting the equation system components, check the accuracy of the solution, if the accuracy isn't precise
    calculate the precise solution and return it

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :param vectorSolution: Nx1 vector semi solution (not surly accurate)
    :return: Nx1 vector, the precise Equation System solution
    """
    # Solve r = Ax0 - b (Vector r represent the accuracy of the solution we found)
    vectorR = multiplyMatrix(originMatrix, vectorSolution)
    for i in range(len(vectorR)):
        vectorR[i][0] = vectorR[i][0] - originVectorB[i][0]

    # Update to the accurate solution
    for i in range(len(vectorSolution)):
        if abs(vectorSolution[i][0] - round(vectorSolution[i][0])) <= max(
                1e-09 * max(abs(vectorSolution[i][0]), abs(round(vectorSolution[i][0]))), 0):
            vectorSolution[i][0] = round(vectorSolution[i][0])

    # Return the final solution of the equation system
    return vectorSolution


def multiplyMatrix(matrixA, matrixB):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrixA: NxM Matrix
    :param matrixB: NxM Matrix
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zero's
    matrixC = [[0] * len(matrixB[0]) for _ in range(len(matrixA))]

    # Multiply the two matrices and store the outcome in matrixC
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    # Return the outcome matrix
    return matrixC


def initElementaryMatrix(size, row, col, value):
    """
    Initialize elementary matrix, from identity matrix, and a specific value, and return it

    :param size: Matrix size
    :param row: Row index
    :param col: Column index
    :param value: Value parameter
    :return: Return the elementary matrix
    """
    # Initialize the desire elementary matrix
    elementaryMatrix = [[1 if row == col else 0 for col in range(size)] for row in range(size)]
    elementaryMatrix[row][col] = value

    # Return the elementary matrix
    return elementaryMatrix


def determinantMatrix(matrix):
    """
    Calculate the matrix determinant and return the result

    :param matrix: NxN Matrix
    :return: Matrix determinant
    """
    # Simple case, The matrix size is 2x2
    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    # Initialize our sum variable
    determinantSum = 0

    # Loop to traverse each column of the matrix
    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        # Calling the function recursively to get determinant value of sub matrix obtained
        determinant_sub = determinantMatrix(
            [row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        # Adding the calculated determinant value of particular column matrix to total the determinantSum
        determinantSum = determinantSum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinantSum


# Our Program Driver
if __name__ == "__main__":

    # Input section
    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    derivativeLeft = 0
    derivativeRight = 1
    xValue = 2.5

    # Running the program
    print('---------- Full Cubic Spline Method ----------')
    FullCubicSpline(graphPoints, xValue, derivativeLeft, derivativeRight)
