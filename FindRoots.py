import math

import sympy as sp
from sympy import ln
from sympy.utilities.lambdify import lambdify


# Global Variable To Set The Wanted Accuracy Solution
MAX_ERROR = 10 ** -10


def bisectionMethod(f, left, right, maxIteration):
    """
    Finding the axis X value when Axis Y equal zero

    :param f: Our function
    :param left: The left segment border of the function
    :param right: The right segment border of the function
    :param maxIteration: The maximum amount of iteration allowed
    :return: The root of the function in the segment [left To right] if existed, else according failed message
    """
    # Search the root within the maximum allowed iteration
    for _ in range(maxIteration):

        # Variable to store the middle of the function segment
        middle = left + (right - left) / 2

        # In case we found our root, Return it
        if abs(f(middle)) < MAX_ERROR:
            return middle

        # In case the root is between the left segment To the middle segment, Update right segment to be the middle
        elif f(left) * f(middle) < 0:
            right = middle

        # In case the root is between the middle segment To the right segment, Update left segment to be the middle
        elif f(middle) * f(right) < 0:
            left = middle

    # In case we didn't find the root within the allowed amount iteration, Send according message
    print('Doesnt Work For This Method')


def rootSearchMethod(f, left, right):
    """
    Method for getting the functions Roots

    :param f: Our function
    :param left: The left segment border of the function
    :param right: The right segment border of the function
    """
    derivativeF = f.diff(x)
    f = lambdify(x, f)
    derivativeF = lambdify(x, derivativeF)

    maxIteration = int(-(ln(MAX_ERROR / (right - left)) / ln(2))) + 1

    # Divide our function segment range into multiply segments with 0.1 range segment and search for each of them a root
    while left < right:
        left = left + 0.1

        if f(left - 0.1) * f(left) < 0:
            roots.append(bisectionMethod(f, left - 0.1, left, maxIteration))

        if derivativeF(left - 0.1) * derivativeF(left) < 0:
            possibleRoot = bisectionMethod(derivativeF, left - 0.1, left, maxIteration)

            if abs(f(possibleRoot)) < MAX_ERROR:
                roots.append(possibleRoot)

    for i in range(len(roots)):
        test = roots[i] * 10 ** int(-math.log10(MAX_ERROR))
        roots[i] = int(test) / 10 ** int(-math.log10(MAX_ERROR))

    print(roots)


roots = []
x = sp.symbols('x')
function = x ** 4 + x ** 3 - 3 * x ** 2
rootSearchMethod(function, -3, 2)
