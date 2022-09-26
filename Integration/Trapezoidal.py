# Finding Area Value Using Trapezoidal Method


# Libraries for working with derivatives
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Global variable to set the accuracy of the solution
ACCURACY = 0.00001


def trapezoidal_rule_method(f, left_domain, right_domain, section_amount):
    
    if not is_inserted_data_valid(f, left_domain, right_domain, section_amount):
        return

    f = sympy.utilities.lambdify(x, f)

    h = abs(right_domain - left_domain) / section_amount

    interval = f(left_domain) + f(right_domain)

    for i in range(1, section_amount):
        interval = interval + 2 * f(left_domain + i * h)

    print(f'Sum Of Area --> {int(h / 2 * interval * 10 ** 5) / 10 ** 5}')


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
