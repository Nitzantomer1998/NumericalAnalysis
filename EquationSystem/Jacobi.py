# Solving Equation System Using Jacobi Method


# Global Variable To Store The Machine Precision, (Set the accuracy of the solution)
ACCURACY = 1


def Jacobi(originMatrix, originVectorB):
    """
    Solving equation system using the Jacobi method

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

                    printIntoFile(None, "This equation System isn't Converge", False)
                    print("This equation system isn't Converge")
                    exit()

            # Saving the equation system final solution
            printIntoFile(currentIteration, 'Solution', True)
            print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, currentIteration))}')

        # According message In case there is more or less than one solution
        else:
            printIntoFile('This is a Singular matrix', True, False)
            print('This is a Singular matrix')

    # In case the input equation system isn't meet the demands
    else:
        printIntoFile(None, "The input equation system isn't match", False)
        print("The input equation system isn't match")


def organizeMatrix(originMatrix, originVectorB):
    """
    Taking care that the pivot in the every row will be the highest possible, and return the updated equation system

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :return: The updated equation system
    """
    # Saving the equation system the user gave
    EquationSystem = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [EquationSystem[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(EquationSystem, 'Inserted Equation System\n', False)

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

    # Saving the equation system after changing rows/cols
    EquationSystem = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [EquationSystem[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(EquationSystem, 'Updated Equation System', False)

    # Return the updated equation system
    return originMatrix, originVectorB