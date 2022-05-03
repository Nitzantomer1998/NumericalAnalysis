import sympy as sp
from sympy.utilities.lambdify import lambdify


# Global Variable To Set The Wanted Accuracy Solution
MAX_ERROR = 0.00001


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
            root, iteration = bisectionMethod(f, startAt, startAt + 0.1)
            print('The root --> ' + str(root) + '\tIteration --> ' + str(iteration))

        # In case the derivative function change its sign (Mean there's a possibility for a root)
        if g(startAt) * g(startAt + 0.1) < 0:

            # Getting a possible root (The return of the derivative function can be Root or an Extreme point)
            possibleRoot, iteration = bisectionMethod(g, startAt, startAt + 0.1)

            # Checking the possible root is indeed a root
            if abs(f(possibleRoot)) < MAX_ERROR:
                print('The root --> ' + str(possibleRoot) + '\tIteration --> ' + str(iteration))

        # Update our domain for this iteration
        startAt = startAt + 0.1


def bisectionMethod(f, left, right):
    """
    Finding the function f root between the domain [left To right]

    :param f: Our function
    :param left: The left domain of the function
    :param right: The right domain of the function
    :return: The root of the function if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for i in range(100):

        # Variable to store the middle of the function segment
        middle = left + (right - left) / 2

        # In case we found our root, Return the root and the iteration number
        if abs(f(middle)) < MAX_ERROR:
            return int(middle * 10 ** 5) / 10 ** 5, i + 1

        # In case the root is between the left segment To the middle segment, Update right segment to be the middle
        elif f(left) * f(middle) < 0:
            right = middle

        # In case the root is between the middle segment To the right segment, Update left segment to be the middle
        elif f(middle) * f(right) < 0:
            left = middle

    # In case we didn't find the root within the allowed amount iteration, Send fail message and shut down the program
    print('Failed To Find The Root, The Bisection Method Is Not Suitable For This Function')
    exit()


# Our Program Driver
if __name__ == "__main__":
    x = sp.symbols('x')
    function = x ** 4 + x ** 3 - 3 * x ** 2
    domainStart = -3
    domainEnd = 2

    print('---------- Bisection Method ----------')
    rootFinder(function, domainStart, domainEnd)
