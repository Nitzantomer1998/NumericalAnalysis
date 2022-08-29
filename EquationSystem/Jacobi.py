# Solving Equation System Using Jacobi Method


def jacobi_method(origin_matrix, origin_vector_b):
    """
    Solving equation system in the Jacobi method

    :param origin_matrix: NxN Matrix
    :param origin_vector_b: Nx1 Vector
    """
    # if the input equation system isn't valid, stop the program
    if not is_equation_system_valid(origin_matrix, origin_vector_b):
        return

    # Organize the matrix pivots
    organize_matrix(origin_matrix, origin_vector_b)

    # Lists contain the Previous iteration values, and the Current iteration values
    previous_iteration = [[0 for _ in range(1)] for _ in range(len(origin_matrix))]
    current_iteration = [[0 for _ in range(1)] for _ in range(len(origin_matrix))]

    # Loop for finding the solution
    for _ in range(500):

        # Calculate the next iteration
        for i in range(len(origin_matrix)):

            # Variable to store the sum of the row
            row_sum = 0

            # Calculate the sum of the row i
            for j in range(len(origin_matrix)):
                if i != j:
                    row_sum = row_sum + origin_matrix[i][j] * previous_iteration[j][0]

            # Update the Current iteration value at the index i
            current_iteration[i][0] = (origin_vector_b[i][0] - row_sum) / origin_matrix[i][i]

        # Save the current iteration values into the file
        print_into_file(current_iteration, _ + 1, True)

        # if we found the solution, Stop the loop
        if is_solution_found(current_iteration, previous_iteration):
            break

        # Update the previous solution to be the current solution
        previous_iteration = [[current_iteration[row][0] for _ in range(1)] for row in range(len(current_iteration))]

        # if the equation system isn't converge
        if _ == 499:
            if not is_diagonal_dominant(origin_matrix):
                print_into_file(None, "Error: Matrix Isn't a Diagonal Dominant", False)
                print("Error: Matrix Isn't a Diagonal Dominant")

            print_into_file(None, "Error: Equation System Isn't Converge", False)
            print("Error: Equation System Isn't Converge")
            exit()

    # Saving the equation system final solution
    print_into_file(current_iteration, 'Solution', True)

    # Printing the equation system final solution
    print(f'Equation System Solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, current_iteration))}')


def organize_matrix(origin_matrix, origin_vector_b):
    """
    Organizing the matrix such that the pivot in every row will be the highest one

    :param origin_matrix: NxN matrix
    :param origin_vector_b: Nx1 vector
    """
    # Saving in the file the input equation system
    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Inserted Equation System\n', False)

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
    print_into_file(build_system_equation(origin_matrix, origin_vector_b), 'Updated Equation System', False)


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
        determinant_sub = calculate_determinant([row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

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
    equation_system = [[origin_matrix[row][col] for col in range(len(origin_matrix[0]))] for row in range(len(origin_matrix))]
    [equation_system[row].append(origin_vector_b[row][0]) for row in range(len(origin_vector_b))]

    # Returning the built list
    return equation_system


def is_equation_system_valid(origin_matrix, origin_vector_b):
    """
    Checking if the inserted system equation is valid, and return accordingly

    :param origin_matrix: NxN Matrix
    :param origin_vector_b: Nx1 Vector
    :return: True if the equation system valid, else False
    """
    # if the dimension of the matrix doesn't match to the dimension of the vector, end the program
    if len(origin_matrix) != len(origin_vector_b):
        print_into_file(None, "Error: Input Equation System Isn't Match", False)
        print("Error: Input Equation System Isn't Match")
        return False

    # if the dimension of the matrix isn't a quadratic matrix, end the program
    for i in range(len(origin_matrix)):
        if len(origin_matrix) != len(origin_matrix[i]):
            print_into_file(None, "Error: Input Equation System Isn't Match", False)
            print("Error: Input Equation System Isn't Match")
            return False

    # if the matrix have more or less than one solution, end the program
    if calculate_determinant(origin_matrix) == 0:
        print_into_file(None, 'Error: Matrix Is Singular', False)
        print('Error: Matrix Is Singular')
        return False

    # Returning true (inserted system equation is valid)
    return True


def is_diagonal_dominant(matrix):
    """
    Checking if the sent matrix is diagonal dominant (Pivot of every row is bigger than the sum of the same row)
    and return accordingly

    :return: True if the is diagonal dominant valid, else False
    """
    for i in range(len(matrix)):

        # Variable to store the summation of absolute row[i]
        row_sum = 0

        # calculate the sum of the row i
        for j in range(len(matrix)):
            if i != j:
                row_sum = row_sum + abs(matrix[i][j])

        # If the summation of the row is bigger than the pivot, return False (The matrix is not diagonal dominant)
        if row_sum > abs(matrix[i][i]):
            return False

    # Return true the matrix is Diagonal Dominant
    return True


def is_solution_found(current_iteration, previous_iteration):
    """
    Returning is the system equation solution is with the right accuracy

    :param current_iteration: Nx1 vector represent the current iteration
    :param previous_iteration: Nx1 vector represent the previous iteration
    :return: True if the solution is accurate, else False
    """
    # Getting the maximum accuracy possible for this computer
    computer_accuracy = find_machine_precision()

    # Loop to traverse and check the accuracy of the solution
    for i in range(len(current_iteration)):

        # if the solution isn't accurate return False
        if abs(current_iteration[i][0] - previous_iteration[i][0]) > computer_accuracy:
            return False

    # Return true the solution is accurate
    return True


def print_into_file(data, message, is_vector):
    """
    Printing the content into the calculation file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    :param is_vector: Is_vector is a boolean representing if the data is a vector
    """
    # Open file and save the sent content
    with open('Calculation.txt', 'a+') as file:

        # if we sent a message
        if message:
            file.write('\n{: ^25}'.format(message))
            file.write('\n' if message == 'Updated Equation System' else '')

        # if we sent a data
        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('' if is_vector else '\n')

        # Used to enhance the appearance
        if message == 'Updated Equation System':
            file.write('\n==========================================================================================\n')
            for i in range(len(data) + 1):
                file.write('{: ^25}'.format('Iteration' if i == 0 else chr(64 + i)))


def reset_file():
    """
    Resetting the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------ Jacobi Method ------------------------------')


def find_machine_precision():
    """
    Finding the maximum precision of your machine, and return it

    :return: Your machine precision
    """
    # Variable to store the computer accuracy
    computer_accuracy = 1

    # Loop to find the maximum precision of your machine
    while 1.0 + (computer_accuracy / 2) > 1.0:
        computer_accuracy = computer_accuracy / 2

    # Return computer maximum precision
    return computer_accuracy


# The Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    reset_file()

    # Input section
    input_matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    input_vector_b = [[2], [6], [5]]

    # Running the program
    print('---------- Jacobi Method ----------')
    jacobi_method(input_matrix, input_vector_b)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
