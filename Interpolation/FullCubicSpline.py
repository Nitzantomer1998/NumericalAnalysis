# Finding Point Approximation Using Full Cubic Spline Interpolation Method


def full_cubic_spline_interpolation(points_list, x_to_find, derivative_values):
   
    if not is_inserted_data_valid(points_list, x_to_find):
        return

    h, lam, u, d = build_data_table(points_list, derivative_values)

    for i in range(len(points_list) - 1):

        if points_list[i][0] <= x_to_find <= points_list[i + 1][0]:

            built_matrix = [[0 for _ in range(len(points_list))] for _ in range(len(points_list))]
            built_vector = [[d[row] for _ in range(1)] for row in range(len(points_list))]

            for j in range(len(points_list) - 1):
                for k in range(len(points_list) - 1):
                    if j == k:
                        built_matrix[j][j] = 2
                        built_matrix[j + 1][k] = u[j + 1]
                        built_matrix[j][k + 1] = lam[j]

            built_matrix[-1][-1] = 2

            vector_solution = lower_upper_decomposition_method(built_matrix, built_vector)

            if any(vector_solution) is None:
                print('Error: Equation System Failed To Find A Solution')
                return

            y_value = ((points_list[i + 1][0] - x_to_find) ** 3 * vector_solution[i][0] + (x_to_find - points_list[i][0]) ** 3 * vector_solution[i + 1][0]) / (6 * h[i]) + ((points_list[i + 1][0] - x_to_find) * points_list[i][1] + (x_to_find - points_list[i][0]) * points_list[i + 1][1]) / h[i] - (((points_list[i + 1][0] - x_to_find) * vector_solution[i][0] + (x_to_find - points_list[i][0]) * vector_solution[i + 1][0]) * h[i]) / 6

            print(f'Point Approximation --> ({x_to_find}, {int(y_value * 10 ** 5) / 10 ** 5})')

            
def InverseMatrix(originMatrix, originVectorB):
    """
    Solving equation system in the Inverse Matrix method

    :param originMatrix: NxN Matrix
    :param originVectorB: Nx1 Vector
    """
    # Check if the matrix is Quadratic matrix, and check if the vector is in appropriate size
    if len(originMatrix) == len(originMatrix[0]) and len(originVectorB) == len(originMatrix) and len(
            originVectorB[0]) == 1:

        # In case the matrix has one solution
        if determinantMatrix(originMatrix):

            # Organize the matrix pivots
            originMatrix, originVectorB = organizeMatrix(originMatrix, originVectorB)

            # Getting the inverse matrix of originMatrix
            inverseMatrix = findInverse(originMatrix)

            # Getting the equation system solution
            vectorSolution = finalSolution(originMatrix, originVectorB, multiplyMatrix(inverseMatrix, originVectorB))

            # Return the equation system final solution
            return vectorSolution

        # According message In case there is more or less than one solution
        else:
            print('This is a Singular matrix')
            return None

    # In case the input equation system isn't meet the demands
    else:
        print("The input equation system isn't match")
        return None


def organizeMatrix(originMatrix, originVectorB):
    """
    Taking care that the pivot in the every row will be the highest possible, and return the updated equation system

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :return: The updated equation system
    """
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

    # Return the updated equation system
    return originMatrix, originVectorB


def findInverse(matrix):
    """
    Solve the matrix into an Identity matrix, and return the inverse matrix

    :param matrix: NxN matrix
    :return: Inverse NxN matrix
    """
    # Initialize inverseMatrix into an Identity matrix
    inverseMatrix = [[1 if row == col else 0 for col in range(len(matrix))] for row in range(len(matrix))]

    # Solving matrix into an Identity matrix, and get alongside the Inverse Matrix (Lower part)
    for i in range(len(matrix)):

        # In case the pivot isn't one, we will make sure it will be
        if matrix[i][i] != 1:
            inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), i, i, 1 / matrix[i][i]), inverseMatrix)
            matrix = multiplyMatrix(initElementaryMatrix(len(matrix), i, i, 1 / matrix[i][i]), matrix)

        # In case the column under the pivot isn't zero
        for j in range(i + 1, len(matrix)):
            if matrix[j][i] != 0:
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix)

    # Solving matrix into an Identity matrix, and get alongside the Inverse Matrix (Upper part)
    for i in reversed(range(len(matrix))):

        # In case the column above the pivot isn't zero
        for j in reversed(range(i)):
            if matrix[j][i] != 0:
                inverseMatrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), inverseMatrix)
                matrix = multiplyMatrix(initElementaryMatrix(len(matrix), j, i, - matrix[j][i]), matrix)

    # Return the inverse matrix
    return inverseMatrix


def finalSolution(originMatrix, originVectorB, vectorSolution):
    """
    Getting the equation system components, check the accuracy of the solution, if the accuracy isn't precise
    calculate the precise solution and return it

    :param originMatrix: NxN matrix
    :param originVectorB: Nx1 vector
    :param vectorSolution: Nx1 vector semi solution (not surly accurate)
    :return: Nx1 vector, the precise Equation System solution
    """
    # Solve r = Ax0 - b (Vector r represent the accuracy of the solution we found)
    vectorR = multiplyMatrix(originMatrix, vectorSolution)
    for i in range(len(vectorR)):
        vectorR[i][0] = vectorR[i][0] - originVectorB[i][0]

    # Update to the accurate solution
    for i in range(len(vectorSolution)):
        if abs(vectorSolution[i][0] - round(vectorSolution[i][0])) <= max(
                1e-09 * max(abs(vectorSolution[i][0]), abs(round(vectorSolution[i][0]))), 0):
            vectorSolution[i][0] = round(vectorSolution[i][0])

    # Return the final solution of the equation system
    return vectorSolution


def multiplyMatrix(matrixA, matrixB):
    """
    Multiplying two matrices and return the outcome matrix

    :param matrixA: NxM Matrix
    :param matrixB: NxM Matrix
    :return: NxM matrix
    """
    # Initialize NxM matrix filled with zero's
    matrixC = [[0] * len(matrixB[0]) for _ in range(len(matrixA))]

    # Multiply the two matrices and store the outcome in matrixC
    for i in range(len(matrixA)):
        for j in range(len(matrixB[0])):
            for k in range(len(matrixB)):
                matrixC[i][j] = matrixC[i][j] + matrixA[i][k] * matrixB[k][j]

    # Return the outcome matrix
    return matrixC


def initElementaryMatrix(size, row, col, value):
    """
    Initialize elementary matrix, from identity matrix, and a specific value, and return it

    :param size: Matrix size
    :param row: Row index
    :param col: Column index
    :param value: Value parameter
    :return: Return the elementary matrix
    """
    # Initialize the desire elementary matrix
    elementaryMatrix = [[1 if row == col else 0 for col in range(size)] for row in range(size)]
    elementaryMatrix[row][col] = value

    # Return the elementary matrix
    return elementaryMatrix


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


# Our Program Driver
if __name__ == "__main__":

    # Input section
    graphPoints = [[0, 0], [1, 0.8415], [2, 0.9093], [3, 0.1411], [4, -0.7568], [5, -0.9589], [6, -0.2794]]
    derivativeLeft = 0
    derivativeRight = 1
    xValue = 2.5

    # Running the program
    print('---------- Full Cubic Spline Method ----------')
    FullCubicSpline(graphPoints, xValue, derivativeLeft, derivativeRight)
