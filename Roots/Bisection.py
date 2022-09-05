# Finding Roots Using Bisection Method


# Libraries for getting the derivatives of a function
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Libraries for calculation log
from math import log

# Global variable to set the accuracy of the solution
ACCURACY = 0.00001


def root_finder(f, left_domain, right_domain, max_iteration_allowed):
   
    g = f.diff(x)

    f = sympy.utilities.lambdify(x, f)
    g = sympy.utilities.lambdify(x, g)

    while left_domain < right_domain:

        if f(left_domain) == 0:

            print_into_file(None, f'Root --> {left_domain}    Iteration --> 0')

            print(f'Root --> {left_domain}    Iteration --> 0')

        elif f(left_domain) * f(left_domain + 0.1) < 0:

            root, iteration = bisection_method(f, left_domain, left_domain + 0.1, max_iteration_allowed)

            print_into_file(None, f'Root --> {root}    Iteration --> {iteration}')

            print(f'Root --> {root}    Iteration --> {iteration}')

        elif g(left_domain) * g(left_domain + 0.1) < 0:

            possible_root, iteration = bisection_method(g, left_domain, left_domain + 0.1, max_iteration_allowed)

            if abs(f(possible_root)) == 0:

                print_into_file(None, f'Root --> {possible_root}    Iteration --> {iteration}')

                print(f'Root --> {possible_root}    Iteration --> {iteration}')

        left_domain = left_domain + 0.1



def bisection_method(f, left_domain, right_domain, max_iteration_allowed):
   
    for i in range(max_iteration_allowed):

        middle_domain = left_domain + (right_domain - left_domain) / 2

        print_into_file([i + 1, middle_domain, f(middle_domain)], None)

        if abs(f(middle_domain)) < solution_accuracy:
            return int(middle_domain * 10 ** 5) / 10 ** 5, i + 1

        elif f(left_domain) * f(middle_domain) < 0:
            right_domain = middle_domain

        else:
            left_domain = middle_domain

    print_into_file(None, 'Error: Failed To Find The Root')
    print('Error: Failed To Find The Root')


def calculate_max_iteration_allowed(left_domain, right_domain):
    
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
        file.write('------------------------------- Bisection Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}\n'.format('Iteration', 'x', 'f(x)'))

# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    # Function to solve
    x = sp.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domainStart = -3
    domainEnd = 2

    # Variable to store the maximum iteration in order to find the function roots
    allowedIteration = int(-(log(ACCURACY / (domainEnd - domainStart)) / log(2))) + 1

    # Running the program
    print('---------- Bisection Method ----------')
    rootFinder(function, domainStart, domainEnd, allowedIteration)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
