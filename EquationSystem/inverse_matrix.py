# Solving Equation System Using Inverse Matrix Method


# Global variable for counting the iteration number in the file
PRINT_COUNTER = 0


def inverse_matrix_method(origin_matrix, origin_vector_b):
    """
    Solving equation system in the Inverse Matrix method

    :param origin_matrix: NxN Matrix
    :param origin_vector_b: Nx1 Vector
    """
    # if the input equation system isn't valid, stop the program
    if not is_equation_system_valid(origin_matrix, origin_vector_b):
        return

    # Organize the matrix pivots
    organize_matrix(origin_matrix, origin_vector_b)

    # Getting the inverse matrix of origin_matrix
    inverse_matrix = find_inverse(origin_matrix)

    # Getting the equation system solution
    semi_solution = multiply_matrices(inverse_matrix, origin_vector_b, False)
    vector_solution = find_final_solution(origin_matrix, origin_vector_b, semi_solution)

    # Saving the equation system final solution
    print_into_file(vector_solution, 'Equation System Final Solution')

    # Printing the equation system final solution
    print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, vector_solution))}')


def organize_matrix(origin_matrix, origin_vector_b):
    """
    Organizing the matrix such that the pivot in every row will be the highest one

    :param origin_matrix: NxN matrix
    :param origin_vector_b: Nx1 vector
    """
    # Saving in the file the input equation system
    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Inserted Equation System\n')

    # Loop to organize the matrix pivots
    for i in range(len(origin_matrix)):

        # Variable to store the highest value for the pivot
        max_pivot = abs(origin_matrix[i][i])

        # Variable to store the new pivot row
        new_pivot_row = -1

        # Searching the highest potential pivot for origin_matrix[i][i]
        for j in range(i + 1, len(origin_matrix)):

            # if there's a higher pivot on the column[i]
            if abs(origin_matrix[j][i]) > max_pivot:
                max_pivot = abs(origin_matrix[j][i])
                new_pivot_row = j

        # if there was a higher pivot, update the matrix so the pivot will be the higher one
        if max_pivot != abs(origin_matrix[i][i]):
            origin_vector_b[i], origin_vector_b[new_pivot_row] = origin_vector_b[new_pivot_row], origin_vector_b[i]
            origin_matrix[i], origin_matrix[new_pivot_row] = origin_matrix[new_pivot_row], origin_matrix[i]

    # Saving in the file the updated equation system
    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Updated Equation System')


def find_inverse(matrix):
    """
    Solving the matrix into an Identity matrix, and return the built inverse matrix

    :param matrix: NxN matrix
    :return: Inverse NxN matrix
    """
    # Initialize inverse_matrix into an Identity matrix
    inverse_matrix = build_elementary_matrix(len(matrix))

    # Solving matrix into an Identity matrix (Lower part), and get alongside the inverse matrix
    for i in range(len(matrix)):

        # if the pivot isn't one
        if matrix[i][i] != 1:
            # Building the elementary matrix in order to affect the inverse matrix
            elementary_matrix = build_elementary_matrix(len(matrix))
            elementary_matrix[i][i] = 1 / matrix[i][i]

            # Update the needed matrices
            inverse_matrix = multiply_matrices(elementary_matrix, inverse_matrix, False)
            matrix = multiply_matrices(elementary_matrix, matrix, True)

        # if the column under the pivot isn't zero
        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                # Building the elementary matrix in order to affect the inverse matrix
                elementary_matrix = build_elementary_matrix(len(matrix))
                elementary_matrix[j][i] = - matrix[j][i]

                # Update the needed matrices
                inverse_matrix = multiply_matrices(elementary_matrix, inverse_matrix, False)
                matrix = multiply_matrices(elementary_matrix, matrix, True)

    # Solving matrix into an Identity matrix (Upper part), and get alongside the inverse matrix
    for i in reversed(range(len(matrix))):

        # if the column above the pivot isn't zero
        for j in reversed(range(i)):
            if matrix[j][i] != 0:
                # Building the elementary matrix in order to affect the inverse matrix
                elementary_matrix = build_elementary_matrix(len(matrix))
                elementary_matrix[j][i] = - matrix[j][i]

                # Update the needed matrices
                inverse_matrix = multiply_matrices(elementary_matrix, inverse_matrix, False)
                matrix = multiply_matrices(elementary_matrix, matrix, True)

    # Return the inverse matrix
    return inverse_matrix


def find_final_solution(origin_matrix, origin_vector_b, vector_solution):
    """
    Getting the equation system components, check the accuracy of the solution, if the accuracy isn't precise enough
    calculate the precise solution and return it

    :param origin_matrix: NxN matrix
    :param origin_vector_b: Nx1 vector
    :param vector_solution: Nx1 vector semi solution (not surly accurate)
    :return: Nx1 vector, the precise Equation System solution
    """
    # Calculating the vector_precision which is the accuracy of the solution for each variable
    vector_precision = multiply_matrices(origin_matrix, vector_solution, False)
    for i in range(len(vector_precision)):
        vector_precision[i][0] = vector_precision[i][0] - origin_vector_b[i][0]

    # if the equation system solution has round error, mention it in the file
    if sum(list(map(sum, vector_precision))) != 0:
        print_into_file(vector_solution, 'Equation System Solution With Round Error')

    # Update to the accurate solution
    for i in range(len(vector_solution)):
        if abs(vector_solution[i][0] - round(vector_solution[i][0])) <= max(
                1e-09 * max(abs(vector_solution[i][0]), abs(round(vector_solution[i][0]))), 0):
            vector_solution[i][0] = round(vector_solution[i][0])

    # Return the final solution of the equation system
    return vector_solution


def calculate_determinant(matrix):
    """
    Calculating the matrix determinant, and return the result

    :param matrix: NxN Matrix
    :return: Matrix determinant value
    """
    # Simple case, The matrix size is 2x2
    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    # Initialize the sum variable
    determinant_sum = 0

    # Loop to traverse each column of the matrix
    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        # Calling the function recursively to get determinant value of sub matrix obtained
        determinant_sub = calculate_determinant(
            [row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        # Adding the calculated determinant value of particular column to the total of determinant_sum
        determinant_sum = determinant_sum + (sign * matrix[0][current_column] * determinant_sub)

    # Returning the final Sum
    return determinant_sum


def build_system_equation(origin_matrix, origin_vector_b):
    """
    Building system equation from the sent matrix and vector, and return it

    :param origin_matrix: NxN matrix
    :param origin_vector_b: Nx1 vector
    :return: (N + 1)xN matrix
    """
    # Creating new double list to build the system equation
    equation_system = [[origin_matrix[row][col] for col in range(len(origin_matrix[0]))] for row in
                       range(len(origin_matrix))]
    [equation_system[row].append(origin_vector_b[row][0]) for row in range(len(origin_vector_b))]

    # Returning the built list
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
    """
    Checking if the inserted system equation is valid, and return accordingly

    :param origin_matrix: NxN Matrix
    :param origin_vector_b: Nx1 Vector
    :return: True if the equation system valid, else False
    """
    # if the dimension of the matrix doesn't match to the dimension of the vector, end the program
    if len(origin_matrix) != len(origin_vector_b):
        print_into_file(None, "Error: Input Equation System Isn't Match")
        print("Error: Input Equation System Isn't Match")
        return False

    # if the dimension of the matrix isn't a quadratic matrix, end the program
    for i in range(len(origin_matrix)):
        if len(origin_matrix) != len(origin_matrix[i]):
            print_into_file(None, "Error: Input Equation System Isn't Match")
            print("Error: Input Equation System Isn't Match")
            return False

    # if the matrix have more or less than one solution, end the program
    if calculate_determinant(origin_matrix) == 0:
        print_into_file(None, 'Error: Matrix Is Singular')
        print('Error: Matrix Is Singular')
        return False

    # Returning true (inserted system equation is valid)
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
            file.write(f'{message} ({PRINT_COUNTER})\n' if PRINT_COUNTER > 0 else f'{message}\n')

        # if we sent a data
        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('\n')
            file.write('\n')

        # Used to enhance the appearance
        if message == 'Updated Equation System' or message == 'After Multiply Matrix':
            file.write('============================================================================================\n')


def reset_file():
    """
    Resetting the calculation file

    """
    with open('..\\Calculation.txt', 'w') as file:
        file.write('------------------------------ Inverse Matrix Method ------------------------------\n')


def multiply_matrices(matrix_a, matrix_b, is_to_save):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrix_a: NxM Matrix
    :param matrix_b: NxM Matrix
    :param is_to_save: Boolean which say if to save the matrices in a file
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zero's
    matrix_c = [[0] * len(matrix_b[0]) for _ in range(len(matrix_a))]

    # Multiply the two matrices and store the outcome in matrix_c
    for i in range(len(matrix_a)):
        for j in range(len(matrix_b[0])):
            for k in range(len(matrix_b)):
                matrix_c[i][j] = matrix_c[i][j] + matrix_a[i][k] * matrix_b[k][j]

    # Saving the matrices in a file
    if is_to_save:
        # Global variable to follow the iteration calculation
        global PRINT_COUNTER
        PRINT_COUNTER += 1

        print_into_file(matrix_a, 'Elementary Matrix')
        print_into_file(matrix_b, 'Pre Multiply Matrix')
        print_into_file(matrix_c, 'After Multiply Matrix')

    # Return the outcome matrix
    return matrix_c


# The Program Driver
if __name__ == "__main__":
    # Reset the calculation file
    reset_file()

    # Input section
    input_matrix = [[2, 2, 2], [2, -1, 1], [-1, -1, 2]]
    input_vector_b = [[4], [-1], [-5]]

    # Running the program
    print('---------- Inverse Matrix Method ----------')
    inverse_matrix_method(input_matrix, input_vector_b)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')