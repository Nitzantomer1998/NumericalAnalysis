# Solving Equation System Using LU Decomposition Method


# Global Variable [Only Used To print the iteration number]
PRINT_COUNTER = 0


def LU(originMatrix, originVectorB):
    """
    Solving equation system in the LU Decomposition method

    :param originMatrix: NxN Matrix
    :param originVectorB: Nx1 Vector
    """
    # Check if the matrix is Quadratic matrix, and check if the vector is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Organize the matrix pivots
            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            # Getting the Lower, and Upper matrices of our equation system
            upperMatrix, lowerMatrix = findLU(originMatrix)

            # Solve Ly = B
            vectorSolutionY = forwardSubstitution(lowerMatrix, originVectorB)

            # Solve Ux = y (Getting the equation system solution)
            vectorSolutionX = finalSolution(originMatrix, originVectorB, backSubstitution(upperMatrix, vectorSolutionY))

            # Saving the equation system final solution
            printIntoFile(vectorSolutionX, 'Equation System Final Solution')
            print(f'Equation system solution {list(map(lambda x: int(x[0] * 10 ** 5) / 10 ** 5, vectorSolutionX))}')

        # According message In case there is more or less than one solution
        else:
            printIntoFile(None, 'This is a Singular matrix')
            print('This is a Singular matrix')

    # In case the input equation system isn't meet the demands
    else:
        printIntoFile(None, "The input equation system isn't match")
        print("The input equation system isn't match")


