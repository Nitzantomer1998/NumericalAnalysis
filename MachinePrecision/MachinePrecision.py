# Machine Precision Finder


# Global Variable [Only Used To print the iteration number]
PRINT_COUNTER = 1


def printIntoFile(data, message, isFinal):
    """
    Printing the data and the message content into a specified file

    :param data: Data is a list representing the calculation variables
    :param message: Message is a String representing the data explanation
    :param isFinal: Indicate if we sent our solution
    """
    # Our Global Variable To Count The Iteration Number
    global PRINT_COUNTER

    # In Case We Are Running A Calculation, It will create a new file with the method name
    if PRINT_COUNTER == 1:
        file = open('MP_Calculation.txt', 'w')
        file.write('------------------------------ Machine Precision Method ------------------------------\n')
        file.write('{: ^22}'.format('Iteration') + 'Calculation\n')
        file.close()

    # Open the file and save the data
    with open('MP_Calculation.txt', 'a+') as file:

        if isFinal:
            # Saving the Solution
            file.write(f'{message}{data}')

        else:
            # Saving the Calculation
            if PRINT_COUNTER > 0:
                for i in range(len(data)):
                    if i == 0:
                        file.write('{: ^22}'.format(f'({PRINT_COUNTER})'))

                    file.write(f'{data[i]} ')
                file.write('\n')

        # Increase Our Global Iteration Counter Variable
        PRINT_COUNTER = PRINT_COUNTER + 1


def machinePrecisionMethod():

    # Variable
    ourEpsilon = 1

    # Loop To Find The Machine Precision
    print("[Machine Precision Finder]")
    while 1.0 + (ourEpsilon / 2) > 1.0:
        printIntoFile([ourEpsilon, '\\', 2, '=', ourEpsilon / 2], None, False)
        ourEpsilon = ourEpsilon / 2

    # Your Own Machine Precision
    printIntoFile(ourEpsilon, '\nYour Epsilon Machine --> ', True)
    print(f'Your Epsilon Is --> {ourEpsilon}')


# Our Program Driver
if __name__ == "__main__":
    machinePrecisionMethod()
    print('Calculation Is Done, Check File "MP_Calculation" For More Information')
