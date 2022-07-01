def Simpson(f, leftDomain, rightDomain, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [leftDomain, rightDomain]

    :param f: Our function
    :param leftDomain: Left domain of the function
    :param rightDomain: Right domain of the function
    :param sectionAmount: The amount of section
    """
    sectionAmountMaxLimit = ((abs(rightDomain - leftDomain) ** 3 * MaxFunctionValue(f, leftDomain, rightDomain)) / (12 * ACCURACY)) ** 0.5

    sectionAmountMinLimit = (abs(rightDomain - leftDomain) ** 5 * MaxFunctionValue(f.diff(x).diff(x).diff(x).diff(x), leftDomain, rightDomain) / (180 * ACCURACY)) ** 0.25

    if sectionAmount <= 0:
        print('You can not divide section to be negative')
        return

    if sectionAmount % 2 == 1:
        print('Section amount must be an even number')
        return

    if sectionAmount > sectionAmountMaxLimit:
        print(f'You chose too many section, the upper limit is {int(sectionAmountMaxLimit)}')
        return

    if sectionAmount + 1 < sectionAmountMinLimit:
        print(f'You chose below the minimum section, the lower limit is {int(sectionAmountMinLimit)}')
        return

    f = lambdify(x, f)

    h = abs(rightDomain - leftDomain) / sectionAmount

    interval = f(leftDomain) + f(rightDomain)

    for i in range(1, sectionAmount):

        if i % 2 == 0:
            interval = interval + 2 * f(i * h + leftDomain)

        else:
            interval = interval + 4 * f(i * h + leftDomain)

    print(f'Sum of the area --> {int(1 / 3 * h * interval * 10 ** 5) / 10 ** 5}')


def MaxFunctionValue(f, startAt, endAt):
    """
    Method for finding the highest point of a function

    :param f: Our function
    :param startAt: Left domain of the function
    :param endAt: Right domain of the function
    """
    f = lambdify(x, f)

    maxValue = max(f(startAt), f(endAt))

    while startAt < endAt:

        maxValue = max(maxValue, f(startAt))

        startAt = startAt + 0.1

    return maxValue
