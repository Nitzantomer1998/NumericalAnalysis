def Trapezoidal(f, leftDomain, rightDomain, sectionAmount):
    """
    Method for finding the locked Area of the function in the segment domain [leftDomain, rightDomain]

    :param f: Our function
    :param leftDomain: Left domain of the function
    :param rightDomain: Right domain of the function
    :param sectionAmount: The amount of section
    """
    # Variable to store the highest possible section amount without losing information in the process
    sectionAmountLimit = math.sqrt(((rightDomain - leftDomain) ** 3 * MaxFunctionValue(f, leftDomain, rightDomain)) / (12 * ACCURACY))

    # In case the user chose more section than we can perform without losing information
    if sectionAmount > sectionAmountLimit:

        # Appropriate failed message
        print(f'You chose too many section, the limit in this case is {sectionAmountLimit}')

    # Initiate the function to be able to calculate Y base on given x
    f = lambdify(x, f)

    # Calculating step size
    h = (rightDomain - leftDomain) / sectionAmount

    # Initialize the integral value
    integral = f(leftDomain) + f(rightDomain)

    # Calculate the rest of the integral value
    for i in range(1, sectionAmount):
        integral = integral + 2 * f(leftDomain + i * h)

    # Print the area value approximation
    return int(integral * h / 2 * 10 ** 5) / 10 ** 5