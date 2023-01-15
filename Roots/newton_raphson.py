# Finding Functions Roots Using Newton Raphson Method


# Libraries for getting the derivative of a function
import sympy


def root_finder(f, left_domain, right_domain, max_iteration_allowed):
    """
    Finding the function roots

    :param f: Our function
    :param left_domain: The domain start of the function
    :param right_domain: The domain end of the function
    :param max_iteration_allowed: The maximum iteration allowed for finding a root
    """
    # Variable to store the derivative functions
    g = f.diff(x)
    h = g.diff(x)

    # Activating the functions to be able to calculate for a specific X
    f = sympy.utilities.lambdify(x, f)
    g = sympy.utilities.lambdify(x, g)
    h = sympy.utilities.lambdify(x, h)

    # Divide the function domain range into multiply domains with 0.1 range, then search for each one of them for a root
    while left_domain < right_domain:

        # if the root is in the current domain section edge
        if f(left_domain) == 0:

            # Saving the root
            print_into_file(None, f'Root --> {left_domain}    Iteration --> 0')

            # Printing the root
            print(f'Root --> {left_domain}    Iteration --> 0')

        # if the function changes its sign (there's at least one root)
        elif f(left_domain) * f(left_domain + 0.1) < 0:

            # Getting the root in this domain section, and the amount of iteration used
            root, iteration = newton_raphson_method(f, g, left_domain + 0.05, max_iteration_allowed)

            # Saving the root
            print_into_file(None, f'Root --> {root}    Iteration --> {iteration}')

            # Printing the root
            print(f'Root --> {root}    Iteration --> {iteration}')

        # else if the derivative function changes its sign (there's a possibility for a root)
        elif g(left_domain) * g(left_domain + 0.1) < 0:

            # Getting a possibility for a root (might be a root or an extreme point), and the amount of iteration used
            possible_root, iteration = newton_raphson_method(g, h, left_domain + 0.05, max_iteration_allowed)

            # if we found a root
            if abs(f(possible_root)) < solution_accuracy:
                # Saving the root
                print_into_file(None, f'Root --> {possible_root}    Iteration --> {iteration}')

                # Printing the root
                print(f'Root --> {possible_root}    Iteration --> {iteration}')

        # Updating the new domain for the next iteration
        left_domain += 0.1


def newton_raphson_method(f, g, current_x, max_iteration_allowed):
    """
    Returning the function root

    :param f: Our function
    :param g: The derivative function of f
    :param current_x: The middle domain value of the function
    :param max_iteration_allowed: The maximum iteration allowed for finding a root
    :return: The root of the function if existed, else according failed message
    """
    # loop for finding a root within the allowed iteration amount
    for i in range(max_iteration_allowed):

        # Variable to store the next_x value
        next_x = current_x - f(current_x) / g(current_x)

        # Save the calculation
        print_into_file([i + 1, next_x, f(next_x), g(next_x)], None)

        # if we found the root, Return the root and the amount of iteration used
        if abs(f(next_x)) < solution_accuracy:
            return int(next_x * 10 ** 5) / 10 ** 5, i + 1

        # Updating the current_x value to be the new found one
        current_x = next_x

    # if we haven't found the root within the allowed amount of iteration, Print a fail message
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
    """
    Printing the content into the calculation file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    """
    # Open file and save the sent content
    with open('..\\Calculation.txt', 'a+') as file:

        # if we sent a message
        if message:
            file.write('\n{: ^25}\n'.format(message))
            file.write('--------------------------------------------------------------------------------------------\n')

        # if we sent a data
        if data:
            for i in range(len(data)):
                file.write('{: ^25}'.format(float(data[i])))
            file.write('\n')


def reset_file():
    """
    Resetting the calculation file

    """
    with open('..\\Calculation.txt', 'w') as file:
        file.write('------------------------------- Newton Raphson Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}{: ^25}\n'.format('Iteration', 'x', 'f(x)', "f'(x)"))


# The Program Driver
if __name__ == "__main__":
    # Reset the calculation file
    reset_file()

    # Input section
    x = sympy.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domain_start = -3
    domain_end = 2
    solution_accuracy = 0.00001

    # Running the program
    print('---------- Newton Raphson Method ----------')
    root_finder(function, domain_start, domain_end, calculate_max_iteration_allowed(domain_start, domain_end))
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
