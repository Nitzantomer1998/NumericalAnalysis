# Machine Precision Finder


def MachinePrecision():
    """
    Finding the machine precision

    """
    # Variable to store our machine precision
    ourPrecision = 1

    # Variable to store the amount of iteration
    loopCounter = 1

    # Loop for finding the Machine Precision
    while 1.0 + (ourPrecision / 2) > 1.0:
        printIntoFile([loopCounter, ourPrecision, '\\', 2, '=', ourPrecision / 2], None)
        ourPrecision = ourPrecision / 2
        loopCounter = loopCounter + 1

    # Your Machine Precision
    printIntoFile(None, f'\nYour Machine Accuracy --> {ourPrecision}')
    print(f'Your Machine Accuracy --> {ourPrecision}')


def printIntoFile(data, message):
    """
    Printing the content into a specified file

    :param data: Data is a list representing matrix
    :param message: Message is a string representing a message
    """
    # Open file and save the sent data
    with open('Calculation.txt', 'a+') as file:

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


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------- Machine Precision Method -------------------------------\n')
        file.write('{: ^25}Calculation\n'.format('Iteration'))


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    print('---------- Machine Precision Method ----------')
    MachinePrecision()
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
