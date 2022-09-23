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


def is_inserted_data_valid(f, left_domain, right_domain, section_amount):
    
    if section_amount <= 0:
        print('Error: Section Amount Must Be Non Negative Integer')
        return False

    if section_amount % 2 == 1:
        print('Section Amount Must Be An Even Integer')
        return False

    max_section_amount = ((abs(right_domain - left_domain) ** 3 * max_function_value(f, left_domain, right_domain)) / (12 * solution_accuracy)) ** 0.5
    if section_amount > max_section_amount:
        print(f'You Chose Too Many Section, The Upper Limit Is {int(max_section_amount)}')
        return False

    min_section_amount = (abs(right_domain - left_domain) ** 5 * max_function_value(f.diff(x).diff(x).diff(x).diff(x), left_domain, right_domain) / (180 * solution_accuracy)) ** 0.25
    if section_amount + 1 < min_section_amount:
        print(f'You Chose Below The Minimum Section, The Lower Limit Is {int(min_section_amount)}')
        return False

    return True


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
