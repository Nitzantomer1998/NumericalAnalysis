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