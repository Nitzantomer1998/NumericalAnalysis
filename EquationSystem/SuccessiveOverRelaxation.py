# Solving Equation System Using Successive Over Relaxation Method


# Global Variable To Store The Machine Precision, (Set the accuracy of the solution)
ACCURACY = 1


def successive_over_relaxation_method(origin_matrix, origin_vector_b, w):
    
    if not is_equation_system_valid(origin_matrix, origin_vector_b, w):
        return

    organize_matrix(origin_matrix, origin_vector_b)

    previous_iteration = [[0 for _ in range(1)] for _ in range(len(origin_matrix))]
    current_iteration = [[0 for _ in range(1)] for _ in range(len(origin_matrix))]

    for _ in range(500):

        for i in range(len(origin_matrix)):

            row_sum = 0

            for j in range(len(origin_matrix)):
                if i != j:
                    row_sum = row_sum + origin_matrix[i][j] * current_iteration[j][0]

            current_iteration[i][0] = (1 - w) * previous_iteration[i][0] + w * (origin_vector_b[i][0] - row_sum) / origin_matrix[i][i]

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

    print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, current_iteration))}')


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


def is_equation_system_valid(origin_matrix, origin_vector_b, w):
    
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

    if w <= 0 or w >= 2:
        print_into_file(None, 'Error: Omega Parameter Is Out Of Boundaries', False)
        print('Error: Omega Parameter Is Out Of Boundaries')
        return False

    return True


def isDiagonalDominant(matrix):
    """
    Check if the pivot in every row is bigger than the sum of the whole row (without the pivot),
    If yes return True, else False

    """
    for i in range(len(matrix)):

        # Variable to store, the summation of absolute row [i]
        rowSum = 0
        for j in range(len(matrix)):
            if i != j:
                rowSum = rowSum + abs(matrix[i][j])

        # If the summation of the row is bigger than the pivot, return False (The matrix is not diagonal dominant)
        if rowSum > abs(matrix[i][i]):
            return False

    # The matrix is Diagonal Dominant
    return True


def machinePrecision():
    """
    Function to find your Machine Precision, And set the accuracy of the solution

    """
    # Our global variable to store the accuracy of the solution
    global ACCURACY

    # Update the accuracy to be the maximum possible for your machine
    while 1.0 + (ACCURACY / 2) > 1.0:
        ACCURACY = ACCURACY / 2


def printIntoFile(data, message, isVector):
    """
    Printing the content into a specified file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    :param isVector: isVector is a boolean representing if the data is a vector
    """
    # Open file and save the sent content
    with open('Calculation.txt', 'a+') as file:

        # In case we sent a message
        if message:
            file.write('\n{: ^25}'.format(message))
            file.write('' if message != 'Updated Equation System' else '\n')

        # In case we sent a data
        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('' if isVector else '\n')

        # Used to enhance the appearance
        if message == 'Updated Equation System':
            file.write('\n==========================================================================================\n')
            for i in range(len(data) + 1):
                file.write('{: ^25}'.format('Iteration' if i == 0 else chr(64 + i)))


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------ Successive Over Relaxation Method ------------------------------')


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Input section
    inputMatrix = [[4, 3, 0], [3, 4, -1], [0, -1, 4]]
    inputVectorB = [[24], [30], [-24]]
    Omega = 1.2

    # Running the program
    print('---------- Successive Over Relaxation Method ----------')
    SuccessiveOverRelaxation(inputMatrix, inputVectorB, Omega)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
