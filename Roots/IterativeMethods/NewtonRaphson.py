# Finding Roots Using Newton-Raphson Method


# Libraries for getting the derivative of a function
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Libraries for calculation log
from math import log

# Global variable to set the accuracy of the solution
ACCURACY = 0.00001


def rootFinder(f, startAt, endAt, maxIteration):
    """
    Method for finding the function Roots

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    :param maxIteration: The maximum iteration for finding the root
    """
    # Variables to store the derivative function
    g = f.diff(x)
    h = g.diff(x)

    # Activating the functions to be able to get an X
    f = lambdify(x, f)
    g = lambdify(x, g)
    h = lambdify(x, h)

    # Divide our function domain range into multiply domains with 0.1 range, then search for each one of them for a root
    while startAt < endAt:

        # In case the root is in the domain edge
        if f(startAt) == 0:
            printIntoFile(['None (Special case)', startAt], True)
            print(f'The root --> {startAt}    Iteration --> None (Special case)')

            startAt = startAt + 0.1
            continue

        # In case the function changes its sign (Means there's at least one root)
        if f(startAt) * f(startAt + 0.1) < 0:
            root, iteration = newtonRaphsonMethod(f, g, startAt + 0.05, maxIteration)
            printIntoFile([iteration, root], True)
            print('The root --> ' + str(root) + '\tIteration --> ' + str(iteration))

        # In case the derivative function changes its sign (Mean there's a possibility for a root)
        if g(startAt) * g(startAt + 0.1) < 0:

            # Getting a possibility for a root (Might be a Root or an Extreme point)
            possibleRoot, iteration = newtonRaphsonMethod(g, h, startAt + 0.05, maxIteration)

            # In case we found a root
            if abs(f(possibleRoot)) < ACCURACY:
                printIntoFile([iteration, possibleRoot], True)
                print('The root --> ' + str(possibleRoot) + '\tIteration --> ' + str(iteration))

            else:
                printIntoFile([iteration, '"Failed" Found Extreme Point, Not A Root'], True)

        # Update our domain for the next iteration
        startAt = startAt + 0.1


def newtonRaphsonMethod(f, g, currentX, maxIteration):
    """
    Finding the function root

    :param f: Our function
    :param g: The derivative function of f
    :param currentX: The value of the middle domain range of the function
    :param maxIteration: The maximum iteration for finding the root
    :return: The root of the function if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for i in range(maxIteration):

        # Variable to store the next X
        nextX = currentX - f(currentX) / g(currentX)

        # Save the calculation in the file
        printIntoFile([i + 1, nextX, f(nextX), g(nextX)], False)

        # In case we found our root, Return the root and the iteration number
        if abs(f(nextX)) < ACCURACY:
            return int(nextX * 10 ** 5) / 10 ** 5, i + 1

        # Update the currentX to be the new one
        currentX = nextX

    # In case we didn't find the root within the allowed amount of iteration, Print a fail message and end the program
    printIntoFile([maxIteration, 'Failed To Find The Root, The Newton Raphson Method Is Not Suitable For This Function'], True)
    print('Failed To Find The Root, The Newton Raphson Method Is Not Suitable For This Function')
    exit()


def printIntoFile(data, isFinal):
    """
    Printing the data content into a specified file

    :param data: Data is a list representing the arguments
    :param isFinal: If True, We print the root solution, Else we print the calculation
    """
    # Open file and save the sent data
    with open('Calculation.txt', 'a+') as file:

        # In case it's the solution
        if isFinal:
            file.write(f'\nRoot --> {data[1]}    Iteration --> {data[0]}\n')
            file.write('--------------------------------------------------------------------------------------------\n')

        else:
            for i in range(len(data)):
                file.write('{: ^25}'.format(data[i]))
            file.write('\n')


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------ Newton-Raphson Method ------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}{: ^25}'.format('Iteration', 'x', 'f(x)', "f'(x)") + '\n')


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Function to solve
    x = sp.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domainStart = -3
    domainEnd = 2

    # Variable to store the maximum iteration in order to find the function roots
    allowedIteration = int(-(log(ACCURACY / (domainEnd - domainStart)) / log(2))) + 1

    print('---------- Newton Raphson Method ----------')
    rootFinder(function, domainStart, domainEnd, allowedIteration)
    print('\nCalculation Is Done, Check File "Calculation" For More Information')
