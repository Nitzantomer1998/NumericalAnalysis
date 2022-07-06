# Finding Area Value Using Simpson Method


# Libraries for working with derivatives
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Global variable to set the accuracy of the solution
ACCURACY = 0.00001


def Simpson(f, startAt, endAt, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [startAt, endAt]

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    :param sectionAmount: The amount of section
    """
    # Variable to store the highest possible section amount without losing information in the process
    sectionAmountMaxLimit = ((abs(endAt - startAt) ** 3 * MaxFunctionValue(f, startAt, endAt)) / (12 * ACCURACY)) ** 0.5

    # Variable to store the lowest possible section amount without losing information in the process
    sectionAmountMinLimit = (abs(endAt - startAt) ** 5 * MaxFunctionValue(f.diff(x).diff(x).diff(x).diff(x), startAt, endAt) / (180 * ACCURACY)) ** 0.25

    # In case the user chose negative amount of sections
    if sectionAmount <= 0:
        print('You can not divide section to be negative')
        return

    # In case the amount of section is not an even number
    if sectionAmount % 2 == 1:
        print('Section amount must be an even number')
        return

    # In case the user chose more section than we can perform without losing information
    if sectionAmount > sectionAmountMaxLimit:
        print(f'You chose too many section, the upper limit is {int(sectionAmountMaxLimit)}')
        return

    # In case the user chose lower section than we can perform without losing information
    if sectionAmount + 1 < sectionAmountMinLimit:
        print(f'You chose below the minimum section, the lower limit is {int(sectionAmountMinLimit)}')
        return

    # Initiate the function to be able to calculate Y base on given x
    f = lambdify(x, f)

    # Calculating step size (gap)
    h = abs(endAt - startAt) / sectionAmount

    # Initialize the integral value
    interval = f(startAt) + f(endAt)

    # Calculate the rest of the interval value
    for i in range(1, sectionAmount):

        # In case the index is on even place [0, 2, 4, 6 ...]
        if i % 2 == 0:
            interval = interval + 2 * f(i * h + startAt)

        # In case the index is on odd place [1, 3, 5, 7 ...]
        else:
            interval = interval + 4 * f(i * h + startAt)

    # Print the area value
    print(f'Sum of the area --> {int(1 / 3 * h * interval * 10 ** 5) / 10 ** 5}')


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
    sectionDivide = 20

    # Running the program
    print('---------- Simpson Rule Method ----------')
    Simpson(function, domainStart, domainEnd, sectionDivide)
