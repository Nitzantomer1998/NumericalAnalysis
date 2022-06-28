# Finding Area Value Using Trapezoidal Method


# Libraries for getting the derivative of a function
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Libraries for calculation log
from math import log

# Global variable to set the accuracy of the solution
ACCURACY = 0.00001


def Trapezoidal(f, leftDomain, rightDomain, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [leftDomain, rightDomain]

    :param f: Our function
    :param leftDomain: Left domain of the function
    :param rightDomain: Right domain of the function
    :param sectionAmount: The amount of section
    """
    # Variable to store the highest possible section amount without losing information in the process
    sectionAmountLimit = (((rightDomain - leftDomain) ** 3 * MaxFunctionValue(f, leftDomain, rightDomain)) / (12 * ACCURACY)) ** 0.5

    # In case the user chose more section than we can perform without losing information
    if sectionAmount > sectionAmountLimit:

        # Appropriate failed message
        print(f'You chose too many section, the limit is {sectionAmountLimit}')

    # Initiate the function to be able to calculate Y base on given x
    f = lambdify(x, f)

    # Calculating step size
    h = (rightDomain - leftDomain) / sectionAmount

    # Initialize the integral value
    integral = f(leftDomain) + f(rightDomain)

    # Calculate the rest of the integral value
    for i in range(1, sectionAmount):
        integral = integral + 2 * f(leftDomain + i * h)

    # Print the area value
    print(f'Sum of the area --> {int(h / 2 * integral * 10 ** 5) / 10 ** 5}')


def MaxFunctionValue(f, startAt, endAt):
    """
    Method for finding the highest point of a function

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    """
    # Variable to store the derivative function
    g = f.diff(x)

    # Activating the functions to be able to get an X
    f = lambdify(x, f)
    g = lambdify(x, g)

    # Variable to store the maximum iteration we allowed
    maxIteration = int(-(log(ACCURACY / (domainEnd - domainStart)) / log(2))) + 1

    # Variable to store the max value of the function
    maxValue = max(f(startAt), f(endAt))

    # Divide our function domain range into multiply domains with 0.1 range
    while startAt < endAt:

        # In case the derivative function changes its sign (Mean there's a possibility for an extreme point)
        if g(startAt) * g(startAt + 0.1) < 0:

            # Getting a possibility for an extreme point (Might be a Root or an Extreme point)
            possiblePoint = Secant(g, startAt, startAt + 0.1, maxIteration)

            # In case we found an extreme point
            if f(possiblePoint) > maxValue:
                maxValue = f(possiblePoint)

        # Update our domain for the next iteration
        startAt = startAt + 0.1

    # Return the highest Y value in the function domain
    return maxValue


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

        # In case we found our root, Return the root and the iteration number
        if abs(f(nextX)) < ACCURACY:
            return nextX

        # Update the previewX to be the currentX
        previewX = currentX

        # Update the currentX to be new one
        currentX = nextX

    # In case we didn't find the root within the allowed amount iteration, Print fail message and shut down the program
    print("Failed to find the root, Secant Method isn't suitable")


# Our Program Driver
if __name__ == "__main__":

    # Symbol
    x = sp.symbols('x')

    # Input section
    function = sp.sin(x)
    domainStart = 0
    domainEnd = sp.pi
    sectionDivide = 4

    # Running the program
    print('---------- Trapezoidal Rule Method ----------')
    Trapezoidal(function, domainStart, domainEnd, sectionDivide)
