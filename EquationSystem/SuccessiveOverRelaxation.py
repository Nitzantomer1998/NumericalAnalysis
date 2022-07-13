def SuccessiveOverRelaxation(originMatrix, originVectorB, W):
    """
    Solving Equation System in the Successive Over Relaxation method

    :param originMatrix: NxN Matrix
    :param originVectorB: Nx1 Vector
    :param W: The relaxation factor
    """
    if len(originMatrix) != len(originMatrix[0]) or len(originVectorB) != len(originMatrix) or len(originVectorB[0]) != 1:
        printIntoFile(None, "The input equation system isn't match", False)
        print("The input equation system isn't match")

    if determinantMatrix(originMatrix) == 0:
        printIntoFile(None, 'This is Singular matrix', False)
        print('This is Singular matrix')

    if W <= 0 or W >= 2:
        printIntoFile(None, 'Omega parameter is out of boundaries', False)
        print('Omega parameter is out of boundaries')

    originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

    machinePrecision()

    prevIteration = [[0 for _ in range(1)] for _ in range(len(originMatrix))]
    currentIteration = [[0 for _ in range(1)] for _ in range(len(originMatrix))]

    for _ in range(500):

        for i in range(len(originMatrix)):
            rowSum = 0
            for j in range(len(originMatrix)):
                if i != j:
                    rowSum = rowSum + originMatrix[i][j] * currentIteration[j][0]

            currentIteration[i][0] = (1 - W) * prevIteration[i][0] + (W * (originVectorB[i][0] - rowSum) / originMatrix[i][i])

        printIntoFile(currentIteration, _ + 1, True)

        if all([False if abs(currentIteration[row][0] - prevIteration[row][0]) > ACCURACY else True for row in range(len(currentIteration))]):
            break

        prevIteration = [[currentIteration[row][0] for _ in range(1)] for row in range(len(currentIteration))]

        if _ == 499:
            if not isDiagonalDominant(originMatrix):
                printIntoFile(None, "This isn't Diagonal Dominant matrix", False)
                print("This isn't Diagonal Dominant matrix")

            printIntoFile(None, "This equation system isn't Converge", False)
            print("This equation system isn't Converge")
            exit()

    printIntoFile(currentIteration, 'Solution', True)
    print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, currentIteration))}')


def organizeMatrix(originMatrix, originVectorB):
    """
    Taking care that the pivot in the every row will be the highest possible, and return the updated equation system

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :return: The updated equation system
    """
    EquationSystem = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [EquationSystem[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(EquationSystem, 'Inserted Equation System\n', False)

    for i in range(len(originMatrix)):

        maxPivot = abs(originMatrix[i][i])

        pivotRow = -1

        for j in range(i + 1, len(originMatrix)):

            if abs(originMatrix[j][i]) > maxPivot:
                maxPivot = abs(originMatrix[j][i])
                pivotRow = j

        if maxPivot != abs(originMatrix[i][i]):
            originVectorB[i], originVectorB[pivotRow] = originVectorB[pivotRow], originVectorB[i]
            originMatrix[i], originMatrix[pivotRow] = originMatrix[pivotRow], originMatrix[i]

    EquationSystem = [[originMatrix[row][col] for col in range(len(originMatrix[0]))] for row in range(len(originMatrix))]
    [EquationSystem[row].append(originVectorB[row][0]) for row in range(len(originVectorB))]
    printIntoFile(EquationSystem, 'Updated Equation System', False)

    return originMatrix, originVectorB


def isDiagonalDominant(matrix):
    """
    Check if the pivot in every row is bigger than the sum of the whole row (without the pivot),
    If yes return True, else False

    """
    for i in range(len(matrix)):
        rowSum = 0
        for j in range(len(matrix)):
            if i != j:
                rowSum = rowSum + abs(matrix[i][j])

        if rowSum > abs(matrix[i][i]):
            return False

    return True


def determinantMatrix(matrix):
    """
    Calculate the matrix determinant and return the result

    :param matrix: NxN Matrix
    :return: Matrix determinant
    """
    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value

    determinantSum = 0

    for current_column in range(len(matrix)):
        sign = (-1) ** current_column

        determinant_sub = determinantMatrix(
            [row[: current_column] + row[current_column + 1:] for row in (matrix[: 0] + matrix[0 + 1:])])

        determinantSum = determinantSum + (sign * matrix[0][current_column] * determinant_sub)

    return determinantSum


def machinePrecision():
    """
    Function to find your Machine Precision, And set the accuracy of the solution

    """
    global ACCURACY

    while 1.0 + (ACCURACY / 2) > 1.0:
        ACCURACY = ACCURACY / 2


def printIntoFile(data, message, isVector):
    """
    Printing the content into a specified file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    :param isVector: isVector is a boolean representing if the data is a vector
    """
    with open('Calculation.txt', 'a+') as file:

        if message:
            file.write('\n{: ^25}'.format(message))
            file.write('' if message != 'Updated Equation System' else '\n')

        if data:
            for i in range(len(data)):
                for j in range(len(data[i])):
                    file.write('{: ^25}'.format(float(data[i][j])))
                file.write('' if isVector else '\n')

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