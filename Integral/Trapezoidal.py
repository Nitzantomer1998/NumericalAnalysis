def Trapezoidal(f, leftDomain, rightDomain, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [leftDomain, rightDomain]

    :param f: Our function
    :param leftDomain: Left domain of the function
    :param rightDomain: Right domain of the function
    :param sectionAmount: The amount of section
    """
    sectionAmountLimit = math.sqrt(((rightDomain - leftDomain) ** 3 * MaxFunctionValue(f, leftDomain, rightDomain)) / (12 * ACCURACY))

    if sectionAmount > sectionAmountLimit:

        print(f'You chose too many section, the limit in this case is {sectionAmountLimit}')

    f = lambdify(x, f)

    h = (rightDomain - leftDomain) / sectionAmount

    integral = f(leftDomain) + f(rightDomain)

    for i in range(1, sectionAmount):
        integral = integral + 2 * f(leftDomain + i * h)

    return int(integral * h / 2 * 10 ** 5) / 10 ** 5


def MaxFunctionValue(f, startAt, endAt):
    """
    Method for finding the highest point of a function

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    """
    g = f.diff(x)

    f = lambdify(x, f)
    g = lambdify(x, g)

    maxIteration = int(-(log(ACCURACY / (domainEnd - domainStart)) / log(2))) + 1

    maxValue = max(f(startAt), f(endAt))

    while startAt < endAt:

        if g(startAt) * g(startAt + 0.1) < 0:

            possiblePoint = Secant(g, startAt, startAt + 0.1, maxIteration)

            if f(possiblePoint) > maxValue:
                maxValue = f(possiblePoint)

        startAt = startAt + 0.1

    return maxValue


def Secant(f, previewX, currentX, maxIteration):
    """
    Finding the function root in the domain range [left To right]

    :param f: Our function
    :param previewX: Left domain of the function
    :param currentX: Right domain of the function
    :param maxIteration: The maximum iteration for finding the root
    :return: The root of the function if existed, else according failed message
    """
    for i in range(maxIteration):

        nextX = (previewX * f(currentX) - currentX * f(previewX)) / (f(currentX) - f(previewX))

        if abs(f(nextX)) < ACCURACY:
            return nextX

        previewX = currentX

        currentX = nextX

    print("Failed to find the root, Secant Method isn't suitable")
