# Solving Equation System Using Gauss Seidel Method


# Global Variable To Store The Machine Precision, (Set the accuracy of the solution)
ACCURACY = 1


def gauss_seidel_method(origin_matrix, origin_vector_b):
    if not is_equation_system_valid(origin_matrix, origin_vector_b):
        return

    organize_matrix(origin_matrix, origin_vector_b)

    find_machine_precision()

    previous_iteration = [[0 for _ in range(1)] for _ in range(len(origin_matrix))]
    current_iteration = [[0 for _ in range(1)] for _ in range(len(origin_matrix))]

    for _ in range(500):

        for i in range(len(origin_matrix)):

            row_sum = 0

            for j in range(len(origin_matrix)):
                if i != j:
                    row_sum = row_sum + origin_matrix[i][j] * current_iteration[j][0]

            current_iteration[i][0] = (origin_vector_b[i][0] - row_sum) / origin_matrix[i][i]

        print_into_file(current_iteration, _ + 1, True)

        if is_solution_found(current_iteration, previous_iteration):
            break

        previous_iteration = [[current_iteration[row][0] for _ in range(1)] for row in range(len(current_iteration))]

        if _ == 499:
            if not is_diagonal_dominant(origin_matrix):
                print_into_file(None, "Error: Matrix Isn't a Diagonal Dominant", False)
                print("Error: Matrix Isn't a Diagonal Dominant")

            print_into_file(None, "Error: Equation System Isn't Converge", False)
            print("Error: Equation System Isn't Converge")
            exit()

    print_into_file(current_iteration, 'Solution', True)

    print(f'Equation System Solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, current_iteration))}')


def organize_matrix(origin_matrix, origin_vector_b):
    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Inserted Equation System\n', False)

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

    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Updated Equation System', False)


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


def is_equation_system_valid(origin_matrix, origin_vector_b):
    if len(origin_matrix) != len(origin_vector_b):
        print_into_file(None, "Error: Input Equation System Isn't Match", False)
        print("Error: Input Equation System Isn't Match")
        return False

    for i in range(len(origin_matrix)):
        if len(origin_matrix) != len(origin_matrix[i]):
            print_into_file(None, "Error: Input Equation System Isn't Match", False)
            print("Error: Input Equation System Isn't Match")
            return False

    if calculate_determinant(origin_matrix) == 0:
        print_into_file(None, 'Error: Matrix Is Singular', False)
        print('Error: Matrix Is Singular')
        return False

    return True


def is_diagonal_dominant(matrix):
    for i in range(len(matrix)):

        row_sum = 0

        for j in range(len(matrix)):
            if i != j:
                row_sum = row_sum + abs(matrix[i][j])

        if row_sum > abs(matrix[i][i]):
            return False

    return True


def is_solution_found(current_iteration, previous_iteration):
    for i in range(len(current_iteration)):

        if abs(current_iteration[i][0] - previous_iteration[i][0]) > ACCURACY:
            return False

    return True


def print_into_file(data, message, is_vector):
    with open('Calculation.txt', 'a+') as file:

        if message:
            file.write('\n{: ^25}'.format(message))
            file.write('' if message != 'Updated Equation System' else '\n')

        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('' if is_vector else '\n')

        if message == 'Updated Equation System':
            file.write('\n==========================================================================================\n')
            for i in range(len(data) + 1):
                file.write('{: ^25}'.format('Iteration' if i == 0 else chr(64 + i)))
                
                
def machinePrecision():
    """
    Function to find your Machine Precision, And set the accuracy of the solution

    """
    # Our global variable to store the accuracy of the solution
    global ACCURACY

    # Update the accuracy to be the maximum possible for your machine
    while 1.0 + (ACCURACY / 2) > 1.0:
        ACCURACY = ACCURACY / 2


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------ Gauss Seidel Method ------------------------------')


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Input section
    inputMatrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    inputVectorB = [[2], [6], [5]]

    # Running the program
    print('---------- Gauss Seidel Method ----------')
    GaussSeidel(inputMatrix, inputVectorB)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
