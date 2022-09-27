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


def max_function_value(f, left_domain, right_domain):
    
    f = sympy.utilities.lambdify(x, f)

    max_value = max(f(left_domain), f(right_domain))

    while left_domain < right_domain:

        max_value = max(max_value, f(left_domain))

        left_domain = left_domain + 0.1

    return max_value



def is_inserted_data_valid(f, left_domain, right_domain, section_amount):
    
    if section_amount <= 0:
        print('Error: Section Amount Must Be Non Negative Integer')
        return False

    max_section_amount = ((abs(right_domain - left_domain) ** 3 * max_function_value(f, left_domain, right_domain)) / (12 * solution_accuracy)) ** 0.5
    if section_amount > max_section_amount:
        print(f'You Chose Too Many Section, The Upper Limit Is {int(max_section_amount)}')
        return False

    return True


if __name__ == "__main__":

    x = sympy.symbols('x')
    function = sympy.sin(x)
    domain_start = 0
    domain_end = sympy.pi
    section_divide = 10
    solution_accuracy = 0.00001

    print('---------- Romberg Method ----------')
    romberg_method(function, domain_start, domain_end, section_divide)
