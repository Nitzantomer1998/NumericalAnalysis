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
    f = lambdify(x, f)

    maxValue = max(f(startAt), f(endAt))

    while startAt < endAt:

        maxValue = max(maxValue, f(startAt))

        startAt = startAt + 0.1

    return maxValue


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
