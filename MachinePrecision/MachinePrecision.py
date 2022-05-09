# Author: Nitzan Tomer.
# Machine Precision.

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
# Variables
ourEpsilon = 1
loopsNum = 0

# "Function" To Find Your Machine Precision
print("\n[Machine Precision Find]")
while 1.0 + (ourEpsilon / 2) > 1.0:
    print(f'({loopsNum}) {ourEpsilon} \\ 2 = {ourEpsilon / 2}')
    loopsNum = loopsNum + 1
    ourEpsilon = ourEpsilon / 2

# Your Own Machine Precision
print(f'Your Epsilon Is --> {ourEpsilon}\n')
