# Finding Roots Using Bisection Method

# Libraries for getting the derivative of a function
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Libraries for calculation log
from math import log


ACCURACY = 0.00001


def rootFinder(f, startAt, endAt, maxIteration):
    """
    Method for finding the function Roots

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    :param maxIteration: The maximum iteration for finding the root
    """
    # Variable to store the derivative function
    g = f.diff(x)

    # Activating the functions to be able to get an X
    f = lambdify(x, f)
    g = lambdify(x, g)

    # Divide our function domain range into multiply domains with 0.1 range, then search for each one of them for a root
    while startAt < endAt:

        # In case the root is in the domain edge
        if f(startAt) == 0:
            print(f'The root --> {startAt}    Iteration --> None (Special case)')

            startAt = startAt + 0.1
            continue

        # In case the function changes its sign (Means there's at least one root)
        if f(startAt) * f(startAt + 0.1) < 0:
            root, iteration = Bisection(f, startAt, startAt + 0.1, maxIteration)
            print(f'The root --> {root}    Iteration --> {iteration}')

        # In case the derivative function changes its sign (Mean there's a possibility for a root)
        if g(startAt) * g(startAt + 0.1) < 0:

            # Getting a possibility for a root (Might be a Root or an Extreme point)
            possibleRoot, iteration = Bisection(g, startAt, startAt + 0.1, maxIteration)

            # In case we found a root
            if abs(f(possibleRoot)) == 0:
                print(f'The root --> {possibleRoot}    Iteration --> {iteration}')

        # Update our domain for the next iteration
        startAt = startAt + 0.1


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


# Our Program Driver
if __name__ == "__main__":

    # Function to solve
    x = sp.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domainStart = -3
    domainEnd = 2

    # Variable to store the maximum iteration in order to find the function roots
    allowedIteration = int(-(log(ACCURACY / (domainEnd - domainStart)) / log(2))) + 1

    # Running the program
    print('---------- Bisection Method ----------')
    rootFinder(function, domainStart, domainEnd, allowedIteration)

