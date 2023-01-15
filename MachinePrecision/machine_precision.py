# Finding This Machine Accuracy Using Machine Precision Method


def find_machine_precision():
    """
    Finding the maximum precision of your machine

    """
    # Variable to store the computer accuracy
    computer_accuracy = 1

    # Variable to store the amount of iteration
    loop_counter = 1

    # Loop to find the maximum precision of your machine
    while 1.0 + (computer_accuracy / 2) > 1.0:
        # Printing the calculation into the calculation file
        print_into_file([loop_counter, computer_accuracy, '\\', 2, '=', computer_accuracy / 2], None)

        # Updating the computer accuracy value and the iteration number
        computer_accuracy /= 2
        loop_counter += 1

    # Saving the final machine precision value
    print_into_file(None, f'\nThis Machine Maximum Accuracy --> {computer_accuracy}')

    # Printing the final machine precision value
    print(f'This Machine Maximum Accuracy --> {computer_accuracy}')


def print_into_file(data, message):
    """
    Printing the content into the calculation file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    """
    # Open file and save the sent content
    with open('..\\Calculation.txt', 'a+') as file:

        # In case we sent a message
        if message:
            file.write(message)

        # In case we sent a data
        if data:
            for i in range(len(data)):
                if i == 0:
                    file.write('{: ^25}'.format(f'({data[0]})'))

                else:
                    file.write(f'{data[i]} ')
            file.write('\n')


def reset_file():
    """
    Resetting the calculation file

    """
    with open('..\\Calculation.txt', 'w') as file:
        file.write('------------------------------- Machine Precision Method -------------------------------\n')
        file.write('{: ^25}Calculation\n'.format('Iteration'))


# The Program Driver
if __name__ == "__main__":
    # Reset the calculation file
    reset_file()

    # Running the program
    print('---------- Machine Precision Method ----------')
    find_machine_precision()
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
