# Finding Area Value Using Romberg Method


# Libraries for working with derivatives
import sympy as sp
from sympy.utilities.lambdify import lambdify


def romberg_method(f, left_domain, right_domain, section_amount):
    
    if not is_inserted_data_valid(f, left_domain, right_domain, section_amount):
        return

    f = sympy.utilities.lambdify(x, f)

    r = [[0.0 for _ in range(section_amount)] for _ in range(section_amount)]

    for i in range(section_amount):

        r[i][0] = trapezoidal_rule_method(f, left_domain, right_domain, 2 ** i)

        for j in range(i):
            r[i][j + 1] = (4 ** (j + 1) * r[i][j] - r[i - 1][j]) / (4 ** (j + 1) - 1)

    print(f'Sum Of Area --> {int(r[-1][-1] * 10 ** 5) / 10 ** 5}')


    
def trapezoidal_rule_method(f, left_domain, right_domain, section_amount):
    
    h = abs(right_domain - left_domain) / section_amount

    interval = f(left_domain) + f(right_domain)

    for i in range(1, section_amount):
        interval = interval + 2 * f(left_domain + i * h)

    return h * interval / 2


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
