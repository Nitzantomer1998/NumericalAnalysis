# Finding Roots Using Newton Raphson Method


# Libraries for getting the derivative of a function
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Libraries for calculation log
from math import log

# Global variable to set the accuracy of the solution
ACCURACY = 0.00001


def root_finder(f, left_domain, right_domain, max_iteration_allowed):
   
    g = f.diff(x)
    h = g.diff(x)

    f = sympy.utilities.lambdify(x, f)
    g = sympy.utilities.lambdify(x, g)
    h = sympy.utilities.lambdify(x, h)

    while left_domain < right_domain:

        if f(left_domain) == 0:

            print_into_file(None, f'Root --> {left_domain}    Iteration --> 0')

            print(f'Root --> {left_domain}    Iteration --> 0')

        elif f(left_domain) * f(left_domain + 0.1) < 0:

            root, iteration = newton_raphson_method(f, g, left_domain + 0.05, max_iteration_allowed)

            print_into_file(None, f'Root --> {root}    Iteration --> {iteration}')

            print(f'Root --> {root}    Iteration --> {iteration}')

        elif g(left_domain) * g(left_domain + 0.1) < 0:

            possible_root, iteration = newton_raphson_method(g, h, left_domain + 0.05, max_iteration_allowed)

            if abs(f(possible_root)) == 0:

                print_into_file(None, f'Root --> {possible_root}    Iteration --> {iteration}')

                print(f'Root --> {possible_root}    Iteration --> {iteration}')

        left_domain = left_domain + 0.1


def newton_raphson_method(f, g, current_x, max_iteration_allowed):
   
    for i in range(max_iteration_allowed):

        next_x = current_x - f(current_x) / g(current_x)

        print_into_file([i + 1, next_x, f(next_x), g(next_x)], None)

        if abs(f(next_x)) < solution_accuracy:
            return int(next_x * 10 ** 5) / 10 ** 5, i + 1

        current_x = next_x

    print_into_file(None, 'Error: Failed To Find The Root')
    print('Error: Failed To Find The Root')
    exit(True)


def calculate_max_iteration_allowed(left_domain, right_domain):
    """
    Returning the max allowed amount of iteration in order to find a root

    :param left_domain: The domain start of the function
    :param right_domain: The domain end of the function
    :return: The max allowed amount of iteration
    """
    # returning the max allowed iteration for finding a root using the needed formula calculation
    return int(- sympy.ln(solution_accuracy / (right_domain - left_domain)) / sympy.ln(2)) + 1

   
def print_into_file(data, message):
    
    with open('Calculation.txt', 'a+') as file:

        if message:
            file.write('\n{: ^25}\n'.format(message))
            file.write('--------------------------------------------------------------------------------------------\n')

        if data:
            for i in range(len(data)):
                file.write('{: ^25}'.format(float(data[i])))
            file.write('\n')



def reset_file():
   
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------- Newton Raphson Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}{: ^25}\n'.format('Iteration', 'x', 'f(x)', "f'(x)"))


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Input section
    x = sp.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domainStart = -3
    domainEnd = 2

    # Variable to store the maximum iteration in order to find the function roots
    allowedIteration = int(-(log(ACCURACY / (domainEnd - domainStart)) / log(2))) + 1

    # Running the program
    print('---------- Newton Raphson Method ----------')
    rootFinder(function, domainStart, domainEnd, allowedIteration)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
