# Finding Roots Using Bisection Method


ACCURACY = 0.00001


def Bisection(f, leftDomain, rightDomain, maxIteration):
    """
    Finding the function root in the domain [left To right]

    :param f: Our function
    :param leftDomain: Left domain of the function
    :param rightDomain: Right domain of the function
    :param maxIteration: The maximum iteration for finding the root
    :return: The root of the function if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for i in range(maxIteration):

        # Variable to store the middle of the current function domain
        middle = leftDomain + (rightDomain - leftDomain) / 2

        # In case we found our root, Return the root and the iteration number
        if abs(f(middle)) < ACCURACY:
            return int(middle * 10 ** 5) / 10 ** 5, i + 1

        # In case the root is between the leftDomain To the middle domain, Update the rightDomain to be the middle
        elif f(leftDomain) * f(middle) < 0:
            rightDomain = middle

        # In case the root is between the middle To the rightDomain, Update the leftDomain to be the middle
        elif f(middle) * f(rightDomain) < 0:
            leftDomain = middle

    # In case we didn't find the root within the allowed amount of iteration, Print a fail message and end the program
    print("Failed to find the root, Bisection Method isn't suitable")
