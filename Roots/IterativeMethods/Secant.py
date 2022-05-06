# Finding The Roots In The Secant Method


# Libraries
import sympy as sp
from sympy.utilities.lambdify import lambdify

# Global Variable To Set The Solution Accuracy
ACCURACY = 0.00001


def rootFinder(f, startAt, endAt):
    """
    Method for getting the functions Roots

    :param f: Our function
    :param startAt: The left domain of the function
    :param endAt: The right domain of the function
    """
    # Variables to store our derivative function
    g = f.diff(x)

    # Making our function be able to get an X
    f = lambdify(x, f)
    g = lambdify(x, g)

    # Divide our function domain range into multiply domains with 0.1 range, then search for each one of them for a root
    while startAt < endAt:

        # In case the function change its sign (Means there's at least one root)
        if f(startAt) * f(startAt + 0.1) < 0:
            root, iteration = secantMethod(f, startAt, startAt + 0.1)
            print('The root --> ' + str(root) + '\tIteration --> ' + str(iteration))

        # In case the derivative function change its sign (Mean there's a possibility for a root)
        if g(startAt) * g(startAt + 0.1) < 0:

            # Getting a possible root (The return of the derivative function can be Root or an Extreme point)
            possibleRoot, iteration = secantMethod(g, startAt, startAt + 0.1)

            # Checking the possible root is indeed a root
            if abs(f(possibleRoot)) < ACCURACY:
                print('The root --> ' + str(possibleRoot) + '\tIteration --> ' + str(iteration))

        # Update our domain for this iteration
        startAt = startAt + 0.1


def secantMethod(f, previewX, currentX):
    """
    Finding the function f root between the domain range [previewX To currentX]

    :param f: Our function
    :param previewX: The left domain of the function
    :param currentX: The right domain of the function
    :return: The root of the function in the domain [previewX To currentX] if existed, else according failed message
    """

    # Search the root within the maximum allowed iteration
    for i in range(100):

        # Variable to store the next X
        nextX = (previewX * f(currentX) - currentX * f(previewX)) / (f(currentX) - f(previewX))

        # In case we found our root, Return the root and the iteration number
        if abs(nextX - currentX) < ACCURACY:
            return int(nextX * 10 ** 5) / 10 ** 5, i + 1

        # Update the previewX to be the currentX
        previewX = currentX

        # Update the currentX to be new one
        currentX = nextX

    # In case we didn't find the root within the allowed amount iteration, Send fail message and shut down the program
    print('Failed To Find The Root, The Secant Method Is Not Suitable For This Function')
    exit()


# Our Program Driver
if __name__ == "__main__":
    x = sp.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domainStart = -3
    domainEnd = 2

    print('---------- Secant Method ----------')
    rootFinder(function, domainStart, domainEnd)
