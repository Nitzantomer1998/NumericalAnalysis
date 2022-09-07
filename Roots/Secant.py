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
        file.write('------------------------------- Secant Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}{: ^25}\n'.format('Iteration', 'previewX', 'nextX', "f(nextX)"))

         
if __name__ == "__main__":

    reset_file()

    x = sympy.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domain_start = -3
    domain_end = 2
    solution_accuracy = 0.00001

    print('---------- Secant Method ----------')
    root_finder(function, domain_start, domain_end, calculate_max_iteration_allowed(domain_start, domain_end))
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
