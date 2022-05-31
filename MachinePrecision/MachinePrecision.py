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
        ourPrecision = ourPrecision / 2
        loopCounter = loopCounter + 1

    # Your Machine Precision
    print(f'Your Machine Accuracy --> {ourPrecision}')


# Our Program Driver
if __name__ == "__main__":

    print('---------- Machine Precision Method ----------')
    MachinePrecision()
