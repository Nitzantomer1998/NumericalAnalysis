# Solving Linear Equation Using Jacobi Method


# Global Variable To Store The Machine Precision, (Set the accuracy of the solution)
ACCURACY = 1


def Jacobi(originMatrix, originVectorB):
    """
    Solving Linear Equation using Jacobi method

    :param originMatrix: NxN Matrix
    :param originVectorB: Nx1 Vector
    """
    # Check if the matrix is Quadratic matrix, and check if the vector is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Organize the matrix pivots
            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            # Getting your Machine Precision
            machinePrecision()

            # Our lists for the Prev iteration values, and our Current iteration values
            prevIteration = [[0 for _ in range(1)] for _ in range(len(originMatrix))]
            currentIteration = [[0 for _ in range(1)] for _ in range(len(originMatrix))]

            # Loop for finding the solution
            for _ in range(500):

                # Calculate the next guess
                for i in range(len(originMatrix)):
                    rowSum = 0
                    for j in range(len(originMatrix)):
                        if i != j:
                            rowSum = rowSum + originMatrix[i][j] * prevIteration[j][0]
                    currentIteration[i][0] = (originVectorB[i][0] - rowSum) / originMatrix[i][i]

                # Save the current iteration values into the file
                printIntoFile(currentIteration, _ + 1, True)

                # In case we found the solution, Stop the program
                if all([False if abs(currentIteration[row][0] - prevIteration[row][0]) > ACCURACY else True for row in range(len(currentIteration))]):
                    break

                # Update the previous solution to be the current solution
                prevIteration = [[currentIteration[row][0] for _ in range(1)] for row in range(len(currentIteration))]

                # According message in case the Matrix is not converge
                if _ == 499:
                    if not isDiagonalDominant(originMatrix):
                        printIntoFile(None, "This isn't a Diagonal Dominant matrix", False)
                        print("This isn't a Diagonal Dominant matrix")

                    printIntoFile(None, "This Linear Equation isn't Converge", False)
                    print("This Linear Equation isn't Converge")
                    exit()

            # Saving the Linear Equation final solution
            printIntoFile(currentIteration, 'Solution', True)
            print(str(list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, currentIteration))))

        # According message In case there is more or less than one solution
        else:
            printIntoFile('This is a Singular matrix', True, False)
            print('This is a Singular matrix')

    # In case the input Linear Equation isn't meet the demands
    else:
        printIntoFile(None, "The input Linear Equation isn't match", False)
        print("The input Linear Equation isn't match")


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
    printIntoFile(LinearEquation, 'Inserted Linear Equation\n', False)

    # Loop to get the highest pivots possible
    for i in range(len(originMatrix)):

        # Variable to store the highest value for the pivot
        maxPivot = abs(originMatrix[i][i])

        # Variable to store the new pivot row
        pivotRow = -1

        # Searching the highest potential Pivot for originMatrix[i][i]
        for j in range(i + 1, len(originMatrix)):

            # In case there's a higher pivot (on the Column[i])
            if abs(originMatrix[j][i]) > maxPivot:
                maxPivot = abs(originMatrix[j][i])
                pivotRow = j

        # In case there was a higher pivot, change the matrix so the Pivot will be the maximum
        if maxPivot != abs(originMatrix[i][i]):
            originVectorB[i], originVectorB[pivotRow] = originVectorB[pivotRow], originVectorB[i]
            originMatrix[i], originMatrix[pivotRow] = originMatrix[pivotRow], originMatrix[i]

    # Saving the Linear Equation after changing rows/cols
    LinearEquation = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [LinearEquation[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(LinearEquation, 'Updated Linear Equation', False)

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

        # If the summation of the row is bigger than the pivot, return False (The matrix isn't diagonal dominant)
        if rowSum > abs(matrix[i][i]):
            return False

    # The matrix is Diagonal Dominant
    return True


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
            file.write('\n' if message == 'Updated Linear Equation' else '')

        # In case we sent a data
        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('' if isVector else '\n')

        # Used to enhance the appearance
        if message == 'Updated Linear Equation':
            file.write('\n==========================================================================================\n')
            for i in range(len(data) + 1):
                file.write('{: ^25}'.format('Iteration' if i == 0 else chr(64 + i)))


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------ Jacobi Method ------------------------------')


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Linear Equation to solve
    inputMatrix = [[4, 2, 0], [2, 10, 4], [0, 4, 5]]
    inputVectorB = [[2], [6], [5]]

    print('---------- Jacobi Method ----------')
    Jacobi(inputMatrix, inputVectorB)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
