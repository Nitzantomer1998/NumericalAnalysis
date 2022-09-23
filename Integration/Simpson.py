# Finding Area Value Using Simpson Method


# Libraries for getting the derivatives of a function
import sympy


def simpson_rule_method(f, left_domain, right_domain, section_amount):
    """
    Finding the locked Area of the function in the sent segment domain [left_domain, right_domain]

    :param f: Our function
    :param left_domain: The domain start of the function
    :param right_domain: The domain end of the function
    :param section_amount: The amount of section
    """
    # if the sent inserted data isn't valid, stop the program
    if not is_inserted_data_valid(f, left_domain, right_domain, section_amount):
        return

    # Activating the function to be able to calculate for a specific X
    f = sympy.utilities.lambdify(x, f)

    # Calculating step size
    h = abs(right_domain - left_domain) / section_amount

    # Initialize the interval value
    interval = f(left_domain) + f(right_domain)

    # Calculate the rest of the interval value
    for i in range(1, section_amount):

        # if the index is even
        if i % 2 == 0:
            interval = interval + 2 * f(i * h + left_domain)

        # if the index is odd
        else:
            interval = interval + 4 * f(i * h + left_domain)

    # Print the area value
    print(f'Sum Of The Area --> {int(1 / 3 * h * interval * 10 ** 5) / 10 ** 5}')


def max_function_value(f, left_domain, right_domain):
    """
    Returning the highest Y value of the sent function in the sent domain

    :param f: Our function
    :param left_domain: The domain start of the function
    :param right_domain: The domain end of the function
    """
    # Activating the function to be able to calculate for a specific X
    f = sympy.utilities.lambdify(x, f)

    # Variable to store the max value of the function (Axis Y)
    max_value = max(f(left_domain), f(right_domain))

    # Divide our function domain range into multiply domains with 0.1 range
    while left_domain < right_domain:

        # Update the maximum Y value of the function
        max_value = max(max_value, f(left_domain))

        # Update our domain for the next iteration
        left_domain = left_domain + 0.1

    # Return the highest Y value in the function domain
    return max_value


def is_inserted_data_valid(f, left_domain, right_domain, section_amount):
    """
    Checking if the inserted segment domain and section amount are valid, and return accordingly

    :param f: Our function
    :param left_domain: The domain start of the function
    :param right_domain: The domain end of the function
    :param section_amount: The amount of section
    :return: True if the sent data valid, else False
    """
    # if the section amount is negative
    if section_amount <= 0:
        print('Error: Section Amount Must Be Non Negative Integer')
        return False

    # if the section amount is not an even integer
    if section_amount % 2 == 1:
        print('Section Amount Must Be An Even Integer')
        return False

    # if the section amount is greater than the maximum of section to be performed without losing information
    max_section_amount = ((abs(right_domain - left_domain) ** 3 * max_function_value(f, left_domain, right_domain)) / (12 * solution_accuracy)) ** 0.5
    if section_amount > max_section_amount:
        print(f'You Chose Too Many Section, The Upper Limit Is {int(max_section_amount)}')
        return False

    # if the section amount is lower than the minimum of section to be performed without losing information
    min_section_amount = (abs(right_domain - left_domain) ** 5 * max_function_value(f.diff(x).diff(x).diff(x).diff(x), left_domain, right_domain) / (180 * solution_accuracy)) ** 0.25
    if section_amount + 1 < min_section_amount:
        print(f'You Chose Below The Minimum Section, The Lower Limit Is {int(min_section_amount)}')
        return False

    # Returning true (inserted data is valid)
    return True


# The Program Driver
if __name__ == "__main__":

    # Input section
    x = sympy.symbols('x')
    function = sympy.sin(x)
    domain_start = 0
    domain_end = sympy.pi
    section_divide = 20
    solution_accuracy = 0.00001

    # Running the program
    print('---------- Simpson Rule Method ----------')
    simpson_rule_method(function, domain_start, domain_end, section_divide)
