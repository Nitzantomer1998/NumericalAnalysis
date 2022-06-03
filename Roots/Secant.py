# Finding Roots Using Secant Method


def Secant(f, previewX, currentX, maxIteration):
    """
    Finding the function root in the domain range [left To right]

    :param f: Our function
    :param previewX: Left domain of the function
    :param currentX: Right domain of the function
    :param maxIteration: The maximum iteration for finding the root
    :return: The root of the function if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for i in range(maxIteration):

        # Variable to store the next X
        nextX = (previewX * f(currentX) - currentX * f(previewX)) / (f(currentX) - f(previewX))

        # In case we found our root, Return the root and the iteration number
        if abs(f(nextX)) < 0.0001:
            return int(nextX * 10 ** 5) / 10 ** 5, i + 1

        # Update the previewX to be the currentX
        previewX = currentX

        # Update the currentX to be new one
        currentX = nextX

    # In case we didn't find the root within the allowed amount iteration, Print fail message and shut down the program
    print("Failed to find the root, Secant Method isn't suitable")
