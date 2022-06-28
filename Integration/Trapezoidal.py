def Trapezoidal(f, leftDomain, rightDomain, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [leftDomain, rightDomain]

    :param f: Our function
    :param leftDomain: Left domain of the function
    :param rightDomain: Right domain of the function
    :param sectionAmount: The amount of section
    """
    sectionAmountLimit = (((rightDomain - leftDomain) ** 3 * MaxFunctionValue(f, leftDomain, rightDomain)) / (12 * ACCURACY)) ** 0.5

    if sectionAmount > sectionAmountLimit:

        print(f'You chose too many section, the limit is {sectionAmountLimit}')

    f = lambdify(x, f)

    h = (rightDomain - leftDomain) / sectionAmount

    integral = f(leftDomain) + f(rightDomain)

    for i in range(1, sectionAmount):
        integral = integral + 2 * f(leftDomain + i * h)

    print(f'Sum of the area --> {int(h / 2 * integral * 10 ** 5) / 10 ** 5}')
