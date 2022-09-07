# Finding Roots Using Secant Method


# Libraries for getting the derivative of a function
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

            root, iteration = secant_method(f, left_domain, left_domain + 0.1, max_iteration_allowed)

            print_into_file(None, f'Root --> {root}    Iteration --> {iteration}')

            print(f'Root --> {root}    Iteration --> {iteration}')

        elif g(left_domain) * g(left_domain + 0.1) < 0:

            possible_root, iteration = secant_method(g, left_domain, left_domain + 0.1, max_iteration_allowed)

            if abs(f(possible_root)) < solution_accuracy:

                print_into_file(None, f'Root --> {possible_root}    Iteration --> {iteration}')

                print(f'Root --> {possible_root}    Iteration --> {iteration}')

        left_domain = left_domain + 0.1


def secant_method(f, previous_x, current_x, max_iteration_allowed):
   
    for i in range(max_iteration_allowed):

        next_x = (previous_x * f(current_x) - current_x * f(previous_x)) / (f(current_x) - f(previous_x))

        print_into_file([i + 1, previous_x, next_x, f(next_x)], None)

        if abs(f(next_x)) < solution_accuracy:
            return int(next_x * 10 ** 5) / 10 ** 5, i + 1

        previous_x = current_x

        current_x = next_x

    print_into_file(None, 'Error: Failed To Find The Root')
    print('Error: Failed To Find The Root')
    exit(True)


def printIntoFile(data, message):
    """
    Printing the content into a specified file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    """
    # Open file and save the sent content
    with open('Calculation.txt', 'a+') as file:

        # In case we sent a message
        if message:
            file.write('\n{: ^25}\n'.format(message))
            file.write('--------------------------------------------------------------------------------------------\n')

        # In case we sent a data
        if data:
            for i in range(len(data)):
                file.write('{: ^25}'.format(float(data[i])))

            file.write('\n')


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------- Secant Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}{: ^25}\n'.format('Iteration', 'previewX', 'nextX', "f(nextX)"))


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
    print('---------- Secant Method ----------')
    rootFinder(function, domainStart, domainEnd, allowedIteration)
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
