# Finding Area Value Using Simpson Rule Method


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

    # Initialize the area summation
    area = 0

    # Loop to calculate the area
    for i in range(1, section_amount + 1):
        # Calculate the values for the current interval
        interval_start_x = left_domain + (i - 1) * h
        interval_start_y = f(interval_start_x)

        interval_end_x = left_domain + i * h
        interval_end_y = f(interval_end_x)

        mid_point_x = (interval_start_x + interval_end_x) / 2
        mid_point_y = f(mid_point_x)

        width = interval_end_x - interval_start_x
        height = (interval_start_y + 4 * mid_point_y + interval_end_y) * h / 6
        area += height

        # Save the calculation
        print_into_file(
            [interval_start_x, interval_start_y, mid_point_x, mid_point_y, interval_end_x, interval_end_y, width,
             height, area], None)

    # Save the area
    print_into_file(None, f'Sum Of Area --> {int(area * 10 ** 5) / 10 ** 5}')

    # Print the area value
    print(f'Sum Of Area --> {int(area * 10 ** 5) / 10 ** 5}')


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
        left_domain += 0.1

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
    max_section_amount = ((abs(right_domain - left_domain) ** 3 * max_function_value(f, left_domain, right_domain)) / (
            12 * solution_accuracy)) ** 0.5

    if section_amount > max_section_amount:
        print(f'You Chose Too Many Section, The Upper Limit Is {int(max_section_amount)}')
        return False

    # if the section amount is lower than the minimum of section to be performed without losing information
    min_section_amount = (abs(right_domain - left_domain) ** 5 * max_function_value(f.diff(x).diff(x).diff(x).diff(x),
                                                                                    left_domain, right_domain) / (
                                  180 * solution_accuracy)) ** 0.25

    if section_amount + 1 < min_section_amount:
        print(f'You Chose Below The Minimum Section, The Lower Limit Is {int(min_section_amount)}')
        return False

    # Returning true (inserted data is valid)
    return True


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
        file.write('------------------------------- Simpson Rule Method -------------------------------\n')
        file.write('{: ^25}{: ^25}{: ^25}{: ^25}{: ^25}{: ^25}{: ^25}{: ^25}{: ^25}\n'.format('Interval_Start',
                                                                                              'f(Interval_Start)',
                                                                                              'Midpoint', 'f(Midpoint)',
                                                                                              'Interval_End',
                                                                                              'f(Interval_End)',
                                                                                              'Width', 'Height = Area',
                                                                                              'Sum Area'))


# The Program Driver
if __name__ == "__main__":
    # Reset the calculation file
    reset_file()

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
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
 
