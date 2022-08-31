# Solving Equation System Using LU Decomposition Method


# Global Variable [Only Used To print the iteration number]
PRINT_COUNTER = 0


def lower_upper_decomposition_method(origin_matrix, origin_vector_b):

    if not is_equation_system_valid(origin_matrix, origin_vector_b):
        return

    organize_matrix(origin_matrix, origin_vector_b)

    upper_matrix, lower_matrix = find_lower_upper(origin_matrix)

    lower_vector_solution = forward_substitution(lower_matrix, origin_vector_b)

    vector_solution = back_substitution(upper_matrix, lower_vector_solution)
    final_vector_solution = find_final_solution(origin_matrix, origin_vector_b, vector_solution)

    print_into_file(final_vector_solution, 'Equation System Final Solution')

    print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, final_vector_solution))}')


def organize_matrix(origin_matrix, origin_vector_b):

    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Inserted Equation System\n')

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

    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Updated Equation System')



def find_lower_upper(upper_matrix):
    
    lower_matrix = [[1.0 if row == col else 0 for col in range(len(upper_matrix))] for row in range(len(upper_matrix))]

    for i in range(len(upper_matrix)):
        for j in range(i + 1, len(upper_matrix)):
            if upper_matrix[j][i] != 0:
                lower_matrix[j][i] = upper_matrix[j][i] / upper_matrix[i][i]

                elementary_matrix = build_elementary_matrix(len(upper_matrix))
                elementary_matrix[j][i] = - upper_matrix[j][i] / upper_matrix[i][i]

                upper_matrix = multiply_matrices(elementary_matrix, upper_matrix, True)

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


def find_final_solution(origin_matrix, origin_vector_b, vector_solution):
    
    vector_precision = multiply_matrices(origin_matrix, vector_solution, False)
    for i in range(len(vector_precision)):
        vector_precision[i][0] = vector_precision[i][0] - origin_vector_b[i][0]

    if sum(list(map(sum, vector_precision))) != 0:
        print_into_file(vector_solution, 'Equation System Solution With Round Error')

    for i in range(len(vector_solution)):
        if abs(vector_solution[i][0] - round(vector_solution[i][0])) <= max(
                1e-09 * max(abs(vector_solution[i][0]), abs(round(vector_solution[i][0]))), 0):
            vector_solution[i][0] = round(vector_solution[i][0])

    return vector_solution


def calculate_determinant(matrix):
    
    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    determinant_sum = 0

    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        determinant_sub = calculate_determinant([row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        determinant_sum = determinant_sum + (sign * matrix[0][current_column] * determinant_sub)

    return determinant_sum


def build_system_equation(origin_matrix, origin_vector_b):
    
    equation_system = [[origin_matrix[row][col] for col in range(len(origin_matrix[0]))] for row in range(len(origin_matrix))]
    [equation_system[row].append(origin_vector_b[row][0]) for row in range(len(origin_vector_b))]

    return equation_system


def build_elementary_matrix(size):
    
    elementary_matrix = [[1.0 if row == col else 0.0 for col in range(size)] for row in range(size)]

    return elementary_matrix


def multiplyMatrix(matrixA, matrixB, isTrue):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrixA: NxM Matrix
    :param matrixB: NxM Matrix
    :param isTrue: Boolean which say if to save the matrices in a file
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zero's
    matrixC = [[0] * len(matrixB[0]) for _ in range(len(matrixA))]

    # Multiply the two matrices and store the outcome in matrixC
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    # Saving the matrices in a file
    if isTrue:

        # Global variable to follow the iteration calculation
        global PRINT_COUNTER
        PRINT_COUNTER = PRINT_COUNTER + 1

        printIntoFile(matrixA, 'Elementary Matrix')
        printIntoFile(matrixB, 'Pre Multiply Matrix')
        printIntoFile(matrixC, 'After Multiply Matrix')

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


def printIntoFile(data, message):
    """
    Printing the content into a specified file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    """
    # Open file and save the sent content
    with open('Calculation.txt', 'a+') as file:

        # In case we sent a message
        if message:
            file.write(f'{message} ({PRINT_COUNTER})\n' if PRINT_COUNTER > 0 else f'{message}\n')

        # In case we sent a data
        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('\n')
            file.write('\n')

        # Used to enhance the appearance
        if message == 'Updated Equation System' or message == 'After Multiply Matrix':
            file.write('============================================================================================\n')


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------ LU Method ------------------------------\n')


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Input section
    inputMatrix = [[2, 2, 2], [2, -1, 1], [-1, -1, 2]]
    inputVectorB = [[4], [-1], [-5]]

    # Running the program
    print('---------- LU Method ----------')
    LU(inputMatrix, inputVectorB)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')