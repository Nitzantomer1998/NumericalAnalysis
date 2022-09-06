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


def NewtonRaphson(f, g, currentX, maxIteration):
    """
    Finding the function root

    :param f: Our function
    :param g: The derivative function of f
    :param currentX: The value of the middle domain range of the function
    :param maxIteration: The maximum iteration for finding the root
    :return: The root of the function if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for i in range(maxIteration):

        # Variable to store the next X
        nextX = currentX - f(currentX) / g(currentX)

        # Save the calculation in the file
        printIntoFile([i + 1, nextX, f(nextX), g(nextX)], None)

        # In case we found our root, Return the root and the iteration number
        if abs(f(nextX)) < ACCURACY:
            return int(nextX * 10 ** 5) / 10 ** 5, i + 1

        # Update the currentX to be the new one
        currentX = nextX

    # In case we didn't find the root within the allowed amount of iteration, Print a fail message and end the program
    printIntoFile(None, "Failed to find the root, Newton Raphson Method isn't suitable")
    print("Failed to find the root, Newton Raphson Method isn't suitable")


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
        file.write('------------------------------- Newton-Raphson Method -------------------------------\n')
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
