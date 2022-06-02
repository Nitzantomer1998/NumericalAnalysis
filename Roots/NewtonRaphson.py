# Finding Roots Using Newton Raphson Method


def NewtonRaphson(f, g, currentX, maxIteration):
    """
    Finding the function root

    :param f: Our function
    :param g: The derivative function of f
    :param currentX: The value of the middle domain range of the function
    :param maxIteration: The maximum iteration for finding the root
    :return: The root of the function if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for i in range(maxIteration):

        # Variable to store the next X
        nextX = currentX - f(currentX) / g(currentX)

        # In case we found our root, Return the root and the iteration number
        if abs(f(nextX)) < 0.00001:
            return int(nextX * 10 ** 5) / 10 ** 5, i + 1

        # Update the currentX to be the new one
        currentX = nextX

    # In case we didn't find the root within the allowed amount of iteration, Print a fail message and end the program
    print("Failed to find the root, Newton Raphson Method isn't suitable")