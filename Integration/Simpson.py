# Finding Area Value Using Simpson Method


# Libraries for working with derivatives
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Global variable to set the accuracy of the solution
ACCURACY = 0.00001


def simpson_rule_method(f, left_domain, right_domain, section_amount):
    
    if not is_inserted_data_valid(f, left_domain, right_domain, section_amount):
        return

    f = sympy.utilities.lambdify(x, f)

    h = abs(right_domain - left_domain) / section_amount

    interval = f(left_domain) + f(right_domain)

    for i in range(1, section_amount):

        if i % 2 == 0:
            interval = interval + 2 * f(i * h + left_domain)

        else:
            interval = interval + 4 * f(i * h + left_domain)

    print(f'Sum Of The Area --> {int(1 / 3 * h * interval * 10 ** 5) / 10 ** 5}')


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
    sectionDivide = 20

    # Running the program
    print('---------- Simpson Rule Method ----------')
    Simpson(function, domainStart, domainEnd, sectionDivide)
