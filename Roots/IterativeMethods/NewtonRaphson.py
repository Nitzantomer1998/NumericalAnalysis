# Finding The Roots In The Newton-Raphson Method


# Libraries
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Libraries for calculation log
from math import log

# Global Variable To Set The Solution Accuracy
ACCURACY = 0.00001


def rootFinder(f, startAt, endAt):
    """
    Method for getting the function Roots

    :param f: Our function
    :param startAt: The left domain of the function
    :param endAt: The right domain of the function
    """
    # Variables to store our derivative function
    g = f.diff(x)
    h = g.diff(x)

    # Making our function be able to get an X
    f = lambdify(x, f)
    g = lambdify(x, g)
    h = lambdify(x, h)

    # Divide our function domain range into multiply domains with 0.1 range, then search for each one of them for a root
    while startAt < endAt:

        # In case the function changes its sign (It means there's at least one root)
        if f(startAt) * f(startAt + 0.1) < 0:
            root, iteration = newtonRaphsonMethod(f, g, startAt + 0.05)
            print('The root --> ' + str(root) + '\tIteration --> ' + str(iteration))

        # In case the derivative function changes its sign (Mean there's a possibility for a root)
        if g(startAt) * g(startAt + 0.1) < 0:

            # Getting a possible root (The return of the derivative function can be a Root or an Extreme point)
            possibleRoot, iteration = newtonRaphsonMethod(g, h, startAt + 0.05)

            # Checking the possible root is indeed a root
            if abs(f(possibleRoot)) < ACCURACY:
                print('The root --> ' + str(possibleRoot) + '\tIteration --> ' + str(iteration))

        # Update our domain for the next iteration
        startAt = startAt + 0.1


def newtonRaphsonMethod(f, g, currentX):
    """
    Finding the function f root

    :param f: Our function
    :param g: The derivative function of f
    :param currentX: The value of the middle domain range of the function
    :return: The root of the function if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for i in range(100):

        # Variable to store the next X
        nextX = currentX - f(currentX) / g(currentX)

        # In case we found our root, Return root and the iteration number
        if abs(nextX - currentX) < ACCURACY:
            return int(nextX * 10 ** 5) / 10 ** 5, i + 1

        # Update the currentX to be the new one
        currentX = nextX

    # In case we didn't find the root within the allowed amount of iteration, Print a fail message and end the program
    print('Failed To Find The Root, The Newton Raphson Method Is Not Suitable For This Function')
    exit()


# Our Program Driver
if __name__ == "__main__":
    x = sp.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domainStart = -3
    domainEnd = 2
    
    # Variable to store the maximum iteration in order to find the function roots
    allowedIteration = int(-(log(ACCURACY / (domainEnd - domainStart)) / log(2))) + 1

    print('---------- Newton Raphson Method ----------')
    rootFinder(function, domainStart, domainEnd)
