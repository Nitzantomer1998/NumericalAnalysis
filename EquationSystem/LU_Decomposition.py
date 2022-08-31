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
        file.write('------------------------------ LU Method ------------------------------\n')
        
        
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


if __name__ == "__main__":

    reset_file()

    input_matrix = [[2, 2, 2], [2, -1, 1], [-1, -1, 2]]
    input_vector_b = [[4], [-1], [-5]]

    print('---------- LU Method ----------')
    lower_upper_decomposition_method(input_matrix, input_vector_b)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
