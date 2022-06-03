# Finding Roots Using Secant Method


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
    # Variable to store the derivative function
    g = f.diff(x)

    # Activating the functions to be able to get an X
    f = lambdify(x, f)
    g = lambdify(x, g)

    # Divide our function domain range into multiply domains with 0.1 range, then search for each one of them for a root
    while startAt < endAt:

        # In case the root is in the domain edge
        if f(startAt) == 0:
            printIntoFile(None, f'The root --> {startAt}    Iteration --> None (Special case)')
            print(f'The root --> {startAt}    Iteration --> None (Special case)')

            startAt = startAt + 0.1
            continue

        # In case the function changes its sign (Means there's at least one root)
        if f(startAt) * f(startAt + 0.1) < 0:
            root, iteration = Secant(f, startAt, startAt + 0.1, maxIteration)
            printIntoFile(None, f'The root --> {root}    Iteration --> {iteration}')
            print(f'The root --> {root}    Iteration --> {iteration}')

        # In case the derivative function changes its sign (Mean there's a possibility for a root)
        if g(startAt) * g(startAt + 0.1) < 0:

            # Getting a possibility for a root (Might be a Root or an Extreme point)
            possibleRoot, iteration = Secant(g, startAt, startAt + 0.1, maxIteration)

            # In case we found a root
            if abs(f(possibleRoot)) < ACCURACY:
                printIntoFile(None, f'The root --> {possibleRoot}    Iteration --> {iteration}')
                print(f'The root --> {possibleRoot}    Iteration --> {iteration}')

            else:
                printIntoFile(None, 'Failed found extreme point, Not a root')

        # Update our domain for the next iteration
        startAt = startAt + 0.1


def Secant(f, previewX, currentX, maxIteration):
    """
    Finding the function root in the domain range [left To right]

    :param f: Our function
    :param previewX: Left domain of the function
    :param currentX: Right domain of the function
    :param maxIteration: The maximum iteration for finding the root
    :return: The root of the function if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for i in range(maxIteration):

        # Variable to store the next X
        nextX = (previewX * f(currentX) - currentX * f(previewX)) / (f(currentX) - f(previewX))

        # Save the calculation in the file
        printIntoFile([i + 1, previewX, nextX, f(nextX)], None)

        # In case we found our root, Return the root and the iteration number
        if abs(f(nextX)) < ACCURACY:
            return int(nextX * 10 ** 5) / 10 ** 5, i + 1

        # Update the previewX to be the currentX
        previewX = currentX

        # Update the currentX to be new one
        currentX = nextX

    # In case we didn't find the root within the allowed amount iteration, Print fail message and shut down the program
    printIntoFile(None, "Failed to find the root, Secant Method isn't suitable")
    print("Failed to find the root, Secant Method isn't suitable")


def printIntoFile(data, message):
    """
    Printing the content into a specified file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    """
    # Open file and save the sent content
    with open('Calculation.txt', 'a+') as file:

        # In case we sent a message
        if message:
            file.write('\n{: ^25}\n'.format(message))
            file.write('--------------------------------------------------------------------------------------------\n')

        # In case we sent a data
        if data:
            for i in range(len(data)):
                file.write('{: ^25}'.format(float(data[i])))

            file.write('\n')


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------- Secant Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}{: ^25}\n'.format('Iteration', 'previewX', 'nextX', "f(nextX)"))


# Our Program Driver
if __name__ == "__main__":

    resetFile()

    x = sp.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domainStart = -3
    domainEnd = 2

    allowedIteration = int(-(log(ACCURACY / (domainEnd - domainStart)) / log(2))) + 1

    print('---------- Secant Method ----------')
    rootFinder(function, domainStart, domainEnd, allowedIteration)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
