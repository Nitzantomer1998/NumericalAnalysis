# Machine Precision Finder


def machinePrecision():
    """
    Finding the machine precision

    """
    # Variable to store our machine precision
    ourPrecision = 1

    # Variable to store the amount of iteration
    loopCounter = 1

    # Loop for finding the Machine Precision
    while 1.0 + (ourPrecision / 2) > 1.0:
        printIntoFile([loopCounter, ourPrecision, '\\', 2, '=', ourPrecision / 2], False)
        ourPrecision = ourPrecision / 2
        loopCounter = loopCounter + 1

    # Your Machine Precision
    printIntoFile(f'\nYour Epsilon Machine --> {ourPrecision}', True)
    print(f'Your Epsilon Is --> {ourPrecision}')


def printIntoFile(data, isFinal):
    """
    Printing the data content into a specified file

    :param data: Data is a list representing the arguments
    :param isFinal: If True, We print the solution, Else we print the calculation
    """
    # Open file and save the sent data
    with open('Calculation.txt', 'a+') as file:

        # In case it's the solution
        if isFinal:
            file.write(f'{data}')

        else:
            for i in range(len(data)):
                if i == 0:
                    file.write('{: ^22}'.format(f'({data[0]})'))

                else:
                    file.write(f'{data[i]} ')
            file.write('\n')


def resetFile():
    """
    Reset the calculation file

    """
    with open('Calculation.txt', 'w') as file:
        file.write('------------------------------- Machine Precision Method -------------------------------\n')
        file.write('{: ^22}'.format('Iteration') + 'Calculation\n')


# Our Program Driver
if __name__ == "__main__":

    # Reset the calculation file
    resetFile()

    print('---------- Machine Precision Method ----------')
    machinePrecision()
    print('\n\nCalculation Is Done, Check File "Calculation" For More Information')
