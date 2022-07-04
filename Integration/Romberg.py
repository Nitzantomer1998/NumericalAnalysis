# Finding Area Value Using Romberg Method


# Libraries for working with derivatives
import sympy as sp
from sympy.utilities.lambdify import lambdify


def Romberg(f, startAt, endAt, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [startAt, endAt]

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    :param sectionAmount: The amount of section
    """
    # Initiate the function to be able to calculate Y base on given x
    f = lambdify(x, f)

    # Initialize matrix to store approximation area values
    R = [[0 for _ in range(sectionAmount)] for _ in range(sectionAmount)]

    # Double loop to fill R with area approximation values
    for i in range(sectionAmount):
        R[i][0] = Trapezoidal(f, startAt, endAt, 2 ** i)

        for j in range(i):
            R[i][j + 1] = (4 ** (j + 1) * R[i][j] - R[i - 1][j]) / (4 ** (j + 1) - 1)

    # Print the area value
    print(f'Sum of the area --> {int(R[-1][-1] * 10 ** 5) / 10 ** 5}')


def Trapezoidal(f, startAt, endAt, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [startAt, endAt]

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    :param sectionAmount: The amount of section
    :return: Interval value
    """
    # Calculating step size (gap)
    h = abs(endAt - startAt) / sectionAmount

    # Initialize the interval value
    interval = f(startAt) + f(endAt)

    # Calculate the rest of the interval value
    for i in range(1, sectionAmount):
        interval = interval + 2 * f(startAt + i * h)

    # Return the area approximation value
    return interval * h / 2


# Our Program Driver
if __name__ == "__main__":

    # Symbol
    x = sp.symbols('x')

    # Input section
    function = sp.sin(x)
    domainStart = 0
    domainEnd = sp.pi
    sectionDivide = 5

    # Running the program
    print('---------- Romberg Method ----------')
    Romberg(function, domainStart, domainEnd, sectionDivide)
