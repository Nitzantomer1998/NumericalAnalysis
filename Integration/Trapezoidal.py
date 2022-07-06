# Finding Area Value Using Trapezoidal Method


# Libraries for working with derivatives
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Global variable to set the accuracy of the solution
ACCURACY = 0.00001


def Trapezoidal(f, startAt, endAt, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [startAt, endAt]

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    :param sectionAmount: The amount of section
    """
    # Variable to store the highest possible section amount without losing information in the process
    sectionAmountLimit = ((abs(endAt - startAt) ** 3 * MaxFunctionValue(f, startAt, endAt)) / (12 * ACCURACY)) ** 0.5

    # In case the user chose negative amount of sections
    if sectionAmount <= 0:
        print('You can not divide section to be negative')
        return

    # In case the user chose more section than we can perform without losing information
    if sectionAmount > sectionAmountLimit:
        print(f'You chose too many section, the limit is {int(sectionAmountLimit)}')
        return

    # Initiate the function to be able to calculate Y base on given x
    f = lambdify(x, f)

    # Calculating step size (gap)
    h = abs(endAt - startAt) / sectionAmount

    # Initialize the interval value
    interval = f(startAt) + f(endAt)

    # Calculate the rest of the interval value
    for i in range(1, sectionAmount):
        interval = interval + 2 * f(startAt + i * h)

    # Print the area value
    print(f'Sum of the area --> {int(h / 2 * interval * 10 ** 5) / 10 ** 5}')


def MaxFunctionValue(f, startAt, endAt):
    """
    Method for finding the highest point of startAt function

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    """
    # Activating the function to be able to get an X
    f = lambdify(x, f)

    # Variable to store the max value of the function (Axis Y)
    maxValue = max(f(startAt), f(endAt))

    # Divide our function domain range into multiply domains with 0.1 range
    while startAt < endAt:

        # Update the maximum Y value of the function
        maxValue = max(maxValue, f(startAt))

        # Update our domain for the next iteration
        startAt = startAt + 0.1

    # Return the highest Y value in the function domain
    return maxValue


# Our Program Driver
if __name__ == "__main__":

    # Symbol
    x = sp.symbols('x')

    # Input section
    function = sp.sin(x)
    domainStart = 0
    domainEnd = sp.pi
    sectionDivide = 10

    # Running the program
    print('---------- Trapezoidal Rule Method ----------')
    Trapezoidal(function, domainStart, domainEnd, sectionDivide)
