# Solving Linear Equation In The Gauss Seidel Method


# Global Variable [Only Used To print the iteration number]
PRINT_COUNTER = -2

# Global Variable To Store The Computer Epsilon Machine
EPSILON = 1


def printIntoFile(data, message, isTrue, isFinal):
    """
    Printing the data and the message content into a specified file

    :param data: Data is a list representing matrix or vector
    :param message: Message is a String representing the data explanation
    :param isTrue: If True, The Linear Equation is valid, else False
    :param isFinal: If True, We Print the Linear Equation Solution
    """

    # Our Global Variable To Count The Iteration Number
    global PRINT_COUNTER

    # In Case We Are Running A New Linear Equation Calculation, It will create a new file with the method name
    if PRINT_COUNTER == -2:
        file = open('GS_Calculation.txt', 'w')
        file.write('------------------------------ Gauss Seidel Method ------------------------------\n')
        file.close()

    # Open the file and save the data
    with open('GS_Calculation.txt', 'a+') as file:

        # In case the Linear Equation is valid
        if isTrue:

            # Saving the Linear Equation input, and the updated one
            if PRINT_COUNTER < 0:
                file.write(str(message) + '\n')
                for i in range(len(data)):
                    for j in range(len(data[0])):
                        objectData = '{: ^22}'.format(data[i][j])
                        file.write(objectData)
                    file.write('\n')
                file.write('\n')

            # In case we are printing new calculation
            if PRINT_COUNTER == 0:
                file.write('========================================================================================\n')
                for i in range(len(data) + 1):
                    objectData = '{: ^22}'.format('Iteration' if i == 0 else chr(64 + i))
                    file.write(objectData)
                file.write('\n')

            # Saving the calculation of the Linear Equation
            if PRINT_COUNTER > -1:
                objectData = '{: ^22}'.format(str('Solution' if isFinal else (PRINT_COUNTER + 1)))
                file.write(objectData)
                for i in range(len(data)):
                    objectData = '{: ^22}'.format(data[i][0])
                    file.write(objectData)
                file.write('\n')

        # In case Linear Equation is not valid
        else:
            file.write('\n' + str(message) + '\n')

        # Increase Our Global Iteration Counter Variable
        PRINT_COUNTER = PRINT_COUNTER + 1


def GaussSeidelMethod():
    """
    Solving Linear Equation in the Gauss Seidel method

    """
    # Initialize the matrix, and vectorB
    originMatrix, originVectorB = initMatrix()

    # Check if the matrix is Quadratic matrix, and check if the vector is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Organize the matrix pivots
            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            # Getting Your Epsilon Machine
            epsilonMachine()

            # Store if the Linear Equation is Diagonal Dominant
            isConvergent = isDiagonalDominant(originMatrix)

            # According message in case the Matrix is Not Diagonal Dominant
            if isConvergent is False:
                printIntoFile(None, 'This Is A Not Diagonal Dominant Matrix', False, False)

            # Our lists for the Prev iteration values, and our Current iteration values
            prevIteration = [[0 for _ in range(1)] for _ in range(len(originMatrix))]
            currentIteration = [[0 for _ in range(1)] for _ in range(len(originMatrix))]

            # The iteration loop to find the Linear Equation solution
            Counter = 0

            while True:
                if isConvergent is False and Counter > 500:
                    printIntoFile(None, 'The Matrix Is Not Convergent', False, False)
                    break

                # Calculate the next guess
                for i in range(len(originMatrix)):
                    rowSum = 0
                    for j in range(len(originMatrix)):
                        if i != j:
                            rowSum = rowSum + originMatrix[i][j] * currentIteration[j][0]
                    currentIteration[i][0] = (originVectorB[i][0] - rowSum) / originMatrix[i][i]

                # Save the current iteration values into the file
                printIntoFile(currentIteration, None, True, False)

                # Check if we arrive to the solution, In case we found our solution, Stop the program
                if all([False if abs(currentIteration[row][0] - prevIteration[row][0]) > EPSILON else True for row in range(len(currentIteration))]):
                    break

                # Update the current solution to be the prev
                prevIteration = [[currentIteration[row][0] for _ in range(1)] for row in range(len(currentIteration))]

                # Stop Condition In case of Not Dominant Diagonal
                Counter = Counter + 1

            # Saving the Linear Equation final solution
            printIntoFile(currentIteration, None, True, True)

        # According message In case there is more or less than one solution
        else:
            printIntoFile(None, 'This Is A Singular Matrix', False, False)

    # In case the input Linear Equation isn't meet the demands
    else:
        printIntoFile(None, "The Input Linear Equation Isn't Match", False, False)


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
    printIntoFile(LinearEquation, '[User Input Linear Equation]', True, False)

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
                for k in range(len(originMatrix)):
                    originMatrix[k][i], originMatrix[k][pivotCol] = originMatrix[k][pivotCol], originMatrix[k][i]

                # In case changing Columns made a higher pivot on row
                i = i - 1

        # Next iteration
        i = i + 1

    # Saving the Linear Equation after changing
    LinearEquation = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [LinearEquation[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(LinearEquation, '[Updated Linear Equation]', True, False)

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

    # The matrix is Diagonal Dominant
    return True


def initMatrix():
    """
    Initialize user Linear Equations, and return them

    :return: NxN matrix, and Nx1 vector B
    """
    # Initialize Linear Equation from the user
    matrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    vectorB = [[2], [6], [5]]

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


GaussSeidelMethod()
print('Calculation Is Done, Check File "GS_Calculation" For The Process')
