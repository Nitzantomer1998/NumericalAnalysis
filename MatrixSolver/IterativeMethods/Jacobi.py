# Solving Linear Equation In The Jacobi Method


# Global Variable [Only Used To print the iteration number]
MATRIX_COUNT = -2

# Global Variable To Store The Computer Epsilon Machine
EPSILON = 1


def printIntoFile(data, message, isTrue=True):
    """
    Printing the data and the message content into a specified file

    :param data: Data is a list representing matrix or vector
    :param message: Message is a String representing the data explanation
    :param isTrue: If True, The Linear Equation is valid, else False
    """
    # Our Global Variable To Count The Iteration Number
    global MATRIX_COUNT

    # In Case We Are Running A New Linear Equation Calculation, It will erase the lase one
    if MATRIX_COUNT == -2:
        file = open('Jacobi_Calculation.txt', 'w')
        file.close()

    # Open the file and save the data
    with open('Jacobi_Calculation.txt', 'a+') as file:

        # In case the Linear Equation is valid
        if isTrue:

            # In case we are printing new calculation
            if MATRIX_COUNT % 3 == 0:
                file.write('==========================================================================================')

            # Saving the Linear Equation input, and the updated one
            if MATRIX_COUNT < 0:
                file.write(str(message) + '\n')
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        objectData = '{: ^22}'.format(data[i][j])
                        file.write(objectData)
                    file.write('\n')
                file.write('\n')

            # Saving the calculation of the Linear Equation
            elif MATRIX_COUNT > -1:
                file.write('\n' + str(message) + ' [' + str(MATRIX_COUNT // 3 + 1) + ']\n')
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        objectData = '{: ^22}'.format(data[i][j])
                        file.write(objectData)
                    file.write('\n')

        # In case Linear Equation is not valid
        else:
            file.write('\n' + str(message) + '\n')

        # Increase Our Global Iteration Counter Variable
        MATRIX_COUNT = MATRIX_COUNT + 1


def JacobiMethod():
    """
    Solving Linear Equation in the Jacobi method

    """
    # Initialize the matrix, and vectorB
    originMatrix, originVectorB = initMatrix()

    # Check if the matrix is Quadratic matrix, and check if the vector is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Organize the matrix pivots
            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            # Check if the Linear Equation is Diagonal Dominant
            if isDiagonalDominant(originMatrix):

                # Get the computer Epsilon machine
                epsilonMachine()

                # Our lists for the Prev iteration values, and our Current iteration values
                prevIteration = [[0], [0], [0]]
                currentIteration = [[0], [0], [0]]

                # The iteration loop to find the Linear Equation solution
                while True:
                    # Calculate the next guess
                    for i in range(len(originMatrix)):
                        rowSum = 0
                        for j in range(len(originMatrix)):
                            if i != j:
                                rowSum = rowSum + originMatrix[i][j] * prevIteration[j][0]
                        currentIteration[i][0] = (originVectorB[i][0] - rowSum) / originMatrix[i][i]

                    flag = True
                    for i in range(len(originMatrix)):
                        if currentIteration[i][0] - prevIteration[i][0] > EPSILON:
                            flag = False

                    # In case we found our solution, Stop the loop
                    if flag:
                        break

                    # Save the current iteration values into the file, and update the current solution to be the prev
                    printIntoFile(currentIteration, 'Linear Equation Final Solution')
                    prevIteration = [[currentIteration[row][0] for col in range(len(currentIteration[0]))] for row in range(len(currentIteration))]

                # Saving the Linear Equation final solution
                printIntoFile(currentIteration, 'Linear Equation Final Solution')

            # According message In case there is no Dominant Diagonal
            else:
                printIntoFile(None, 'This Is A Not Diagonal Dominant Matrix', False)

        # According message In case there is more or less than one solution
        else:
            printIntoFile(None, 'This Is A Singular Matrix', False)

    # In case the input Linear Equation isn't meet the demands
    else:
        printIntoFile(None, "The Input Linear Equation Isn't Match", False)


def organizeMatrix(originMatrix, originVectorB):
    """
    Taking care that the pivot in the every row will be the highest possible, and return the updated Linear Equation

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :return: The updated Linear Equation
    """
    # Saving the Linear Equation the user gave
    LinearEquation = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [LinearEquation[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(LinearEquation, '[User Input Linear Equation]')

    # Iteration Variable
    i = 0
    while i < len(originMatrix):
        # Variable to store the highest value for the pivot
        maxPivot = abs(originMatrix[i][i])

        # Variable to store the new pivot row
        pivotRow = 0

        # Variable to store the new pivot column
        pivotCol = 0

        # Searching for the highest Pivot in originMatrix[i][i]
        for j in range(i + 1, len(originMatrix)):

            # In case there's a higher pivot (on the Column[i])
            if abs(originMatrix[j][i]) > maxPivot:
                # Store the new highest pivot, and his row
                maxPivot = abs(originMatrix[j][i])
                pivotRow = j
                pivotCol = 0

            # In case there's a higher pivot (on the Row[i])
            if abs(originMatrix[i][j]) > maxPivot:
                # Store the new highest pivot, and his column
                maxPivot = abs(originMatrix[i][j])
                pivotCol = j
                pivotRow = 0

        # In case there was a higher pivot, change the matrix so the Pivot will be the maximum
        if maxPivot != abs(originMatrix[i][i]):

            # In case the highest pivot is on the Rows
            if pivotRow > pivotCol:
                # Changed the Matrix and the vector Rows
                originVectorB[i], originVectorB[pivotRow] = originVectorB[pivotRow], originVectorB[i]
                originMatrix[i], originMatrix[pivotRow] = originMatrix[pivotRow], originMatrix[i]

            # In case the highest pivot is on the Columns
            else:
                # Changed the Matrix Columns
                for i in range(len(originMatrix)):
                    originMatrix[i][i], originMatrix[i][pivotCol] = originMatrix[i][pivotCol], originMatrix[i][i]

                # In case changing Columns made a higher pivot on row
                i = i - 1

        # Next iteration
        i = i + 1

    # Saving the Linear Equation after changing
    LinearEquation = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [LinearEquation[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(LinearEquation, '[Updated Linear Equation]')

    # Return the updated Linear Equation
    return originMatrix, originVectorB


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

    # The matrix is Diagonal Dominant)
    return True


def initMatrix():
    """
    Initialize user Linear Equations, and return them

    :return: NxN matrix, and Nx1 vector B
    """
    # Initialize Linear Equation from the user
    matrix = [[3, -1, 1], [0, 1, -1], [1, 1, -2]]
    vectorB = [[4], [-1], [-3]]

    # Return the user linear equation
    return matrix, vectorB


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


def epsilonMachine():
    """
    Function To Find Your Machine Precision

    """
    global EPSILON
    EPSILON = 1
    while 1.0 + (EPSILON / 2) > 1.0:
        EPSILON = EPSILON / 2


JacobiMethod()
