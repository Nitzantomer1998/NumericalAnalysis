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


def max_function_value(f, left_domain, right_domain):
    
    f = sympy.utilities.lambdify(x, f)

    max_value = max(f(left_domain), f(right_domain))

    while left_domain < right_domain:

        max_value = max(max_value, f(left_domain))

        left_domain = left_domain + 0.1

    return max_value


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
