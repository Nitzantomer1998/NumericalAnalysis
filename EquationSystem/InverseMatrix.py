# Solving Equation System Using Inverse Matrix Method


# Global Variable [Only Used To print the iteration number]
PRINT_COUNTER = 0


def inverse_matrix_method(origin_matrix, origin_vector_b):
    if not is_equation_system_valid(origin_matrix, origin_vector_b):
        return

    organize_matrix(origin_matrix, origin_vector_b)

    inverse_matrix = find_inverse(origin_matrix)

    semi_solution = multiply_matrices(inverse_matrix, origin_vector_b, False)
    vector_solution = find_final_solution(origin_matrix, origin_vector_b, semi_solution)

    print_into_file(vector_solution, 'Equation System Final Solution')

    print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, vector_solution))}')


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


def find_inverse(matrix):
    
    inverse_matrix = build_elementary_matrix(len(matrix))

    for i in range(len(matrix)):

        if matrix[i][i] != 1:

            elementary_matrix = build_elementary_matrix(len(matrix))
            elementary_matrix[i][i] = 1 / matrix[i][i]

            inverse_matrix = multiply_matrices(elementary_matrix, inverse_matrix, False)
            matrix = multiply_matrices(elementary_matrix, matrix, True)

        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:

                elementary_matrix = build_elementary_matrix(len(matrix))
                elementary_matrix[j][i] = - matrix[j][i]

                inverse_matrix = multiply_matrices(elementary_matrix, inverse_matrix, False)
                matrix = multiply_matrices(elementary_matrix, matrix, True)

    for i in reversed(range(len(matrix))):

        for j in reversed(range(i)):
            if matrix[j][i] != 0:

                elementary_matrix = build_elementary_matrix(len(matrix))
                elementary_matrix[j][i] = - matrix[j][i]

                inverse_matrix = multiply_matrices(elementary_matrix, inverse_matrix, False)
                matrix = multiply_matrices(elementary_matrix, matrix, True)

    return inverse_matrix


def find_final_solution(origin_matrix, origin_vector_b, vector_solution):

    vector_precision = multiply_matrices(origin_matrix, vector_solution, False)
    for i in range(len(vector_precision)):
        vector_precision[i][0] = vector_precision[i][0] - origin_vector_b[i][0]

    if sum(list(map(sum, vector_precision))) != 0:
        print_into_file(vector_solution, 'Equation System Solution With Round Error')

    for i in range(len(vector_solution)):
        if abs(vector_solution[i][0] - round(vector_solution[i][0])) <= max(1e-09 * max(abs(vector_solution[i][0]), abs(round(vector_solution[i][0]))), 0):
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
    """
    Initialize elementary matrix, and return it

    :param size: Matrix size
    :return: The elementary matrix
    """
    # Initialize thh elementary matrix
    elementary_matrix = [[1.0 if row == col else 0.0 for col in range(size)] for row in range(size)]

    # Return the elementary matrix
    return elementary_matrix


def is_equation_system_valid(origin_matrix, origin_vector_b):
    
    if len(origin_matrix) != len(origin_vector_b):
        print_into_file(None, "Error: Input Equation System Isn't Match")
        print("Error: Input Equation System Isn't Match")
        return False

    for i in range(len(origin_matrix)):
        if len(origin_matrix) != len(origin_matrix[i]):
            print_into_file(None, "Error: Input Equation System Isn't Match")
            print("Error: Input Equation System Isn't Match")
            return False

    if calculate_determinant(origin_matrix) == 0:
        print_into_file(None, 'Error: Matrix Is Singular')
        print('Error: Matrix Is Singular')
        return False

    return True


def print_into_file(data, message):
    
    with open('Calculation.txt', 'a+') as file:

        if message:
            file.write(f'{message} ({PRINT_COUNTER})\n' if PRINT_COUNTER > 0 else f'{message}\n')

        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('\n')
            file.write('\n')

        if message == 'Updated Equation System' or message == 'After Multiply Matrix':
            file.write('============================================================================================\n')


def reset_file():
    
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------ Inverse Matrix Method ------------------------------\n')


def multiply_matrices(matrix_a, matrix_b, is_to_save):
    
    matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                matrix_c[i][j] = matrix_c[i][j] + matrix_a[i][k] * matrix_b[k][j]

    if is_to_save:

        global PRINT_COUNTER
        PRINT_COUNTER = PRINT_COUNTER + 1

        print_into_file(matrix_a, 'Elementary Matrix')
        print_into_file(matrix_b, 'Pre Multiply Matrix')
        print_into_file(matrix_c, 'After Multiply Matrix')

    return matrix_c    


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Input section
    inputMatrix = [[2, 2, 2], [2, -1, 1], [-1, -1, 2]]
    inputVectorB = [[4], [-1], [-5]]

    # Running the program
    print('---------- Inverse Matrix Method ----------')
    InverseMatrix(inputMatrix, inputVectorB)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
